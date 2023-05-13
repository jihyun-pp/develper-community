from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from os import environ

load_dotenv()
engine = create_engine(environ['DB_CONN_URL'], echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()