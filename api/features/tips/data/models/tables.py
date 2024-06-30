import uuid
from datetime import datetime
from sqlalchemy import Boolean, Column, String, Integer, TIMESTAMP, JSON, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy_utils import UUIDType
from sqlalchemy.sql import func

from api.features.tips.domain.entities.tips_entity import TipsEntity
from api.features.tips.domain.entities.tips_query_model import TipsReadModel

Base = declarative_base()


class Tip(Base):
    __tablename__ = 'tips'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    user_id = Column(String(50))
    text = Column(JSON, nullable=False)
    good = Column(Integer)
    is_public = Column(Boolean, default=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(),
                        onupdate=func.current_timestamp())
    created_at = Column(TIMESTAMP, server_default=func.now())
    tags = relationship('Tag', secondary='tip_tags',
                        back_populates='tips', cascade='all, delete')

    def to_entity(self) -> TipsEntity:
        return TipsEntity(
            id=self.id,
            user_id=self.user_id,
            text=self.text,
            tags=self.tags,
            is_public=self.is_public,
            updated_at=self.updated_at,
            created_at=self.created_at
        )

    def to_read_model(self) -> TipsReadModel:
        return TipsReadModel(
            id=str(self.id),
            user_id=str(self.user_id),
            text=self.text,
            tags=[tag.name for tag in self.tags],
            is_public=self.is_public,
            updated_at=self.updated_at,
            created_at=self.created_at
        )


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String(50))
    tips = relationship('Tip', secondary='tip_tags',
                        back_populates='tags', order_by=lambda: Tip.updated_at.desc())


tag_relation = Table(
    'tip_tags', Base.metadata,
    Column('tips_id', UUIDType(binary=False),
           ForeignKey('tips.id'), primary_key=True),
    Column('tags_id', UUIDType(binary=False),
           ForeignKey('tags.id'), primary_key=True)
)

DB_URL = "mysql+pymysql://root@db:3306/tips?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
