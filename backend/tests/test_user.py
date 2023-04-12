import unittest
import pytest
from starlette.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.asyncio import AsyncSession
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

@pytest.fixture(scope="session")
def test_db_session():
    session = AsyncSession(bind=engine)
    try: yield session
    finally: session.close()


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()


if __name__ == "__main__":
    unittest.main()