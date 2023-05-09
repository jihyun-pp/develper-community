from fastapi.testclient import TestClient
import pytest
import json
from httpx import AsyncClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Test! Hello!"}

@pytest.mark.asyncio
async def test_root():
    # 비동기 테스트
    async with AsyncClient(base_url="http://127.0.0.1:9000") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}
