from bookworm.app import create_app
from bookworm import config


def test_create_app():
    assert create_app()


def test_config():
    assert config.TestingConfig


def test_client(client):
    response = client.get('/')
    assert response.status_code == 200





