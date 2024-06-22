from typing import List, Optional
from pydantic import BaseModel, Field


class TipsBase(BaseModel):
    user_id: str
    text: str
    tags: List[str]


class Tips(TipsBase):
    id: str
    good: int = Field(0)
    updated_at: str
    created_at: str


class TipsCreate(TipsBase):
    pass
