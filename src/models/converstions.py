from pydantic import BaseModel
from datetime import datetime


class ConversationBase(BaseModel):
    created_at: datetime


class ConversationCreate(ConversationBase):
    pass


class Conversation(ConversationBase):
    id: int

    class Config:
        orm_mode = True
