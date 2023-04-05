from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, Date, DateTime
from backend.app.database import Base
from sqlalchemy import MetaData
from backend.app.database import engine
from datetime import datetime

metadata = MetaData()  # 테이블의 메타 정보 담을 객체

class User(Base):
    __tablename__ = 'tb_user'

    uid = Column('uid', Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', String(100), unique=True, nullable=False)
    password = Column('password', String(100))
    username = Column('username', String(100))
    email = Column('email', String(100))
    auth = Column('auth', String(100))
    createdAt = Column('createdAt', DateTime, default=datetime.now())

user_table = Table(
    'tb_user',
    metadata,
    Column('uid', String(100), nullable=False),
    Column('user_id', String(100), unique=True, nullable=False),
    Column('password', String(100), nullable=False),
    Column('username', String(100), nullable=False),
    Column('email', String(100), nullable=False),
    Column('auth', String(100), nullable=False),
    Column('createdAt', String(100), default=datetime.now())
)

metadata.create_all(engine)