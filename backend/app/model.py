from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, Date, DateTime
from app.database import Base
from sqlalchemy import MetaData
from app.database import engine
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
    Column('uid', Integer, primary_key=True, autoincrement=True),
    Column('user_id', String(100), unique=True, nullable=False),
    Column('password', String(100), nullable=False),
    Column('username', String(100), nullable=False),
    Column('email', String(100), nullable=False),
    Column('auth', String(100), nullable=False),
    Column('createdAt', String(100), default=datetime.now())
)

class Category(Base):
    __tablename__ = 'tb_category'

    cid = Column('cid', Integer, primary_key=True, autoincrement=True)
    type = Column('category_nm', String(100), nullable=False)

category_table = Table(
    'tb_category', metadata,
    Column('cid', Integer, primary_key=True, autoincrement=True),
    Column('category_nm', String(100), nullable=True)
    # 카테고리 유형 : Q&A, 지식, 커뮤니티, notice
)

class Board(Base):
    __tablename__ = 'tb_board'

    bid = Column('bid', Integer, primary_key=True, autoincrement=True)
    category = Column('category', Integer, ForeignKey('tb_category.cid'))
    uid = Column('uid', Integer, ForeignKey('tb_user.uid'))
    title = Column('title', String(100), nullable=False)
    content = Column('content', String(4000), nullable=False)
    createdAt = Column('createdAt', DateTime, default=datetime.now())
    updatedAt = Column('updatedAt', DateTime, default=datetime.now())
    hit = Column('hit', Integer, default=0)
    imgurl = Column('imgPath', String(100))

board_table = Table(
    'tb_board',
    metadata,
    Column('bid', Integer, primary_key=True, autoincrement=True),
    Column('category', Integer, ForeignKey('tb_category.cid')),
    Column('uid', Integer, ForeignKey('tb_user.uid')),
    Column('title', String(100), nullable=False),
    Column('content', String(4000), nullable=False),
    Column('createdAt', DateTime, default=datetime.now()),
    Column('updatedAt', DateTime, default=datetime.now()),
    Column('hit', Integer, default=0),
    Column('imgPath', String(100))
)


class Reply(Base):
    __tablename__ = 'tb_reply'

    rid = Column('rid', Integer, primary_key=True, autoincrement=True)
    bid = Column('cid', Integer, ForeignKey('tb_board.bid'))
    uid = Column('uid', Integer, ForeignKey('tb_user.uid'))
    createdAt = Column('createdAt', DateTime, default=datetime.now())
    updatedAt = Column('updatedAt', DateTime, default=datetime.now())

reply_table = Table(
    'tb_reply',
    metadata,
    Column('rid', Integer, primary_key=True, autoincrement=True),
    Column('cid', Integer, ForeignKey('tb_board.bid')),
    Column('uid', Integer, ForeignKey('tb_user.uid')),
    Column('createdAt', DateTime, default=datetime.now()),
    Column('updatedAt', DateTime, default=datetime.now())
)


metadata.create_all(engine)