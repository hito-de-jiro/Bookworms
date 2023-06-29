def test_add_new_author(client, init_database):
    path = "api/v1/author"
    responce = client.post(path,
                           json={
                               "firs_name": "Alexander",
                               "last_name": "Dumas",
                               "dob": "1823-01-14"
                           })

    assert responce.status_code == 200
    assert b'{"firs_name": "Alexander", "last_name": "Dumas", "dob": "1823-01-14"}' in responce.data