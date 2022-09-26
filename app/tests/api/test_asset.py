from app.tests.utils.portfolios import create_portfolio
from app.tests.utils.assets import create_asset


class TestAssetApi:
    def test_create_asset(self, client, jwt):
        create_portfolio(client, jwt, "Fixed Income")

        response = create_asset(client, jwt, "Savings", 1)

        assert response.status_code == 201
        assert response.json() == {"id": 1, "name": "Savings", "portfolio_id": 1}

    def test_get_asset(self, client, jwt):
        create_portfolio(client, jwt, "Fixed Income")

        create_response = create_asset(client, jwt, "Savings", 1)
        created_asset = create_response.json()

        response = client.get(
            f"/assets/{created_asset['id']}",
            headers={"Authorization": f"Bearer {jwt}"},
        )

        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "name": "Savings",
            "portfolio_id": 1,
        }

    def test_list_assets(self, client, jwt):
        create_portfolio(client, jwt, "Fixed Income")
        create_asset(client, jwt, "Savings", 1)

        response = client.get(
            "/assets/?portfolio_id=1",
            headers={"Authorization": f"Bearer {jwt}"},
        )

        assert response.status_code == 200
        assert response.json() == [
            {
                "id": 1,
                "name": "Savings",
                "portfolio_id": 1,
            }
        ]

    def test_update_asset(self, client, jwt):
        create_portfolio(client, jwt, "Fixed Income")
        create_asset(client, jwt, "Savings", 1)

        response = client.put(
            "/assets/1",
            json={"name": "Checking"},
            headers={"Authorization": f"Bearer {jwt}"},
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "name": "Checking",
            "portfolio_id": 1,
        }

    def test_delete_asset(self, client, jwt):
        create_portfolio(client, jwt, "Fixed Income")
        create_asset(client, jwt, "Savings", 1)

        response = client.delete(
            "/assets/1",
            headers={"Authorization": f"Bearer {jwt}"},
        )

        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "name": "Savings",
            "portfolio_id": 1,
        }
