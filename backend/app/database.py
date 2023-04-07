import contextlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
from os import environ

load_dotenv()

DATABASE = "mysql+pymysql://{}:{}@{}:{}/{}".format(
    environ['DB_USER'],
    environ['DB_PW'],
    environ['DB_HOST'],
    environ['DB_PORT'],
    environ['DB_NAME']
)

engine = create_engine(DATABASE, echo=True)

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()   # 실제 연결
Base.query = SessionLocal.query_property()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()