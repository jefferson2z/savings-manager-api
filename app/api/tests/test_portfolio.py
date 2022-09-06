import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

import os

os.environ["DATABASE_URL"] = SQLALCHEMY_DATABASE_URL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi.testclient import TestClient

from app.api.dependencies import get_db
from app.db.init_db import init_db
from app.main import app


@pytest.fixture()
def client():
    yield TestClient(app)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

init_db(engine)


def override_get_db():
    """Dependency for getting a database session"""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


def test_list_portfolios(client):
    response = client.get("/portfolios")
    assert response.status_code == 200
    assert response.json() == {"portfolios": []}
