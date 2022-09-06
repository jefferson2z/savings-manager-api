class TestUserApi:
    def test_create_user(self, client):
        response = client.post(
            "/users/", json={"username": "Ikari", "password": "safe password"}
        )
        assert response.status_code == 200
        assert response.json() == {"id": "1", "username": "Ikari"}

    def test_get_user(self, client):
        pass

    def test_delete_user(self, client):
        pass

    def test_update_usere(self, client):
        pass
