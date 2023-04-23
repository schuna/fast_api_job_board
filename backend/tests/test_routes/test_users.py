import json


def test_user_create(client):
    data = {"username": "test_user", "email": "abc@test.com", "password": "1234"}
    # noinspection PyTypeChecker
    response = client.post("/user/", data=json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "abc@test.com"
