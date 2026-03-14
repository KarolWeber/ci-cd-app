import pytest
from calculator import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.data.decode() == "5"

def test_sub(client):
    response = client.get("/sub?a=5&b=1")
    assert response.status_code == 200
    assert response.data.decode() == "4"
