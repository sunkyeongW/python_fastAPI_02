from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://admin:1234@localhost:3306/dev") #함수를 이용해 DB 연결한 엔진 생성
SessionLocal = sessionmaker(  #SessionLocal: 함수를 이용해 세선 생성
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base() #declarative_base: 함수는 모델 정의를 위한 부모 클래스 생성