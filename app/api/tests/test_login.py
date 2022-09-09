class TestLoginApi:
    def test_get_access_token(self, client):
        client.post("/users/", json={"username": "Ikari", "password": "safe password"})
        response = client.post(
            "/token", data={"username": "Ikari", "password": "safe password"}
        )
        response_json = response.json()
        assert "access_token" in response_json
        assert "token_type" in response_json
        assert response_json["token_type"] == "bearer"
