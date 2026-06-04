from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    service_name: str = "noiseproof-agent-api"
    workflow_version: str = "phase40-lineage-warning-code-dashboard"
    database_url: str = "postgresql://noiseproof:noiseproof@localhost:5432/noiseproof"
    max_raw_upload_bytes: int = 1_000_000
    noiseproof_scanner: str = "unavailable"
    raw_file_scanner_timeout_seconds: int = 30
    clamd_host: str = "clamav"
    clamd_port: int = 3310
    openai_api_key: str = ""
    embedding_model: str = "text-embedding-3-small"
    embedding_dimension: int = 1536

    model_config = SettingsConfigDict(
        env_file=("../../.env", ".env"),
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
