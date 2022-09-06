def test_list_portfolios(client):
    response = client.get("/portfolios")
    assert response.status_code == 200
    assert response.json() == {"portfolios": []}
