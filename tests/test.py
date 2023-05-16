from fastapi.testclient import TestClient
import pytest
import json
from httpx import AsyncClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_new_user():
    async with AsyncClient(base_url="http://127.0.0.1:9000") as ac:
        response = await ac.post(
            "/users/new",
            content=json.dumps(
                {
                    "email": "user1@example.com",
                    "password": "1234",
                    "password_confirm": "1234",
                    "nickname": "user1",
                    "birth": 1998
                }
            ),
        )
        assert response.status_code != 200
        assert response.json() == {
            "id": "foobar",
            "title": "Foo Bar",
            "description": "The Foo Barters",
        }
