import json

import pytest


@pytest.mark.skipif
def test_hello_route(client):
    """test root route"""

    # Do work
    response = client.get('/')

    # Validate
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello, Dude!'


@pytest.mark.skipif
def test_read_all_authors(client, init_database):
    """test reading all authors"""

    # Prepare
    expected_json = [
        {"borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"},
        {"borne": "1802-02-26", "first_name": "Victor", "id": 2, "last_name": "Hugo"},
        {"borne": "1564-04-26", "first_name": "William", "id": 3, "last_name": "Shakespeare"},
    ]

    # Do work
    response = client.get('api/v1/authors')

    # Validate
    assert response.status_code == 200
    assert response.json == expected_json


@pytest.mark.skipif
def test_read_one_author(client, init_database):
    """test reading one author"""
    # Prepare
    expected_json = {"borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"}

    # Do work
    response = client.get('api/v1/authors/1')

    # Validate
    assert response.status_code == 200
    assert response.json == expected_json


@pytest.mark.skipif
def test_add_new_author(client, init_database):
    """test create a new author"""
    # Prepare
    new_author = {"borne": "1992-09-18", "first_name": "Jora", "id": 4, "last_name": "Mendel"}

    # Do work
    response = client.post("/api/v1/authors", json=new_author)

    # Validate
    assert response.status_code == 201
    assert json.loads(response.data) == new_author


@pytest.mark.skipif
def test_add_existing_author(client, init_database):
    """test create an existing author"""
    # Prepare
    author = {"borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"}

    # Do work
    response = client.post('/api/v1/authors', json=author)

    # Validate
    assert response.status_code == 406
    assert b"Author id:1 already exists" in response.data


@pytest.mark.skipif
def test_update_author(client, init_database):
    """test update an existing author"""
    # Prepare
    update_author = {"borne": "1041-07-27", "first_name": "Edward", "id": 1, "last_name": "de Bullon"}

    # Do work
    response = client.put('/api/v1/authors/1', json=update_author)

    # Validate
    assert response.status_code == 201
    assert json.loads(response.data) == update_author


@pytest.mark.skipif
def test_update_wrong_author(client, init_database):
    """test delete an non-exist author"""
    # Do work
    response = client.delete('/api/v1/authors/111')

    # Validate
    assert response.status_code == 404
    assert b"Author id:111 not found" in response.data


@pytest.mark.skipif
def test_delete_author(client, init_database):
    """test delete an exist author"""
    # Do work
    response = client.delete('/api/v1/authors/1')

    # Validate
    assert response.status_code == 200
    assert b"Author id:1 successfully deleted" in response.data


@pytest.mark.skipif
def test_delete_wrong_author(client, init_database):
    """test delete an non-exist author"""
    # Do work
    response = client.delete('/api/v1/authors/111')

    # Validate
    assert response.status_code == 404
    assert b"Author id:111 not found" in response.data


@pytest.mark.skipif
def test_search(client, init_database):
    """test searching"""
    # Prepare
    searched = 'vi'
    expected_json = [
        {"borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"},
        {"borne": "1802-02-26", "first_name": "Victor", "id": 2, "last_name": "Hugo"},
    ]

    # Do work
    response = client.get(f'/api/v1/authors/search?q={searched}&?page=2')

    # Validate
    assert response.status_code == 200
    assert response.json == expected_json


@pytest.mark.skipif
def test_wrong_search(client, init_database):
    """test wrong search"""
    # Prepare
    searched = 'zz'
    # Do work
    response = client.get(f'/api/v1/authors/search?q={searched}&?page=2')
    assert response.status_code == 404
    assert b"Information not found" in response.data
