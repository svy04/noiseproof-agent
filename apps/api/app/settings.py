from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    service_name: str = "noiseproof-agent-api"
    workflow_version: str = "phase5.5-collection-plan-preview"
    database_url: str = "postgresql://noiseproof:noiseproof@localhost:5432/noiseproof"

    model_config = SettingsConfigDict(
        env_file=("../../.env", ".env"),
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
