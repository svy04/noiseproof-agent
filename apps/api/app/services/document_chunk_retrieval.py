from dataclasses import asdict
import time
from uuid import UUID

from packages.ingestion.retrieval.lexical import _terms
from packages.ingestion.types import RetrievalCandidate

from app.db import Repository
from app.schemas import (
    DocumentRetrievalRunRequest,
    RetrievalRunCreate,
    RetrievalRunResponse,
)


def run_document_chunk_retrieval(
    document_id: UUID,
    payload: DocumentRetrievalRunRequest,
    repository: Repository,
) -> RetrievalRunResponse:
    started_at = time.perf_counter()
    chunks = list(repository.list_document_chunks(document_id=document_id, limit=100))
    query_terms = _terms(payload.question)
    warnings = [
        "Document retrieval uses existing document_chunks rows as the source table.",
        "This retrieval run stores candidate_chunk_ids only and does not generate Evidence Ledger entries.",
        "This retrieval run is not financial advice.",
    ]

    if not query_terms:
        warnings.append("Question produced no searchable terms.")
    if not chunks:
        warnings.append("No persisted document_chunks exist for this document.")

    candidates = _rank_chunk_candidates(
        document_id=document_id,
        chunks=chunks,
        query_terms=query_terms,
        strategy=payload.strategy,
        top_k=payload.top_k,
    )
    if chunks and not candidates:
        warnings.append(
            "No persisted document_chunks matched the question for the selected strategy."
        )

    latency_ms = max(0, round((time.perf_counter() - started_at) * 1000))
    result_count = len(candidates)
    candidate_chunk_ids = [candidate.metadata["chunk_id"] for candidate in candidates]
    run = repository.create_retrieval_run(
        RetrievalRunCreate(
            question=payload.question,
            strategy=payload.strategy,
            status="completed" if result_count else "no_results",
            latency_ms=latency_ms,
            result_count=result_count,
            hit_rate=_hit_rate(result_count, payload.top_k, candidates),
            citation_coverage=1.0 if candidates else 0.0,
            missing_evidence_count=0 if candidates else 1,
            metadata_json={
                "source_table": "document_chunks",
                "document_id": str(document_id),
                "candidate_chunk_ids": candidate_chunk_ids,
                "source_count": len(chunks),
                "top_k": payload.top_k,
                "warning_count": len(warnings),
                "persistence_boundary": (
                    "document_chunk_retrieval_run_only_no_evidence_ledger"
                ),
                "no_embeddings": True,
                "no_semantic_retrieval": True,
                "no_evidence_ledger_generation": True,
                "not_financial_advice": True,
            },
        )
    )

    return RetrievalRunResponse(
        **run,
        results=[asdict(candidate) for candidate in candidates],
        warnings=warnings,
    )


def _rank_chunk_candidates(
    *,
    document_id: UUID,
    chunks: list[dict],
    query_terms: list[str],
    strategy: str,
    top_k: int,
) -> list[RetrievalCandidate]:
    unique_query_terms = set(query_terms)
    if not unique_query_terms:
        return []

    candidates = []
    for chunk in chunks:
        if chunk.get("chunk_strategy") != strategy:
            continue
        matched_terms = sorted(unique_query_terms.intersection(_terms(chunk["chunk_text"])))
        if not matched_terms:
            continue
        metadata = dict(chunk.get("metadata_json") or {})
        metadata.update(
            {
                "chunk_id": str(chunk["id"]),
                "document_id": str(document_id),
                "source_table": "document_chunks",
                "persistence_boundary": (
                    "document_chunk_retrieval_run_only_no_evidence_ledger"
                ),
            }
        )
        candidates.append(
            RetrievalCandidate(
                source_id=str(chunk["id"]),
                source_type=chunk["source_type"],
                chunk_strategy=chunk["chunk_strategy"],
                chunk_index=chunk["chunk_index"],
                text=chunk["chunk_text"],
                score=round(len(matched_terms) / max(len(unique_query_terms), 1), 4),
                matched_terms=matched_terms,
                metadata=metadata,
            )
        )

    return sorted(
        candidates,
        key=lambda candidate: (
            candidate.score,
            len(candidate.matched_terms),
            -candidate.chunk_index,
        ),
        reverse=True,
    )[: max(1, top_k)]


def _hit_rate(
    result_count: int,
    top_k: int,
    candidates: list[RetrievalCandidate],
) -> float:
    if result_count == 0:
        return 0.0
    return round(result_count / max(min(top_k, len(candidates) or top_k), 1), 4)
