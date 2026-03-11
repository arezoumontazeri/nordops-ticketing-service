from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "NordOps Ticketing Service"
    log_level: str = "INFO"
    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/ticketing"

settings = Settings()