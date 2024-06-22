from typing import List
from datetime import datetime


class TipsEntity(object):
    def __init__(
        self,
        id: str,
        user_id: str,
        text: str,
        tags: List[str],
        good: int,
        is_public: bool,
        updated_at: datetime,
        created_at: datetime
    ):
        self.id = id,
        self.user_id = user_id,
        self.text = text,
        self.tags = tags,
        self.good = good,
        self.is_public = is_public
        self.updated_at = updated_at
        self.created_at = created_at

    def __eq__(self, other) -> bool:
        if isinstance(other, TipsEntiry):
            return self.id == other.id
        return False
