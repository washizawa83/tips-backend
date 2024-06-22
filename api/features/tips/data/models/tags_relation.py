from api.core.models.mysql.models import Base

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy_utils import UUIDType

from app.core.models.postgres.models import Base


class TagRelation():
    __tablename__ = 'tag_relation'

    tips_id: UUIDType = Column(
        'tips_id', ForeignKey('tips.id'), primary_key=True)
    tags_id: UUIDType = Column(
        'tags_id', ForeignKey('tags.id'), primary_key=True)
