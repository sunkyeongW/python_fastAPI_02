import email
from email.policy import default
from enum import unique
from lib2to3.pgen2.token import STRING
from sqlalchemy import Boolean, Column, Integer, String
from app.database import Base

class User(Base):     #dayabase.py에 있는 부모클래스
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)