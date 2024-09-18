import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


    def test_create_todo(client):
        client.post('/todos/', json=)