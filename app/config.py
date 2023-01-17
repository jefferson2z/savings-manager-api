from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Savings Manager"

    # Security
    secret_key: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: str = "30"

    # Database Settings
    postgres_user: str | None = None
    postgres_password: str | None = None
    postgres_server: str | None = None
    postgres_port: str | None = None
    postgres_db: str | None = None
    database_url: str | None = None

    # Redis Settings
    redis_host: str | None = None
    redis_port: str | None = None

    # Clients Settings
    client_url: str | None = None

    # Testing environment
    ci: bool = False

    def get_database_url(self):
        if self.database_url:
            return self.database_url
        else:
            return (
                f"postgresql://{self.postgres_user}:{self.postgres_password}"
                f"@{self.postgres_server}:{self.postgres_port}/{self.postgres_db}"
            )

    def get_redis_address(self):
        return {"host": self.redis_host, "port": self.redis_port}


settings = Settings()
