from typing import List
from pydantic import Field, BaseModel


class TipsBaseModel(BaseModel):
    user_id: str
    text: str
    tags: List[str]
