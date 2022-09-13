from wsgiref import headers


class TestPortfolioApi:
    def test_create_portfolio(self, client, jwt):
        response = client.post(
            "/portfolios/",
            json={"name": "Stocks"},
            headers={"Authorization": f"Bearer {jwt}"},
        )

        assert response.status_code == 201
        assert response.json() == {"portfolio": {"id": 1, "name": "Stocks"}}

    def test_list_portfolios(self, client, jwt):
        response = client.get(
            "/portfolios",
            headers={"Authorization": f"Bearer {jwt}"},
        )
        assert response.status_code == 200
        assert response.json() == {"portfolios": []}
