import pytest

from bookworm import config
from bookworm.app import create_app
from bookworm.models.models import Author, db


@pytest.fixture
def client():
    app = create_app()
    app.config.from_object(config.TestingConfig)
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture
def init_database():
    db.create_all()

    test_authors = [
        {"id": 1, "first_name": "Francois", "last_name": "Villon", "borne": "1431-04-01", "books": []},
        {"id": 2, "first_name": "Victor", "last_name": "Hugo", "borne": "1802-02-26", "books": []},
        {"id": 3, "first_name": "William", "last_name": "Shakespeare", "borne": "1564-04-26", "books": []},
    ]

    def create_author_model(author):
        return Author(**author)

    mapped_authors = map(create_author_model, test_authors)
    t_authors = list(mapped_authors)

    db.session.add_all(t_authors)
    db.session.commit()

    yield db

    db.session.remove()
    db.drop_all()
