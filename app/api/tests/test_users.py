class TestUserApi:
    def test_create_user(self, client):
        response = client.post(
            "/users/", json={"username": "Ikari", "password": "safe password"}
        )
        assert response.status_code == 201
        assert response.json() == {"id": "1", "username": "Ikari"}

    def test_get_user(self, client):
        post_response = client.post(
            "/users/", json={"username": "Ikari", "password": "safe password"}
        )
        created_user = post_response.json()
        response = client.get(f"/users/{created_user.get('id')}")
        assert response.status_code == 200
        assert response.json() == created_user

    def test_delete_user(self, client):
        pass

    def test_update_usere(self, client):
        pass
