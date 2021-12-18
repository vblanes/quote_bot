from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id_ = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    telegram_id = Column(Integer, nullable=True)


class Quote(Base):
    __tablename__ = 'quote'

    id_ = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey('user.id_'))
    conversation_id = Column(ForeignKey('conversation.id_'))
    quote_text = Column(String, nullable=False)

class Conversation(Base):
    __tablename__ = 'conversation'

    id_ = Column(Integer(), primary_key=True, autoincrement=True)
    date_ = Column(Date, nullable=True)
    context = Column(String, nullable=True)