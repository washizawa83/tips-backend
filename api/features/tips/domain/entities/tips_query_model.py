import typing
from datetime import datetime

from pydantic import Field

from api.features.tips.domain.entities.tips_common_model import TipsBaseModel
from api.features.tips.domain.entities.tips_entity import TipsEntity


class TipsReadModel(TipsBaseModel):
    id: str
    good: int = Field(0)
    is_public: bool
    updated_at: datetime
    created_at: datetime

    class Config(object):
        orm_mode = True

    @classmethod
    def from_entity(cls, entity: TipsEntity) -> 'TipsReadModel':
        return cls(
            id=entity.id,
            user_id=entity.user_id,
            text=entity.text,
            tags=entity.tags,
            good=entity.good,
            is_public=entity.is_public,
            updated_at=entity.updated_at,
            created_at=entity.created_at
        )
