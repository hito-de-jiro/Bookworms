def test_add_new_author(client, init_database):
    path = "api/v1/authors"
    response = client.post(path,
                           json={
                               "first_name": "Alexandre",
                               "last_name": "Dumas",
                               "dob": "1802-07-24",
                               "books": []
                           })

    assert response.status_code == 200
    assert b'{"firs_name": "Alexander", "last_name": "Dumas", "dob": "1823-01-14"}' in response.data


def test_get_all_authors(client, init_database):
    path = "api/v1/authors"
    response = client.get(path)

    assert b'[{}]' in response.data
