from __future__ import annotations

from typing import Any, Callable

from openai import OpenAI


class EmbeddingProviderError(RuntimeError):
    def __init__(self, error_type: str, message: str) -> None:
        self.error_type = error_type
        super().__init__(message)


class OpenAIEmbeddingProviderClient:
    def __init__(
        self,
        *,
        client_factory: Callable[..., Any] = OpenAI,
        timeout_seconds: float = 10.0,
    ) -> None:
        self._client_factory = client_factory
        self._timeout_seconds = timeout_seconds

    def create_embedding(
        self,
        *,
        text: str,
        model: str,
        dimension: int,
        encoding_format: str,
        api_key: str,
    ) -> dict:
        try:
            client = self._client_factory(api_key=api_key, timeout=self._timeout_seconds)
            response = client.embeddings.create(
                input=text,
                model=model,
                dimensions=dimension,
                encoding_format=encoding_format,
            )
        except TimeoutError as exc:
            raise EmbeddingProviderError(
                "provider_timeout",
                self._redact_secret(f"provider timeout: {exc}", api_key),
            ) from exc
        except Exception as exc:
            raise EmbeddingProviderError(
                "provider_error",
                self._redact_secret(f"provider error: {exc}", api_key),
            ) from exc

        return {
            "embedding": self._extract_embedding(response),
            "model": self._extract_model(response, model),
            "usage": self._extract_usage(response),
            "provider_call_boundary": "openai_python_sdk_disabled_adapter",
            "timeout_seconds": self._timeout_seconds,
            "secret_exposed": False,
        }

    @staticmethod
    def _extract_embedding(response: Any) -> list:
        data = getattr(response, "data", None)
        if data is None and isinstance(response, dict):
            data = response.get("data")
        first = data[0] if data else None
        embedding = getattr(first, "embedding", None)
        if embedding is None and isinstance(first, dict):
            embedding = first.get("embedding")
        return list(embedding or [])

    @staticmethod
    def _extract_model(response: Any, fallback: str) -> str:
        if isinstance(response, dict):
            return response.get("model", fallback)
        return getattr(response, "model", fallback)

    @staticmethod
    def _extract_usage(response: Any) -> dict:
        usage = response.get("usage") if isinstance(response, dict) else getattr(response, "usage", None)
        if usage is None:
            return {}
        if isinstance(usage, dict):
            return dict(usage)
        if hasattr(usage, "model_dump"):
            return dict(usage.model_dump())
        return dict(usage)

    @staticmethod
    def _redact_secret(message: str, api_key: str) -> str:
        if api_key:
            message = message.replace(api_key, "[redacted]")
        return message
