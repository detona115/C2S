import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import init_db
from app.seed import seed_db


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    init_db()

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    init_db()
    seed_db(10)

client = TestClient(app)

def test_mcp_query_empty():
    response = client.post("/mcp/query", json={})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_mcp_query_filter():
    response = client.post("/mcp/query", json={"marca": "Fiat"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert data[0]["marca"] == "Fiat"
