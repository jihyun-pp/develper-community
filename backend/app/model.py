from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, Date
from app.database import Base
from sqlalchemy import MetaData
from app.database import engine

metadata = MetaData()  # 테이블의 메타 정보 담을 객체

class User(Base):