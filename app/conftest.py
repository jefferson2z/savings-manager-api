import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

import os

os.environ["DATABASE_URL"] = SQLALCHEMY_DATABASE_URL


from app.main import app
from app.api.dependencies import get_db
from app.db.init_db import init_db

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


@pytest.fixture()
def client():
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
