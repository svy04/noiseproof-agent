from app.settings import Settings
from app.services.embedding_model_preview import get_embedding_provider_client
from app.services.openai_embedding_provider import OpenAIEmbeddingProviderClient


def test_openai_provider_client_is_disabled_by_default_even_with_api_key():
    settings = Settings(openai_api_key="sk-test-secret")

    provider_client = get_embedding_provider_client(settings)

    assert provider_client is None


def test_openai_provider_client_is_disabled_without_api_key_even_when_opted_in():
    settings = Settings(enable_openai_provider=True, openai_api_key="", ci=False)

    provider_client = get_embedding_provider_client(settings)

    assert provider_client is None


def test_openai_provider_client_is_disabled_in_ci_even_when_opted_in():
    settings = Settings(
        enable_openai_provider=True,
        openai_api_key="sk-test-secret",
        ci=True,
    )

    provider_client = get_embedding_provider_client(settings)

    assert provider_client is None


def test_openai_provider_client_requires_owner_runtime_opt_in_outside_ci():
    settings = Settings(
        enable_openai_provider=True,
        openai_api_key="sk-test-secret",
        ci=False,
        openai_provider_timeout_seconds=4.5,
    )

    provider_client = get_embedding_provider_client(settings)

    assert isinstance(provider_client, OpenAIEmbeddingProviderClient)
    assert provider_client._timeout_seconds == 4.5


def test_settings_reads_noiseproof_openai_provider_opt_in_env(monkeypatch):
    monkeypatch.setenv("NOISEPROOF_ENABLE_OPENAI_PROVIDER", "true")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-env-secret")
    monkeypatch.setenv("CI", "false")

    settings = Settings()

    assert settings.enable_openai_provider is True
    assert settings.openai_api_key == "sk-env-secret"
    assert settings.ci is False
