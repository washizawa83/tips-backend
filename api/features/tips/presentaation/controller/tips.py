from typing import List
from fastapi import APIRouter, Depends, status, HTTPException

from api.features.tips.domain.entities.tips_query_model import TipsReadModel
from api.features.tips.domain.usecase.get_tips import GetTipsUseCase
from api.features.tips.dependencies import get_tips_use_case

router = APIRouter()


@router.get('/tips', response_model=List[TipsReadModel])
def list_tips(
    get_tips_use_case: GetTipsUseCase = Depends(get_tips_use_case)
):
    try:
        tips = get_tips_use_case(None)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if not tips:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return tips


@router.post('/tips')
def create_tips():
    pass


@router.put('/tips{tips_id}')
def update_tips():
    pass


@router.delete('/tips/{tips_id}')
def delete_tips():
    pass


@router.put('/tips/{tips_id}')
def update_tips_good():
    pass
