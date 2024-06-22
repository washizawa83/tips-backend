from fastapi import Depends
from sqlalchemy.orm import Session

from api.features.tips.domain.services.tips_query_service import TipsQueryService
from api.features.tips.data.services.tips_query_service_impl import TipsQueryServiceImpl
from api.features.tips.domain.usecase.get_tips import GetTipsUseCase, GetTipsUseCaseImpl
from api.core.database.mysql.database import get_session


def get_tips_query_service(
    session: Session = Depends(get_session)
) -> TipsQueryService:
    return TipsQueryServiceImpl(session)


def get_tips_use_case(
    tips_query_service: TipsQueryService = Depends(get_tips_query_service)
) -> GetTipsUseCase:
    return GetTipsUseCaseImpl(tips_query_service)
