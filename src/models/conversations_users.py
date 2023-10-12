from pydantic import BaseModel


class ConversationUsersBase(BaseModel):
    conversation_id: int
    user_id: int


class ConversationUsersCreate(ConversationUsersBase):
    pass


class ConversationUsers(ConversationUsersBase):
    id: int

    class Config:
        orm_mode = True
