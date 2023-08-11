import json

import pytest


@pytest.mark.skipif
def test_read_all_authors(client, init_database):
    """test reading all authors"""
    response = client.get('api/v1/authors')
    assert response.status_code == 200

    expected_data = [
        {"books": [], "borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"},
        {"books": [], "borne": "1802-02-26", "first_name": "Victor", "id": 2, "last_name": "Hugo"},
        {"books": [], "borne": "1564-04-26", "first_name": "William", "id": 3, "last_name": "Shakespeare"},
    ]
    print(response.json)
    assert response.json == expected_data


@pytest.mark.skipif
def test_read_one_author(client, init_database):
    """test reading one author"""
    response = client.get('api/v1/authors/1')
    assert response.status_code == 200

    expected_data = {"books": [], "borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"}

    print(response.json)
    assert response.json == expected_data


@pytest.mark.skipif
def test_add_new_author(client, init_database):
    """test create a new author"""
    new_author = {"books": [], "borne": "1992-09-18", "first_name": "Jora", "id": 4, "last_name": "Mendel"}

    response = client.post('/api/v1/authors', json=new_author)

    assert response.status_code == 201
    assert json.loads(response.data) == new_author


@pytest.mark.skipif
def test_create_existing_author(client, init_database):
    """test create an existing author"""
    author = {"books": [], "borne": "1431-04-01", "first_name": "Francois", "id": 1, "last_name": "Villon"}

    response = client.post('/api/v1/authors', json=author)
    assert response.status_code == 406
    assert b"Person with that data 1 already exists" in response.data
