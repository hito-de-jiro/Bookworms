import pytest
import config
from api.models import Author

from api.app import app
from config import db


@pytest.fixture
def client():
    app.config.from_object(config.TestingConfig)
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture
def init_database():
    """Create database and table"""
    db.create_all()

    test_authors = [
        {"first_name": "John", "last_name": "Keats", "borne": "1795-10-31", "books": []},
        {"first_name": "Victor", "last_name": "Hugo", "borne": "1802-02-26", "books": []},
        {"first_name": "William", "last_name": "Shakespeare", "borne": "1564-04-26", "books": []},
    ]

    def create_post_model(author):
        return Author(**author)

    # convert the list dictionaries to a list of Authors objects
    mapped_authors = map(create_post_model, test_authors)
    t_authors = list(mapped_authors)

    # add authors to database
    db.session.add_all(t_authors)

    # commit changes
    db.session.commit()

    yield db
    db.session.remove()
    # drop database table
    db.drop_all()
