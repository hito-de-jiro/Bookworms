import pytest


@pytest.mark.unit
def test_create_author(client, init_database):
    # Prepare
    path = "api/v1/authors"
    fake_data = {
        "first_name": "Joanne",
        "last_name": "Rowling",
        "borne": "1965-07-31",
    }

    # Do work
    actual_response = client.post(path, json=fake_data)
    print()
    # Validate
    assert actual_response.status_code == 201
    assert b'{"first_name": "Joanne", "last_name": "Rowling", "borne": "1965-07-31"}' in actual_response.data


def test_fetch_author(client, init_database):
    path = "api/v1/authors/1"
    response = client.get(path)

    assert b'{"first_name": "John", "last_name": "Keats", "borne": "1795-10-31",}' in response.data


def test_fetch_authors(client, init_database):
    path = "api/v1/authors"
    response = client.get(path)
    assert b'{"first_name": "John", "last_name": "Keats", "borne": "1795-10-31", ' \
           b'{"first_name": "Victor", "last_name": "Hugo", "borne": "1802-02-26"}, ' \
           b'{"first_name": "William", "last_name": "Shakespeare", "borne": "1564-04-26"},' \
           in response.data
