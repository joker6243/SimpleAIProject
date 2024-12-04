from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils.database import get_db
from app.services.user_service import get_user_by_id, create_user

router = APIRouter()


@router.post("/users/")
async def create_user_route(name: str, email: str, 
                            db: AsyncSession = Depends(get_db)):
    return await create_user(db, name, email)


@router.get("/users/{user_id}")
async def get_user_route(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
