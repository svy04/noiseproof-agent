from __future__ import annotations

from fastapi import Depends, HTTPException

from app.schemas import EmbeddingModelPreviewOut, EmbeddingModelPreviewRequest
from app.services.openai_embedding_provider import OpenAIEmbeddingProviderClient
from app.settings import Settings, get_settings

SOURCE_REVIEW_PATH = "docs/review/embedding-provider-source-review.md"


def get_embedding_provider_client(settings: Settings = Depends(get_settings)):
    if settings.ci:
        return None
    if not settings.enable_openai_provider:
        return None
    if not settings.openai_api_key.strip():
        return None
    if settings.openai_provider_timeout_seconds <= 0:
        return None
    return OpenAIEmbeddingProviderClient(
        timeout_seconds=settings.openai_provider_timeout_seconds
    )


def preview_embedding_model_provider(
    payload: EmbeddingModelPreviewRequest,
    settings: Settings,
    provider_client=None,
) -> EmbeddingModelPreviewOut:
    provider = payload.provider.lower()
    if provider != "openai":
        raise HTTPException(
            status_code=400,
            detail="Only openai is supported for the disabled embedding provider preview.",
        )
    if payload.encoding_format != "float":
        raise HTTPException(
            status_code=400,
            detail="Only encoding_format: float is allowed for the current provider contract.",
        )

    model = payload.embedding_model or settings.embedding_model or "text-embedding-3-small"
    dimension = payload.embedding_dimension or settings.embedding_dimension or 1536
    configured = bool(settings.openai_api_key.strip())
    if payload.allow_provider_call and configured and provider_client is None:
        raise HTTPException(
            status_code=501,
            detail="live embedding provider client is not implemented for this phase.",
        )
    if payload.allow_provider_call and configured and provider_client is not None:
        provider_response = provider_client.create_embedding(
            text=payload.text,
            model=model,
            dimension=dimension,
            encoding_format="float",
            api_key=settings.openai_api_key,
        )
        embedding = provider_response.get("embedding")
        if not isinstance(embedding, list) or len(embedding) != dimension:
            raise HTTPException(
                status_code=502,
                detail="provider response dimension mismatch.",
            )
        provider_call_boundary = provider_response.get(
            "provider_call_boundary",
            "mocked_provider_client",
        )
        owner_runtime_provider_call = (
            provider_call_boundary == "openai_python_sdk_disabled_adapter"
        )
        embedding_status = (
            "owner_runtime_provider_generated"
            if owner_runtime_provider_call
            else "mocked_provider_generated"
        )
        network_boundary = (
            "owner_runtime_provider_call"
            if owner_runtime_provider_call
            else "mocked_provider_call_only"
        )
        cost_boundary = (
            "owner_runtime_provider_cost_possible"
            if owner_runtime_provider_call
            else "no_live_cost_incurred"
        )
        source_warning = (
            "Embedding vector came from an owner-runtime OpenAI provider call."
            if owner_runtime_provider_call
            else "Embedding vector came from an injected mocked provider client."
        )
        runtime_warning = (
            "Live provider calls are owner-runtime only and not CI evidence."
            if owner_runtime_provider_call
            else "No live OpenAI provider call was made by the default runtime."
        )
        return EmbeddingModelPreviewOut(
            provider=provider,
            embedding_model=model,
            embedding_dimension=dimension,
            encoding_format="float",
            configured=True,
            embedding_status=embedding_status,
            embedding=embedding,
            metadata_json={
                "provider": provider,
                "provider_model": provider_response.get("model", model),
                "provider_dimension": dimension,
                "network_boundary": network_boundary,
                "cost_boundary": cost_boundary,
                "persistence_boundary": "preview_only_not_persisted",
                "source_review": SOURCE_REVIEW_PATH,
                "provider_call_boundary": provider_call_boundary,
                "provider_response_dimension_check": "passed",
                "usage": provider_response.get("usage", {}),
                "secret_exposed": False,
            },
            warnings=[
                source_warning,
                runtime_warning,
                "The vector is preview-only and is not persisted or used for retrieval.",
                "Actual live embedding model generation remains unproven.",
            ],
        )
    status = "configured_no_call" if configured else "disabled_missing_api_key"

    warnings = [
        "This endpoint previews provider readiness and does not call OpenAI.",
        "No embedding vector is generated, persisted, or used for retrieval.",
        "Actual embedding model generation remains unproven.",
    ]
    if configured:
        warnings.append("OPENAI_API_KEY is configured but not called in this phase.")
    else:
        warnings.append("OPENAI_API_KEY is not configured; provider calls remain disabled.")

    return EmbeddingModelPreviewOut(
        provider=provider,
        embedding_model=model,
        embedding_dimension=dimension,
        encoding_format="float",
        configured=configured,
        embedding_status=status,
        embedding=None,
        metadata_json={
            "provider": provider,
            "provider_model": model,
            "provider_dimension": dimension,
            "network_boundary": "no_network_call",
            "cost_boundary": "no_cost_incurred",
            "persistence_boundary": "preview_only_not_persisted",
            "source_review": SOURCE_REVIEW_PATH,
            "secret_exposed": False,
        },
        warnings=warnings,
    )
