from abc import abstractmethod
from typing import Sequence

from api.core.use_case.use_case import BaseUseCase
from api.features.tips.domain.entities.tips_query_model import TipsReadModel
from api.features.tips.domain.services.tips_query_service import TipsQueryService


class GetTipsUseCase(BaseUseCase[None, Sequence[TipsReadModel]]):
    service: TipsQueryService

    @abstractmethod
    def __call__(self, args: None) -> Sequence[TipsReadModel]:
        raise NotImplementedError()


class GetTipsUseCaseImpl(GetTipsUseCase):
    def __init__(self, service: TipsQueryService):
        self.service: TipsQueryService = service

    def __call__(self, args: None) -> Sequence[TipsReadModel]:
        try:
            tips = self.service.findall()
        except Exception:
            raise

        return tips
