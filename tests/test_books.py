import json

import pytest


# @pytest.mark.skipif
def test_books_route(client, init_database):
    """test reading all authors"""
    # Prepare
    expected_json = [
        {"id": 1, "title": "Ballade des pendus", "text": "Frères humains, qui ...", "genre": "Balada", "author_id": 1},
        {"id": 2, "title": "Some title", "text": "Some text", "genre": "Drama", "author_id": 2},
        {"id": 3, "title": "Some title again", "text": "Very interesting text", "genre": "Adventures", "author_id": 3},
    ]

    # Do work
    response = client.get('/api/v1/books')

    # Validate
    assert response.status_code == 200
    assert response.json == expected_json


# @pytest.mark.skipif
def test_read_one_book(client, init_database):
    """test reading one book"""
    # Prepare
    expected_json = {"id": 1,
                     "title": "Ballade des pendus",
                     "text": "Frères humains, qui ...",
                     "genre": "Balada",
                     "author_id": 1}

    # Do work
    response = client.get('api/v1/books/1')

    # Validate
    assert response.status_code == 200
    assert response.json == expected_json


# @pytest.mark.skipif
def test_read_one_wrong_book(client, init_database):
    """test reading wrong book"""
    # Do work
    response = client.get('api/v1/books/111')

    # Validate
    assert response.status_code == 404
    assert b"Book with ID 111 not found" in response.data


# @pytest.mark.skipif
def test_add_new_book(client, init_database):
    """test create a new book"""
    # Prepare
    new_book = {"id": 3,
                "title": "Very MEGA important book",
                "text": "Very MEGA interesting text",
                "genre": "Pro zaek",
                "author_id": 3}

    # Do work
    response = client.post("/api/v1/books", json=new_book)

    # Validate
    assert response.status_code == 201
    assert json.loads(response.data) == new_book
