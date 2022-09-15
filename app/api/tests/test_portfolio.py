class TestPortfolioApi:
    def test_create_portfolio(self, client, jwt):
        response = client.post(
            "/portfolios/",
            json={"name": "Stocks"},
            headers={"Authorization": f"Bearer {jwt}"},
        )

        assert response.status_code == 201
        assert response.json() == {
            "portfolio": {"id": 1, "name": "Stocks", "user_id": 1, "assets": []}
        }

    def test_get_portfolio(self, client, jwt):
        client.post(
            "/portfolios/",
            json={"name": "Stocks"},
            headers={"Authorization": f"Bearer {jwt}"},
        )
        response = client.get(
            "/portfolios/1",
            headers={"Authorization": f"Bearer {jwt}"},
        )
        assert response.status_code == 200
        assert response.json() == {
            "portfolio": {"id": 1, "name": "Stocks", "user_id": 1, "assets": []}
        }

    def test_list_portfolios(self, client, jwt):
        response = client.post(
            "/portfolios/",
            json={"name": "Stocks"},
            headers={"Authorization": f"Bearer {jwt}"},
        )
        response = client.get(
            "/portfolios",
            headers={"Authorization": f"Bearer {jwt}"},
        )
        assert response.status_code == 200
        assert response.json() == {
            "portfolios": [{"id": 1, "name": "Stocks", "user_id": 1, "assets": []}]
        }
