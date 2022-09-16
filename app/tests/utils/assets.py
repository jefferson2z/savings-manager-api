def create_asset(client, jwt, name, portfolio_id=1):
    response = client.post(
        "/assets/",
        json={"name": name, "portfolio_id": portfolio_id},
        headers={"Authorization": f"Bearer {jwt}"},
    )
    return response
