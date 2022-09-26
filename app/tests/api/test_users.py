class TestUserApi:
    def test_create_user(self, client):
        response = client.post(
            "/users/", json={"username": "Ikari", "password": "safe password"}
        )
        assert response.status_code == 201
        assert response.json() == {"id": "1", "username": "Ikari", "portfolios": []}

    def test_get_me_user(self, client, jwt):
        response = client.get(
            "/users/me",
            headers={"Authorization": f"Bearer {jwt}"},
        )
        assert response.json() == {"id": "1", "username": "Ikari", "portfolios": []}

    def test_delete_user(self, client, jwt):
        response = client.delete(
            "/users/me",
            headers={"Authorization": f"Bearer {jwt}"},
        )
        assert response.status_code == 200
        assert response.json() == {"id": "1", "username": "Ikari", "portfolios": []}

    def test_update_user(self, client):
        pass
