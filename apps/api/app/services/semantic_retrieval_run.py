import time
from uuid import UUID

from fastapi import HTTPException

from app.db import Repository
from app.schemas import (
    RetrievalCandidateOut,
    RetrievalRunCreate,
    RetrievalRunResponse,
    SemanticRetrievalRunRequest,
)
from app.services.semantic_retrieval_preview import RANKING_BOUNDARY


PERSISTENCE_BOUNDARY = "semantic_retrieval_run_only_no_evidence_ledger"
RETRIEVAL_MODE = "semantic_persisted"
STRATEGY = "semantic-cosine"


def run_semantic_retrieval(
    *,
    document_id: UUID,
    payload: SemanticRetrievalRunRequest,
    repository: Repository,
) -> RetrievalRunResponse:
    if len(payload.query_embedding) != payload.embedding_dimension:
        raise HTTPException(
            status_code=400,
            detail="query_embedding length must match embedding_dimension.",
        )

    started_at = time.perf_counter()
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
    candidate_embedding_ids = [str(row["embedding_id"]) for row in rows]
    missing_embedding_chunk_ids = [
        str(chunk["id"]) for chunk in chunks if str(chunk["id"]) not in candidate_chunk_ids
    ]
    warnings = [
        "Semantic retrieval run uses a caller-provided query vector; it does not generate embeddings.",
        "Semantic retrieval run persists retrieval_runs only and does not generate Evidence Ledger entries.",
        "This semantic retrieval run is not financial advice.",
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

    result_count = len(rows)
    run = repository.create_retrieval_run(
        RetrievalRunCreate(
            question=payload.question,
            strategy=STRATEGY,
            status="completed" if result_count else "no_results",
            latency_ms=max(0, round((time.perf_counter() - started_at) * 1000)),
            result_count=result_count,
            hit_rate=round(result_count / payload.limit, 4),
            citation_coverage=1.0 if result_count else 0.0,
            missing_evidence_count=0 if result_count else 1,
            metadata_json={
                "document_id": str(document_id),
                "source_table": "document_chunks",
                "embedding_table": "chunk_embeddings",
                "retrieval_mode": RETRIEVAL_MODE,
                "preview_source": "semantic_preview_runtime_smoke",
                "candidate_chunk_ids": candidate_chunk_ids,
                "candidate_embedding_ids": candidate_embedding_ids,
                "missing_embedding_chunk_ids": missing_embedding_chunk_ids,
                "embedding_model": payload.embedding_model,
                "embedding_dimension": payload.embedding_dimension,
                "query_vector_source": "caller_provided_vector",
                "ranking_boundary": RANKING_BOUNDARY,
                "persistence_boundary": PERSISTENCE_BOUNDARY,
                "source_count": len(chunks),
                "limit": payload.limit,
                "warning_count": len(warnings),
                "no_embedding_generation": True,
                "no_evidence_ledger_generation": True,
                "not_financial_advice": True,
            },
        )
    )

    return RetrievalRunResponse(
        **run,
        results=[_retrieval_candidate_from_row(row) for row in rows],
        warnings=warnings,
    )


def _retrieval_candidate_from_row(row: dict) -> RetrievalCandidateOut:
    distance = float(row["distance"])
    return RetrievalCandidateOut(
        source_id=str(row["chunk_id"]),
        source_type=row.get("source_type") or "document_chunk",
        chunk_strategy=row["chunk_strategy"],
        chunk_index=row["chunk_index"],
        text=row["chunk_text"],
        score=round(1.0 - distance, 4),
        matched_terms=[],
        metadata={
            "chunk_id": str(row["chunk_id"]),
            "embedding_id": str(row["embedding_id"]),
            "distance": distance,
            "embedding_model": row["embedding_model"],
            "embedding_dimension": row["embedding_dimension"],
            "distance_metric": row["distance_metric"],
            "source_table": "document_chunks",
            "embedding_table": "chunk_embeddings",
            "ranking_boundary": RANKING_BOUNDARY,
            "persistence_boundary": PERSISTENCE_BOUNDARY,
            "chunk_metadata_json": row.get("chunk_metadata_json") or {},
            "embedding_metadata_json": row.get("embedding_metadata_json") or {},
        },
    )
