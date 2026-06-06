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


PDF_PAGE_DIAGNOSTIC_METADATA_KEYS = (
    "page_diagnostics_available",
    "layout_block_diagnostics_available",
    "extraction_scope",
    "page_text_char_counts",
    "extracted_page_count",
    "empty_page_count",
    "text_block_count",
    "image_block_count",
    "table_candidate_diagnostics_available",
    "table_candidate_count",
    "table_candidate_page_counts",
    "table_candidate_shapes",
    "table_extraction_performed",
    "default_pdf_parser_table_adapter_metadata",
    "table_adapter",
    "table_adapter_boundary",
    "table_adapter_extraction_performed",
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
    candidate_provenance = _candidate_provenance(candidates)
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
                **candidate_provenance,
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


def _candidate_provenance(candidates: list[RetrievalCandidate]) -> dict[str, object]:
    source_types = sorted(
        {candidate.source_type for candidate in candidates if candidate.source_type}
    )
    parsers = sorted(
        {
            str(candidate.metadata["parser"])
            for candidate in candidates
            if candidate.metadata.get("parser")
        }
    )
    has_pdf_candidate = "pdf" in source_types
    digital_pdf_text_extraction = any(
        candidate.metadata.get("digital_pdf_text_extraction") is True
        for candidate in candidates
    )
    robust_pdf_values = [
        candidate.metadata.get("robust_pdf_extraction")
        for candidate in candidates
        if "robust_pdf_extraction" in candidate.metadata
    ]

    provenance: dict[str, object] = {
        "candidate_source_types": source_types,
        "candidate_parsers": parsers,
        "source_provenance_boundary": "retrieval_run_candidate_chunk_metadata_only",
    }
    if has_pdf_candidate:
        provenance["digital_pdf_text_extraction"] = digital_pdf_text_extraction
        provenance["robust_pdf_extraction"] = any(
            value is True for value in robust_pdf_values
        )
        provenance.update(_first_pdf_page_diagnostics(candidates))
    return provenance


def _first_pdf_page_diagnostics(
    candidates: list[RetrievalCandidate],
) -> dict[str, object]:
    diagnostics: dict[str, object] = {}
    for key in PDF_PAGE_DIAGNOSTIC_METADATA_KEYS:
        for candidate in candidates:
            if key in candidate.metadata:
                diagnostics[key] = candidate.metadata[key]
                break
    return diagnostics
