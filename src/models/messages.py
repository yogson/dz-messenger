from pydantic import BaseModel
from datetime import datetime


class MessageBase(BaseModel):
    conversation_id: int
    sender_id: int
    content: str
    sent_at: datetime


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: int

    class Config:
        orm_mode = True
