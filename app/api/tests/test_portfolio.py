from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_list_portfolios():
    response = client.get("/portfolios")
    assert response.status_code == 200
    assert response.json() == {"portfolios": []}
