from api.core.models.mysql.models import Base

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped

from app.core.models.postgres.models import Base
from app.features.task.domain.entities.tips_entity import TipsEntity
from app.features.task.domain.entities.tips_query_model import TipsReadModel


class Tips(Base):
    __tablename__ = 'tips'

    user_id: str = Column('user_id', String)
    text: str = Column('text', String)
    tags = relationship('tags', secondary='tag_relation',
                        back_populates='tips')
    good: int = Column('good', Integer)
    is_public: bool = Column('is_public', Boolean, default=False)
