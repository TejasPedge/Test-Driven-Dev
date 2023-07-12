import json
import pytest
from app import app, weather_data

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_weather_existing_city(client):
    response = client.get('/weather/San Francisco')
    assert response.status_code == 200
    assert response.json == weather_data['San Francisco']

def test_get_weather_nonexistent_city(client):
    response = client.get('/weather/Chicago')
    assert response.status_code == 404
    assert response.data == b'Weather data not found for Chicago'
