

from lib2to3.pytree import Base
from operator import index
from turtle import title
from sqlalchemy import Column, Integer, String
from .database import Base




class Blog(Base):
    __tablename__ = 'blog_users'
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String)
    body = Column(String)
   