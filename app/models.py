from .database import Base
from sqlalchemy import Column,Integer,String,Boolean,TIMESTAMP, text,ForeignKey
from sqlalchemy.orm import Relationship

class Post(Base):
    __tablename__ = "newpost"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    contant = Column(String,nullable=False)
    published = Column(Boolean,server_default='TRUE',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)

    owner = Relationship("User")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    phone_NO = Column(String,nullable=False)

class Vote(Base):

    __tablename__ = "vote"

    post_id = Column(Integer,ForeignKey("newpost.id",ondelete="CASCADE"),primary_key=True)
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)