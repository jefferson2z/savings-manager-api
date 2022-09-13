import pytest
from fastapi.testclient import TestClient


import os

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
os.environ["DATABASE_URL"] = SQLALCHEMY_DATABASE_URL


from app.main import app
from app.db.database import engine
from app.db.init_db import init_db


@pytest.fixture()
def client():
    init_db(engine)
    yield TestClient(app)
    if os.path.exists("test.db"):
        os.remove("test.db")


@pytest.fixture()
def jwt(client):
    client.post("/users/", json={"username": "Ikari", "password": "safe password"})
    response_token = client.post(
        "/token", data={"username": "Ikari", "password": "safe password"}
    )
    response_token_json = response_token.json()
    access_token = response_token_json["access_token"]
    yield access_token
