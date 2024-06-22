from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from api.features.tips.data.models.tips import Tips
from api.features.tips.domain.entities.tips_query_model import TipsReadModel


class TipsQueryServiceImpl():
    def __init__(self, session: Session):
        self.session: Session = session

    def find_all(self) -> Sequence[TipsReadModel]:
        statement = select(Tips)
