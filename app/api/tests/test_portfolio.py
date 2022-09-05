import pytest

# from fastapi.testclient import TestClient

# from app.main import app


# client = TestClient(app)


@pytest.mark.skip(reason="must handle database connection")
def test_list_portfolios():
    pass
    # response = client.get("/portfolios")
    # assert response.status_code == 200
    # assert response.json() == {"portfolios": []}
