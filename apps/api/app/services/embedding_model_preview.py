from __future__ import annotations

from fastapi import HTTPException

from app.schemas import EmbeddingModelPreviewOut, EmbeddingModelPreviewRequest
from app.settings import Settings

SOURCE_REVIEW_PATH = "docs/review/embedding-provider-source-review.md"


def preview_embedding_model_provider(
    payload: EmbeddingModelPreviewRequest,
    settings: Settings,
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
