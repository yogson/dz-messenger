from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    nickname: str
    created_at: datetime
    last_seen: Optional[datetime]


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
