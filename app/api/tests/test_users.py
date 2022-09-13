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

    def test_get_me_user(self, client, jwt):
        response = client.get(
            "/users/me",
            headers={"Authorization": f"Bearer {jwt}"},
        )
        assert response.json() == {"id": "1", "username": "Ikari"}

    def test_get_user_not_found(self, client):
        response = client.get("/users/1")
        assert response.status_code == 404

    def test_delete_user(self, client):
        post_response = client.post(
            "/users/", json={"username": "Ikari", "password": "safe password"}
        )
        created_user = post_response.json()
        response = client.delete(f"/users/{created_user.get('id')}")
        assert response.status_code == 200

    def test_update_user(self, client):
        pass
