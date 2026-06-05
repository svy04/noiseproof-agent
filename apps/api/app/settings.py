from functools import lru_cache

from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    service_name: str = "noiseproof-agent-api"
    workflow_version: str = "phase40-lineage-warning-code-dashboard"
    database_url: str = "postgresql://noiseproof:noiseproof@localhost:5432/noiseproof"
    max_raw_upload_bytes: int = 1_000_000
    noiseproof_scanner: str = "unavailable"
    raw_file_scanner_timeout_seconds: int = 30
    raw_file_download_operator_token: str = Field(
        default="",
        validation_alias=AliasChoices(
            "NOISEPROOF_RAW_FILE_DOWNLOAD_OPERATOR_TOKEN",
            "raw_file_download_operator_token",
        ),
    )
    clamd_host: str = "clamav"
    clamd_port: int = 3310
    openai_api_key: str = ""
    embedding_model: str = "text-embedding-3-small"
    embedding_dimension: int = 1536
    enable_openai_provider: bool = Field(
        default=False,
        validation_alias=AliasChoices(
            "NOISEPROOF_ENABLE_OPENAI_PROVIDER",
            "enable_openai_provider",
        ),
    )
    ci: bool = Field(default=False, validation_alias=AliasChoices("CI", "ci"))
    openai_provider_timeout_seconds: float = Field(
        default=10.0,
        validation_alias=AliasChoices(
            "OPENAI_PROVIDER_TIMEOUT_SECONDS",
            "openai_provider_timeout_seconds",
        ),
    )

    model_config = SettingsConfigDict(
        env_file=("../../.env", ".env"),
        extra="ignore",
        populate_by_name=True,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
