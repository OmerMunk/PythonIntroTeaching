import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'message': 'Welcome to the Flask App!'}

def test_404(client):
    response = client.get('/shubulu')
    assert response.status_code == 404


def test_add(client):
    response = client.get('/add')
    assert response.status_code == 405
    # send a post request with {"a": 5, "b": 5}
    response = client.post('/add', json={"a": 5, "b": 5})
    assert response.status_code == 200
    response = client.post('/add', json={"a": 5})
    assert response.status_code == 400
    assert response.json == {'error': 'Missing parameters'}
    response = client.post('/add', json={"b": 5})
    assert response.status_code == 400
    assert response.json == {'error': 'Missing parameters'}
    response = client.post('/add', json={})
    assert response.status_code == 400
    assert response.json == {'error': 'Missing parameters'}


def test_get_user(client):
    response = client.get('/user/1')
    assert response.status_code == 200
    assert response.json == {'name': 'Alice', 'age': 30}
    response = client.get('/user/4')
    assert response.status_code == 404
    assert response.json == {'error': 'User not found'}