import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_factorial_of_five(client):
    response = client.get("/factorial?number=5")
    assert response.status_code == 200
    assert response.get_json() == {"number": 5, "factorial": 120}


def test_factorial_of_zero(client):
    response = client.get("/factorial?number=0")
    assert response.status_code == 200
    assert response.get_json()["factorial"] == 1


def test_missing_parameter(client):
    response = client.get("/factorial")
    assert response.status_code == 400
    assert "error" in response.get_json()


@pytest.mark.parametrize("value", ["abc", "3.5", ""])
def test_not_an_integer(client, value):
    response = client.get(f"/factorial?number={value}")
    assert response.status_code == 400


def test_negative_number(client):
    response = client.get("/factorial?number=-3")
    assert response.status_code == 400


def test_too_large_number(client):
    response = client.get("/factorial?number=1001")
    assert response.status_code == 400