from typing import Generator
import pytest
from fastapi.testclient import TestClient

from app.database import get_db
from app.main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    db = get_db()
    yield db


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c