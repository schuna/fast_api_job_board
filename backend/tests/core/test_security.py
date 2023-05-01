from core.security import create_access_token


def test_create_access_token():
    data = {"sub": "abc@email.com"}
    token = create_access_token(data)
    print(token)