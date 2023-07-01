import pytest
from bookworm import config

from bookworm.config import db
from bookworm.app import app
from bookworm.models import Author


@pytest.fixture
def client():
    app.config.from_object(config.TestingConfig)
    with app.test_client():
        with app.app_context():
            yield client


@pytest.fixture
def init_database():
    db.create_all()

    test_authors = [
        {"first_name": "Francois ", "last_name": "Villon", "dob": "1431-04-01", "books": []},
        {"first_name": "Victor", "last_name": "Hugo", "dob": "1802-02-26", "books": []},
        {"first_name": "William", "last_name": "Shakespeare", "dob": "1564-04-26", "books": []},
    ]

    def create_post_model(author):
        return Author(**author)

    mapped_authors = map(create_post_model, test_authors)
    t_authors = list(mapped_authors)

    db.session.add_all(t_authors)
    db.session.commit()

    yield db

    db.session.remove()
    db.drop_all()
