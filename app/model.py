from sqlalchemy import *
from sqlalchemy.orm import relationship
from app.database import Base
from app.database import engine
from datetime import datetime

metadata = MetaData()  # 테이블의 메타 정보 담을 객체

class User(Base):
    __tablename__ = 'tb_users'

    uid = Column('uid', BIGINT, primary_key=True, autoincrement=True)
    email = Column('email', String(100), unique=True, nullable=False)
    password = Column('password', String(100))
    nickname = Column('nickname', String(100))
    birth = Column('birth', BIGINT)
    auth = Column('auth', String(100))
    createdAt = Column('createdAt', DateTime, default=datetime.now())
    updatedAt = Column('updatedAt', DateTime, default=datetime.now())

users_table = Table(
    'tb_users',
    metadata,
    Column('uid', BIGINT, primary_key=True, autoincrement=True),
    Column('email', String(100), unique=True, nullable=False),
    Column('password', String(100)),
    Column('nickname', String(100)),
    Column('birth', BIGINT),
    Column('auth', String(100)),
    Column('createdAt', DateTime, default=datetime.now()),
    Column('updatedAt', DateTime, default=datetime.now())
)

# metadata.create_all(engine)