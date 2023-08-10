import pytest

from bookworm import config
from bookworm.app import create_app
from bookworm.config import db
from bookworm.models.models import Author, Book


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
        {"first_name": "Francois ", "last_name": "Villon", "borne": "1431-04-01", "books": []},
        {"first_name": "Victor", "last_name": "Hugo", "borne": "1802-02-26", "books": []},
        {"first_name": "William", "last_name": "Shakespeare", "borne": "1564-04-26", "books": []},
    ]

    test_book = [
        {
            "title": "Test title",
            "text": "Test text",
            "genre": "Test genre",
        }
    ]

    def create_author_model(author):
        return Author(**author)

    def create_book_model(book):
        return Book(**book)

    mapped_authors = map(create_author_model, test_authors)
    t_authors = list(mapped_authors)

    mapped_books = map(create_book_model, test_book)
    t_book = list(mapped_books)

    db.session.add_all(t_authors)
    db.session.add_all(t_book)
    db.session.commit()

    yield db

    db.session.remove()
    db.drop_all()


@pytest.fixture
def test_database():
    """fixture for cleaning and leveraging test db"""

    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()
