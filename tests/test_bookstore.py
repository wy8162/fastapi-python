import pytest
from fastapi.testclient import TestClient
from requests import Response
from bookstore.main import app


@pytest.fixture(scope="module", autouse=True)
def client():
    return TestClient(app)


def test_ping(client):
    response: Response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "ok"}
