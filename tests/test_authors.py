import json
from functools import partial

from bookworm.models.models import Author
from tests.conftest import update_database

update_authors = partial(update_database, model=Author)


def test_hello_route(client):
    """test root route"""

    # Do work
    response = client.get('/')

    # Validate
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello, Dude!'


def test_read_all_authors(client, init_database):
    """test reading all authors"""

    # Prepare
    expected_json = [
        {"borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"},
        {"borne": "1802-02-26", "first_name": "Victor", "id": 2, "last_name": "Hugo"},
        {"borne": "1564-04-26", "first_name": "William", "id": 3, "last_name": "Shakespeare"},
    ]
    update_authors(data=expected_json)

    # Do work
    response = client.get('api/v1/authors')

    # Validate
    assert response.status_code == 200
    assert response.json == expected_json


def test_read_one_author(client, init_database):
    """test reading one author"""
    # Prepare
    expected_json = [
        {"borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"},
    ]
    update_authors(data=expected_json)

    # Do work
    response = client.get('api/v1/authors/1')

    # Validate
    assert response.status_code == 200
    assert response.json == expected_json[0]


def test_add_new_author(client, init_database):
    """test create a new author"""
    # Prepare
    new_author = {"borne": "1992-09-18", "first_name": "Jora", "id": 4, "last_name": "Mendel"}

    # Do work
    response = client.post("/api/v1/authors", json=new_author)

    expected_json = client.get("/api/v1/authors/4")

    # Validate
    assert response.status_code == 201
    assert json.loads(response.text) == new_author

    assert expected_json.json == new_author


def test_add_existing_author(client, init_database):
    """test create an existing author"""
    # Prepare
    author = [
        {"borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"},
    ]
    update_authors(data=author)

    # Do work
    response = client.post('/api/v1/authors', json=author[0])

    # Validate
    assert response.status_code == 409
    assert "Conflict. Author with ID:1 already exists" in response.text


def test_update_author(client, init_database):
    """test update an existing author"""
    # Prepare
    author = [
        {"borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"},
    ]
    update_authors(data=author)
    update_author = {"borne": "1041-07-27", "first_name": "Edward", "id": 1, "last_name": "de Bullon"}

    # Do work
    response = client.put('/api/v1/authors/1', json=update_author)
    updated_author = client.get('/api/v1/authors/1')

    # Validate
    assert response.status_code == 200
    assert json.loads(response.text) == update_author
    assert updated_author.json == update_author


def test_update_wrong_author(client, init_database):
    """test delete an non-exist author"""
    # Prepare
    update_author = {"borne": "1041-07-27", "first_name": "Edward", "id": 1, "last_name": "de Bullon"}

    # Do work
    response = client.put('/api/v1/authors/1', json=update_author)

    # Validate
    assert response.status_code == 404
    assert "Author with ID:1 not found" in response.text


def test_delete_author(client, init_database):
    """test delete an exist author"""
    # Prepare
    author = [
        {"borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"},
    ]
    update_authors(data=author)
    # Do work
    response = client.delete('/api/v1/authors/1')

    # Validate
    assert response.status_code == 200
    assert "Author with ID:1 successfully deleted" in response.text

    response = client.get('/api/v1/authors/1')

    assert response.status_code == 404
    assert "Author with ID:1 does not exists" in response.text


def test_delete_wrong_author(client, init_database):
    """test delete an non-exist author"""
    # Do work
    response = client.delete('/api/v1/authors/1')

    # Validate
    assert response.status_code == 404
    assert "Author with ID:1 not found" in response.text


def test_search(client, init_database):
    """test searching"""
    # Prepare
    firstname = "Francois"
    lastname = "Villon"

    expected_json = [
        {"borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"},
    ]
    update_authors(data=expected_json)

    # Do work
    response = client.get(f'api/v1/authors/search?firstname={firstname}&lastname={lastname}')

    # Validate
    assert response.status_code == 200
    assert response.json == expected_json


def test_wrong_search(client, init_database):
    """test wrong search"""
    # Prepare
    firstname = 'Isaak'
    lastname = 'Kaz'

    # Do work
    response = client.get(f'/api/v1/authors/search?firstname={firstname}&lastname={lastname}')

    # Validate
    assert response.status_code == 404
    assert "Information not found" in response.text


def test_pagination(client, init_database):
    """test pagination"""
    # Prepare
    firstname = 'Victor'
    lastname = ''

    authors = [
        {"borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"},
        {"borne": "1802-02-26", "first_name": "Victor", "id": 2, "last_name": "Hugo"},
        {"borne": "1564-04-26", "first_name": "William", "id": 3, "last_name": "Shakespeare"},
        {"borne": "1872-12-06", "first_name": "Victor", "id": 4, "last_name": "Brumental"},
        {"borne": "1764-05-11", "first_name": "George", "id": 5, "last_name": "Pompidu"},
    ]
    update_authors(data=authors)

    # Do work
    response_page_1 = client.get(f'/api/v1/authors/search?firstname={firstname}&lastname={lastname}&page=1&per_page=1')
    response_page_2 = client.get(f'/api/v1/authors/search?firstname={firstname}&lastname={lastname}&page=2&per_page=1')

    # Validate
    assert response_page_1.status_code == 200
    assert len(json.loads(response_page_1.data)) == 1
    assert response_page_2.status_code == 200
    assert len(json.loads(response_page_2.data)) == 1
