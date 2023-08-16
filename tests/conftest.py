import pytest

from bookworm.app import create_app
from bookworm.config import TestingConfig
from bookworm.models.models import Author, Book, db


@pytest.fixture
def client():
    app = create_app(config=TestingConfig)
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture
def init_database(client):
    db.create_all()

    test_authors = [
        {"id": 1, "first_name": "Francois", "last_name": "Villon", "borne": "1431-04-01"},
        {"id": 2, "first_name": "Victor", "last_name": "Hugo", "borne": "1802-02-26"},
        {"id": 3, "first_name": "William", "last_name": "Shakespeare", "borne": "1564-04-26"},
    ]

    test_books = [
        {"id": 1, "title": "Ballade des pendus", "text": "Frères humains, qui ...", "genre": "Balada", "author_id": 1},
        {"id": 2, "title": "Some title", "text": "Some text", "genre": "Drama", "author_id": 2},
        {"id": 3, "title": "Some title again", "text": "Very interesting text", "genre": "Adventures", "author_id": 3},
    ]

    def create_author_model(author):
        return Author(**author)

    def create_book_model(book):
        return Book(**book)

    mapped_authors = map(create_author_model, test_authors)
    t_authors = list(mapped_authors)

    mapped_books = map(create_book_model, test_books)
    t_books = list(mapped_books)

    db.session.add_all(t_authors)
    db.session.add_all(t_books)
    db.session.commit()

    yield db

    db.session.remove()
    db.drop_all()
