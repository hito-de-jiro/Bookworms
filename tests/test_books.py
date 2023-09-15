import json
from functools import partial

import pytest

from bookworm.models.models import Book
from tests.conftest import update_database
from tests.test_authors import update_authors

update_books = partial(update_database, model=Book)


@pytest.fixture
def init_authors():
    authors = [
        {"borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"},
        {"borne": "1802-02-26", "first_name": "Victor", "id": 2, "last_name": "Hugo"},
        {"borne": "1564-04-26", "first_name": "William", "id": 3, "last_name": "Shakespeare"},
    ]
    update_authors(data=authors)


def test_read_all_books(client, init_database, init_authors):
    """test reading all authors"""
    # Prepare
    expected_json = [
        {"id": 1, "title": "Ballade des pendus", "text": "Frères humains, qui ...", "genre": "Balada", "author_id": 1},
        {"id": 2, "title": "Some title", "text": "Some text", "genre": "Drama", "author_id": 2},
        {"id": 3, "title": "Some title again", "text": "Very interesting text", "genre": "Adventures", "author_id": 3},
    ]

    update_books(data=expected_json)

    # Do work
    response = client.get('/api/v1/books')

    # Validate
    assert response.status_code == 200
    assert response.json == expected_json


def test_read_one_book(client, init_database, init_authors):
    """test reading one book"""
    # Prepare
    expected_json = [
        {
            "id": 1,
            "title": "Ballade des pendus",
            "text": "Frères humains, qui ...",
            "genre": "Balada",
            "author_id": 1
        },
    ]
    update_books(data=expected_json)

    # Do work
    response = client.get('api/v1/books/1')

    # Validate
    assert response.status_code == 200
    assert response.json == expected_json[0]


def test_read_one_wrong_book(client, init_database, init_authors):
    """test reading wrong book"""
    # Do work
    response = client.get('api/v1/books/1')

    # Validate
    assert response.status_code == 404
    assert "Book with ID:1 does not exists" in response.text


def test_add_new_book(client, init_database, init_authors):
    """test create a new book"""
    # Prepare
    new_book = [
        {
            "id": 4,
            "title": "Very MEGA important book",
            "text": "Very MEGA interesting text",
            "genre": "Pro zaek",
            "author_id": 1
        },
    ]

    # Do work
    response = client.post('/api/v1/books', json=new_book[0])

    # Validate
    assert response.status_code == 201
    assert json.loads(response.data) == new_book[0]


def test_add_existing_book(client, init_database, init_authors):
    """test create an existing book"""
    # Prepare
    book = [
        {
            "id": 1,
            "title": "Ballade des pendus",
            "text": "Frères humains, qui ...",
            "genre": "Balada",
            "author_id": 1
        },
    ]
    update_books(data=book)

    # Do work
    response = client.post('/api/v1/books', json=book[0])

    # Validate
    assert response.status_code == 406
    assert "Author with ID: 1 added this book" in response.text


def test_update_book(client, init_database, init_authors):
    """test update an existing book"""
    # Prepare
    book = [
        {
            "id": 1,
            "title": "Ballade des pendus",
            "text": "Frères humains, qui ...",
            "genre": "Balada",
            "author_id": 1
        },
    ]
    update_books(data=book)
    update_book = [
        {
            "id": 1,
            "title": "Some title",
            "text": "Some text",
            "genre": "Some genre",
            "author_id": 1
        },
    ]

    # Do work
    response = client.put('/api/v1/books/1', json=update_book[0])

    # Validate
    assert response.status_code == 201
    assert json.loads(response.data) == update_book[0]


def test_update_wrong_book(client, init_database, init_authors):
    """test update a wrong book"""
    # Prepare
    update_book = [
        {
            "id": 1,
            "title": "Some title",
            "text": "Some text",
            "genre": "Some genre",
            "author_id": 1
        },
    ]

    # Do work
    response = client.put('/api/v1/books/1', json=update_book[0])

    # Validate
    assert response.status_code == 404
    assert "Note with ID 1 not found" in response.text


def test_delete_book(client, init_database, init_authors):
    """test delete an exist author"""
    # Prepare
    book = [
        {
            "id": 1,
            "title": "Ballade des pendus",
            "text": "Frères humains, qui ...",
            "genre": "Balada",
            "author_id": 1
        },
    ]
    update_books(data=book)

    # Do work
    response = client.delete('/api/v1/books/1')

    # Validate
    assert response.status_code == 200
    assert "Book with ID:1 successfully deleted" in response.text


def test_delete_wrong_book(client, init_database, init_authors):
    """test delete a non-exist book"""
    # Do work
    response = client.delete('/api/v1/books/1')

    # Validate
    assert response.status_code == 404
    assert "Book with ID:1 not found" in response.text
