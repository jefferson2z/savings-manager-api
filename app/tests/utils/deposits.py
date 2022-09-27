def create_deposit(client, jwt, *, amount, date, asset_id, description=""):
    response = client.post(
        "/deposits/",
        json={
            "amount": amount,
            "date": date,
            "asset_id": asset_id,
            "description": description,
        },
        headers={"Authorization": f"Bearer {jwt}"},
    )
    return response
