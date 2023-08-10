import json


def test_read_all_authors(client, init_database):
    """test reading all authors"""
    response = client.get('api/v1/authors')
    assert response.status_code == 200

    expected_data = [
        {"id": 1, "first_name": "Francois ", "last_name": "Villon", "borne": "1431-04-01", "books": []},
        {"id": 2, "first_name": "Victor", "last_name": "Hugo", "borne": "1802-02-26", "books": []},
        {"id": 3, "first_name": "William", "last_name": "Shakespeare", "borne": "1564-04-26", "books": []},
    ]
    assert response.json == expected_data


def test_add_new_author(client, init_database):
    """test create a new author"""
    new_author = {
        "books": [],
        "id": 4,
        "borne": "1992-09-18",
        "first_name": "Jora",
        "last_name": "Mendel"
    }

    response = client.post('/api/v1/authors', json=new_author)

    assert response.status_code == 201
    assert json.loads(response.data) == new_author
