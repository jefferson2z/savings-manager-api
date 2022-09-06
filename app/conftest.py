import pytest
from fastapi.testclient import TestClient


import os

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
os.environ["DATABASE_URL"] = SQLALCHEMY_DATABASE_URL


from app.main import app


@pytest.fixture()
def client():
    yield TestClient(app)
    if os.path.exists("test.db"):
        os.remove("test.db")
