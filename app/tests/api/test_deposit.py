from app.tests.utils.deposits import create_deposit
from app.tests.utils.portfolios import create_portfolio
from app.tests.utils.assets import create_asset


class TestDepositApi:
    def test_create_deposit(self, client, jwt):
        create_portfolio(client, jwt, "Fixed Income")

        create_asset(client, jwt, "Savings", 1)

        response = create_deposit(
            client,
            jwt,
            amount=15.30,
            date="2022-09-26",
            asset_id=1,
            description="Nice description",
        )

        assert response.status_code == 201
        assert response.json() == {
            "id": 1,
            "amount": 15.30,
            "date": "2022-09-26",
            "description": "Nice description",
            "asset_id": 1,
        }

    def test_get_deposit(self, client, jwt):
        create_portfolio(client, jwt, "Fixed Income")

        create_asset(client, jwt, "Savings", 1)

        created_response = create_deposit(
            client,
            jwt,
            amount=15.30,
            date="2022-09-26",
            asset_id=1,
            description="Nice description",
        )
        created_deposit = created_response.json()

        response = client.get(
            f"/deposits/{created_deposit['id']}",
            headers={"Authorization": f"Bearer {jwt}"},
        )

        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "amount": 15.30,
            "date": "2022-09-26",
            "description": "Nice description",
            "asset_id": 1,
        }

    def test_list_deposits(self, client, jwt):
        create_portfolio(client, jwt, "Fixed Income")

        create_asset(client, jwt, "Savings", 1)

        create_deposit(
            client,
            jwt,
            amount=15.30,
            date="2022-09-26",
            asset_id=1,
            description="Nice description",
        )

        response = client.get(
            "/deposits/?asset_id=1",
            headers={"Authorization": f"Bearer {jwt}"},
        )

        assert response.status_code == 200
        assert response.json() == [
            {
                "id": 1,
                "amount": 15.30,
                "date": "2022-09-26",
                "description": "Nice description",
                "asset_id": 1,
            }
        ]

    def test_update_deposit(self, client, jwt):
        create_portfolio(client, jwt, "Fixed Income")

        create_asset(client, jwt, "Savings", 1)

        create_deposit(
            client,
            jwt,
            amount=15.30,
            date="2022-09-26",
            asset_id=1,
            description="Nice description",
        )

        response = client.put(
            "/deposits/1",
            json={"amount": 1080.20},
            headers={"Authorization": f"Bearer {jwt}"},
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "amount": 1080.20,
            "date": "2022-09-26",
            "description": "Nice description",
            "asset_id": 1,
        }

    def test_delete_deposit(self, client, jwt):
        create_portfolio(client, jwt, "Fixed Income")

        create_asset(client, jwt, "Savings", 1)

        create_deposit(
            client,
            jwt,
            amount=15.30,
            date="2022-09-26",
            asset_id=1,
            description="Nice description",
        )

        response = client.delete(
            "/deposits/1",
            headers={"Authorization": f"Bearer {jwt}"},
        )

        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "amount": 15.30,
            "date": "2022-09-26",
            "description": "Nice description",
            "asset_id": 1,
        }
