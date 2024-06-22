from api.core.models.mysql.models import Base

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped

from app.core.models.postgres.models import Base


class Tags(Base):
    __tablename__ = 'tags'

    name: str = Column('name', String, )
    tips = relationship('tips', secondary='tag_relation',
                        back_populates='tags')
