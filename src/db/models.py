from datetime import datetime

from sqlalchemy import UUID, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class UserDB(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    guid = Column(UUID, nullable=False)
    nickname = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    last_seen = Column(DateTime)


class ConversationDB(Base):
    __tablename__ = "Conversations"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class ConversationUsersDB(Base):
    __tablename__ = "Conversations_users"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("Conversations.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False)
