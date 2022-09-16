def create_portfolio(client, jwt, name):
    response = client.post(
        "/portfolios/",
        json={"name": name},
        headers={"Authorization": f"Bearer {jwt}"},
    )
    return response
