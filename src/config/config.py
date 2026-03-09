from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    environment: str
    postgres_version: str
    postgres_port: str
    postgres_database: str
    postgres_user: str
    postgres_password: str
    postgres_url: str


settings = Settings()
