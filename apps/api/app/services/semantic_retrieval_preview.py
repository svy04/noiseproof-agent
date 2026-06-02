from uuid import UUID

from fastapi import HTTPException

from app.db import Repository
from app.schemas import (
    SemanticRetrievalCandidateOut,
    SemanticRetrievalPreviewOut,
    SemanticRetrievalPreviewRequest,
)


RANKING_BOUNDARY = "exact_cosine_caller_provided_query_vector"
PERSISTENCE_BOUNDARY = "preview_only_not_persisted"


def preview_semantic_retrieval(
    *,
    document_id: UUID,
    payload: SemanticRetrievalPreviewRequest,
    repository: Repository,
) -> SemanticRetrievalPreviewOut:
    if len(payload.query_embedding) != payload.embedding_dimension:
        raise HTTPException(
            status_code=400,
            detail="query_embedding length must match embedding_dimension.",
        )

    chunks = list(repository.list_document_chunks(document_id=document_id, limit=100))
    rows = list(
        repository.preview_semantic_retrieval_candidates(
            document_id=document_id,
            query_embedding=payload.query_embedding,
            embedding_model=payload.embedding_model,
            embedding_dimension=payload.embedding_dimension,
            limit=payload.limit,
        )
    )

    candidate_chunk_ids = [str(row["chunk_id"]) for row in rows]
    missing_embedding_chunk_ids = [
        str(chunk["id"]) for chunk in chunks if str(chunk["id"]) not in candidate_chunk_ids
    ]
    warnings = [
        "Semantic retrieval preview uses a caller-provided query vector; it does not generate embeddings.",
        "Semantic retrieval preview is preview-only and does not persist retrieval_runs.",
    ]
    if not chunks:
        warnings.append("No persisted document_chunks exist for this document.")
    if chunks and missing_embedding_chunk_ids:
        warnings.append(
            "Some persisted document_chunks have no matching created embedding for the requested model/dimension."
        )
    if not rows:
        warnings.append(
            "No created chunk_embeddings matched the requested model/dimension."
        )

    return SemanticRetrievalPreviewOut(
        question=payload.question,
        retrieval_mode="semantic_preview",
        persistence_boundary=PERSISTENCE_BOUNDARY,
        ranking_boundary=RANKING_BOUNDARY,
        candidates=[_candidate_from_row(row) for row in rows],
        missing_embedding_chunk_ids=missing_embedding_chunk_ids,
        warnings=warnings,
        metadata_json={
            "document_id": str(document_id),
            "source_table": "document_chunks",
            "embedding_table": "chunk_embeddings",
            "retrieval_mode": "semantic_preview",
            "candidate_chunk_ids": candidate_chunk_ids,
            "missing_embedding_chunk_ids": missing_embedding_chunk_ids,
            "embedding_model": payload.embedding_model,
            "embedding_dimension": payload.embedding_dimension,
            "query_vector_source": "caller_provided_vector",
            "ranking_boundary": RANKING_BOUNDARY,
            "persistence_boundary": PERSISTENCE_BOUNDARY,
            "no_retrieval_run_persistence": True,
            "no_embedding_generation": True,
            "no_evidence_ledger_generation": True,
        },
    )


def _candidate_from_row(row: dict) -> SemanticRetrievalCandidateOut:
    return SemanticRetrievalCandidateOut(
        chunk_id=row["chunk_id"],
        embedding_id=row["embedding_id"],
        document_id=row["document_id"],
        chunk_index=row["chunk_index"],
        chunk_strategy=row["chunk_strategy"],
        text=row["chunk_text"],
        distance=float(row["distance"]),
        distance_metric=row["distance_metric"],
        embedding_model=row["embedding_model"],
        metadata={
            "source_table": "document_chunks",
            "embedding_table": "chunk_embeddings",
            "embedding_id": str(row["embedding_id"]),
            "embedding_model": row["embedding_model"],
            "embedding_dimension": row["embedding_dimension"],
            "distance_metric": row["distance_metric"],
            "ranking_boundary": RANKING_BOUNDARY,
            "chunk_metadata_json": row.get("chunk_metadata_json") or {},
            "embedding_metadata_json": row.get("embedding_metadata_json") or {},
        },
    )
