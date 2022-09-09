from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Savings Manager"

    # Security
    secret_key: str
    jwt_algorithm: str
    access_token_expire_minutes: str

    # Database Settings
    postgres_user: str | None
    postgres_password: str | None
    postgres_server: str | None
    postgres_port: str | None
    postgres_db: str | None
    database_url: str | None

    # Clients Settings
    client_url: str

    def get_database_url(self):
        if self.database_url:
            return self.database_url
        else:
            return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_server}:{self.postgres_port}/{self.postgres_db}"


settings = Settings()
