def test_add_new_author(client, init_database):
    path = "api/v1/authors"
    response = client.post(path,
                           json={
                               "id": 1,
                               "first_name": "Alexandre",
                               "last_name": "Dumas",
                               "borne": "1802-07-24",
                               "books": []
                           })

    assert response.status_code == 200
    # assert b'{"id": 5, "firs_name": "Alexander", "last_name": "Dumas", "borne": "1823-01-14"}' in response.data
    data = response.json()
    print(data)


def test_update_author():
    # TODO document why this method is empty
    pass


def test_get_all_authors(client, init_database):
    path = "api/v1/authors"
    response = client.get(path)

    assert b'[{}]' in response.data


def test_empty_db(client, init_database):
    rv = client.get('/')
    assert b'No entries here so far' in rv.data
