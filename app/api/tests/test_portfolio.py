class TestPortfolioApi:
    def test_create_portfolio(self, client):
        response = client.post("/portfolios/", json={"name": "Stocks"})
        assert response.status_code == 200
        assert response.json() == {"portfolio": {"id": 1, "name": "Stocks"}}

    def test_list_portfolios(self, client):
        response = client.get("/portfolios")
        assert response.status_code == 200
        assert response.json() == {"portfolios": []}
