from typing import Sequence, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from api.features.tips.data.models.tables import Tip, Tag
from api.features.tips.domain.entities.tips_query_model import TipsReadModel
from api.features.tips.domain.services.tips_query_service import TipsQueryService


class TipsQueryServiceImpl(TipsQueryService):
    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id_: str) -> Optional[TipsReadModel]:
        result = self.session.get(Task, id_)

        if result is None:
            return None

        return result.to_read_model()

    def findall(self) -> Sequence[TipsReadModel]:
        statement = select(Tip)
        result = self.session.execute(statement).scalars().all()

        if len(result) == 0:
            return []

        return [tips.to_read_model() for tips in result]
