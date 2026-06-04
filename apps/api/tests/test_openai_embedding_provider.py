import pytest


def test_openai_embedding_provider_normalizes_sdk_response_without_secret_leak():
    from app.services.openai_embedding_provider import OpenAIEmbeddingProviderClient

    captured = {}

    class FakeUsage:
        def model_dump(self):
            return {"prompt_tokens": 4, "total_tokens": 4}

    class FakeEmbedding:
        embedding = [0.1, 0.2, 0.3]

    class FakeResponse:
        data = [FakeEmbedding()]
        model = "text-embedding-3-small"
        usage = FakeUsage()

    class FakeEmbeddings:
        def create(self, **kwargs):
            captured["create_kwargs"] = kwargs
            return FakeResponse()

    class FakeOpenAI:
        def __init__(self, *, api_key, timeout):
            captured["api_key"] = api_key
            captured["timeout"] = timeout
            self.embeddings = FakeEmbeddings()

    client = OpenAIEmbeddingProviderClient(
        client_factory=FakeOpenAI,
        timeout_seconds=7.5,
    )

    result = client.create_embedding(
        text="Enterprise demand growth",
        model="text-embedding-3-small",
        dimension=3,
        encoding_format="float",
        api_key="sk-test-secret",
    )

    assert captured["api_key"] == "sk-test-secret"
    assert captured["timeout"] == 7.5
    assert captured["create_kwargs"] == {
        "input": "Enterprise demand growth",
        "model": "text-embedding-3-small",
        "dimensions": 3,
        "encoding_format": "float",
    }
    assert result["embedding"] == [0.1, 0.2, 0.3]
    assert result["model"] == "text-embedding-3-small"
    assert result["usage"] == {"prompt_tokens": 4, "total_tokens": 4}
    assert result["provider_call_boundary"] == "openai_python_sdk_disabled_adapter"
    assert result["timeout_seconds"] == 7.5
    assert result["secret_exposed"] is False
    assert "sk-test-secret" not in repr(result)


def test_openai_embedding_provider_redacts_secret_from_provider_errors():
    from app.services.openai_embedding_provider import (
        EmbeddingProviderError,
        OpenAIEmbeddingProviderClient,
    )

    class FakeEmbeddings:
        def create(self, **_kwargs):
            raise RuntimeError("provider rejected sk-test-secret")

    class FakeOpenAI:
        def __init__(self, *, api_key, timeout):
            self.embeddings = FakeEmbeddings()

    client = OpenAIEmbeddingProviderClient(client_factory=FakeOpenAI)

    with pytest.raises(EmbeddingProviderError) as exc_info:
        client.create_embedding(
            text="Enterprise demand growth",
            model="text-embedding-3-small",
            dimension=3,
            encoding_format="float",
            api_key="sk-test-secret",
        )

    assert exc_info.value.error_type == "provider_error"
    assert "sk-test-secret" not in str(exc_info.value)
    assert "[redacted]" in str(exc_info.value)


def test_openai_embedding_provider_maps_timeout_without_secret_leak():
    from app.services.openai_embedding_provider import (
        EmbeddingProviderError,
        OpenAIEmbeddingProviderClient,
    )

    class FakeEmbeddings:
        def create(self, **_kwargs):
            raise TimeoutError("timeout for sk-test-secret")

    class FakeOpenAI:
        def __init__(self, *, api_key, timeout):
            self.embeddings = FakeEmbeddings()

    client = OpenAIEmbeddingProviderClient(client_factory=FakeOpenAI)

    with pytest.raises(EmbeddingProviderError) as exc_info:
        client.create_embedding(
            text="Enterprise demand growth",
            model="text-embedding-3-small",
            dimension=3,
            encoding_format="float",
            api_key="sk-test-secret",
        )

    assert exc_info.value.error_type == "provider_timeout"
    assert "sk-test-secret" not in str(exc_info.value)
