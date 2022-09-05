from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Savings Manager"

    # Database Settings
    postgres_user: str | None
    postgres_password: str | None
    postgres_server: str | None
    postgres_port: str | None
    postgres_db: str | None
    database_url: str | None

    # Clients Settings
    client_url: str


settings = Settings()
