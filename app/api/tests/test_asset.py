class TestAssetApi:
    def test_create_asset(self, client, jwt):
        client.post(
            "/portfolios/",
            json={"name": "Fixed Income"},
            headers={"Authorization": f"Bearer {jwt}"},
        )

        response = client.post(
            "/assets/",
            json={"name": "Savings", "portfolio_id": "1"},
            headers={"Authorization": f"Bearer {jwt}"},
        )

        assert response.status_code == 201
        assert response.json() == {
            "asset": {"id": 1, "name": "Savings", "portfolio_id": 1}
        }
