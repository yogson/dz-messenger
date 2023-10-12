from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from db import async_session
from db.models import UserDB
from models.users import User, UserCreate

root_router = APIRouter()

@root_router.post("/users/", response_model=User)
async def create_user(user: UserCreate, db: AsyncSession = Depends(async_session)):
    db_user = UserDB(**user.model_dump())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


@root_router.get("/users/", response_model=List[User])
async def list_users(offset: int = 0, limit: int = 10, db: AsyncSession = Depends(async_session)):
    stmt = select(UserDB).offset(offset).limit(limit)
    users = (await db.execute(stmt)).scalars().all()
    return users


@root_router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(async_session)):
    stmt = select(UserDB).where(UserDB.id == user_id)
    user = (await db.execute(stmt)).scalar()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@root_router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate, db: AsyncSession = Depends(async_session)):
    stmt = select(UserDB).where(UserDB.id == user_id)
    existing_user = (await db.execute(stmt)).scalar()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for field, value in user.dict().items():
        setattr(existing_user, field, value)
    await db.commit()
    await db.refresh(existing_user)
    return existing_user


@root_router.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int, db: AsyncSession = Depends(async_session)):
    stmt = select(UserDB).where(UserDB.id == user_id)
    existing_user = (await db.execute(stmt)).scalar()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await db.delete(existing_user)
    await db.commit()
    return existing_user

# Conversation handlers
# (Similar async handlers for Conversation and ConversationUsers)
