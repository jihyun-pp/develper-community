import contextlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
from os import environ

load_dotenv()

engine = create_engine(environ['MARIADB_CONN_URL'], echo=True)

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = SessionLocal.query_property()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()