from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.db import Repository, get_repository
from app.schemas import (
    ChunkEmbeddingCreate,
    ChunkEmbeddingOut,
    ChunkEmbeddingRequest,
    EmbeddingModelPreviewOut,
    EmbeddingModelPreviewRequest,
    TextEmbeddingPreviewOut,
    TextEmbeddingPreviewRequest,
)
from app.services.embedding_model_preview import preview_embedding_model_provider
from app.services.text_embedding_preview import preview_text_embedding
from app.settings import Settings, get_settings

router = APIRouter(prefix="/chunks", tags=["chunk-embeddings"])


def _normalize_embedding_metadata(payload: ChunkEmbeddingRequest) -> dict:
    metadata = dict(payload.metadata_json)
    embedding_source = metadata.get("embedding_source")
    if embedding_source not in (None, "caller_provided_vector"):
        raise HTTPException(
            status_code=400,
            detail="Chunk embeddings currently accept only caller-provided vector input.",
        )
    if payload.embedding is not None and len(payload.embedding) != payload.embedding_dimension:
        raise HTTPException(
            status_code=400,
            detail="embedding_dimension must match the caller-provided vector length.",
        )

    metadata["embedding_source"] = "caller_provided_vector"
    metadata["persistence_boundary"] = "caller_provided_embedding_only_no_generation"
    return metadata


@router.post("/embedding-preview", response_model=TextEmbeddingPreviewOut)
def create_text_embedding_preview(
    payload: TextEmbeddingPreviewRequest,
) -> TextEmbeddingPreviewOut:
    return preview_text_embedding(payload)


@router.post("/embedding-model-preview", response_model=EmbeddingModelPreviewOut)
def create_embedding_model_preview(
    payload: EmbeddingModelPreviewRequest,
    settings: Settings = Depends(get_settings),
) -> EmbeddingModelPreviewOut:
    return preview_embedding_model_provider(payload, settings)


@router.post("/{chunk_id}/embeddings", response_model=ChunkEmbeddingOut, status_code=201)
def create_chunk_embedding(
    chunk_id: UUID,
    payload: ChunkEmbeddingRequest,
    repository: Repository = Depends(get_repository),
) -> dict:
    metadata = _normalize_embedding_metadata(payload)
    return repository.create_chunk_embedding(
        ChunkEmbeddingCreate(
            chunk_id=chunk_id,
            embedding_model=payload.embedding_model,
            embedding_dimension=payload.embedding_dimension,
            embedding_text_hash=payload.embedding_text_hash,
            distance_metric=payload.distance_metric,
            embedding_status=payload.embedding_status,
            embedding=payload.embedding,
            metadata_json=metadata,
        )
    )


@router.get("/{chunk_id}/embeddings", response_model=list[ChunkEmbeddingOut])
def list_chunk_embeddings(
    chunk_id: UUID,
    embedding_model: str | None = None,
    embedding_status: str | None = None,
    limit: int = 20,
    repository: Repository = Depends(get_repository),
) -> list[dict]:
    return list(
        repository.list_chunk_embeddings(
            chunk_id=chunk_id,
            embedding_model=embedding_model,
            embedding_status=embedding_status,
            limit=limit,
        )
    )
