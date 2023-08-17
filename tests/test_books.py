import json


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


def test_read_one_wrong_book(client, init_database):
    """test reading wrong book"""
    # Do work
    response = client.get('api/v1/books/111')

    # Validate
    assert response.status_code == 404
    assert b"Book with ID 111 not found" in response.data


def test_add_new_book(client, init_database):
    """test create a new book"""
    # Prepare
    new_book = {"id": 4,
                "title": "Very MEGA important book",
                "text": "Very MEGA interesting text",
                "genre": "Pro zaek",
                "author_id": 1}

    # Do work
    response = client.post('/api/v1/books', json=new_book)

    # Validate
    assert response.status_code == 201
    assert json.loads(response.data) == new_book


def test_add_existing_book(client, init_database):
    """test create an existing book"""
    # Prepare
    book = {
        "id": 1,
        "title": "Ballade des pendus",
        "text": "Frères humains, qui ...",
        "genre": "Balada",
        "author_id": 1
    }

    # Do work
    response = client.post('/api/v1/books', json=book)

    # Validate
    assert response.status_code == 406
    assert b"Author with ID: 1 added this book" in response.data


def test_update_book(client, init_database):
    """test update an existing book"""
    # Prepare
    update_book = {
        "id": 1,
        "title": "Some title",
        "text": "Some text",
        "genre": "Some genre",
        "author_id": 1
    }

    # Do work
    response = client.put('/api/v1/books/1', json=update_book)

    # Validate
    assert response.status_code == 201
    assert json.loads(response.data) == update_book


def test_update_wrong_book(client, init_database):
    """test update a wrong book"""
    # Prepare
    update_book = {
        "id": 1,
        "title": "Some title",
        "text": "Some text",
        "genre": "Some genre",
        "author_id": 1
    }

    # Do work
    response = client.put('/api/v1/books/11', json=update_book)

    # Validate
    assert response.status_code == 404
    assert b"Note with ID 11 not found" in response.data


def test_delete_book(client, init_database):
    """test delete an exist author"""
    # Do work
    response = client.delete('/api/v1/books/1')

    # Validate
    assert response.status_code == 200
    assert b"Book with ID:1 successfully deleted" in response.data


def test_delete_wrong_book(client, init_database):
    """test delete a non-exist book"""
    # Do work
    response = client.delete('/api/v1/books/11')

    # Validate
    assert response.status_code == 404
    assert b"Book with ID:11 not found" in response.data
