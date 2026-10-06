from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Payment application is running" in response.data


def test_version():
    client = app.test_client()
    response = client.get("/version")

    assert response.status_code == 200