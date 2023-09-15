import pytest

from bookworm.app import create_app
from bookworm.config import TestingConfig
from bookworm.models.models import db


@pytest.fixture
def client():
    app = create_app(config=TestingConfig)
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture
def init_database(client):
    db.create_all()

    yield db

    db.session.remove()
    db.drop_all()


def update_database(model, data):
    prepared_models = [model(**row) for row in data]

    db.session.add_all(prepared_models)
    db.session.commit()
