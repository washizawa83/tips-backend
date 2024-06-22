from typing import List
from fastapi import APIRouter, Depends

import api.schemas.tips as tips_schema
from api.features.tips.domain.usecase.get_tips import GetTipsUseCase
from api.features.tips.dependencies import get_tips_use_case

router = APIRouter()


@router.get('/tips', response_model=List[tips_schema.Tips])
async def list_tips(
    get_tips_use_case: GetTipsUseCase = Depends(get_tips_use_case)
):
    return [
        tips_schema.Tips(
            id='test-id',
            user_id='test-user-id',
            text='test-text',
            tags=['python', 'fastAPI'],
            good=8,
            updated_at='2024/06/22',
            created_at='2024/06/20'
        )
    ]


@router.post('/tips')
async def create_tips():
    pass


@router.put('/tips{tips_id}')
async def update_tips():
    pass


@router.delete('/tips/{tips_id}')
async def delete_tips():
    pass


@router.put('/tips/{tips_id}')
async def update_tips_good():
    pass
