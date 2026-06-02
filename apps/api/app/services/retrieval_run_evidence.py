from uuid import UUID, uuid4

from fastapi import HTTPException

from packages.ingestion.retrieval.lexical import _terms

from app.db import Repository
from app.schemas import (
    EvidenceLedgerCandidateIn,
    EvidenceLedgerPersistedOut,
    EvidenceLedgerPreviewRequest,
    EvidenceLedgerStoredEntryOut,
)
from app.services.evidence_ledger import preview_evidence_ledger
from app.services.run_trace import run_with_trace


def persist_evidence_ledger_from_retrieval_run(
    retrieval_run_id: UUID,
    repository: Repository,
) -> EvidenceLedgerPersistedOut:
    retrieval_run = repository.get_retrieval_run(retrieval_run_id)
    if retrieval_run is None:
        raise HTTPException(status_code=404, detail="Retrieval run not found")

    workflow_trace_id = uuid4()

    def operation(agent_run_id: UUID) -> EvidenceLedgerPersistedOut:
        preview_warnings, candidates = _candidates_from_retrieval_run(
            retrieval_run=retrieval_run,
            retrieval_run_id=retrieval_run_id,
            repository=repository,
        )
        preview = preview_evidence_ledger(
            EvidenceLedgerPreviewRequest(
                question=retrieval_run["question"],
                retrieval_results=candidates,
            )
        )
        persisted = repository.create_evidence_ledger_entries(
            preview.question,
            preview.entries,
            workflow_trace_id=workflow_trace_id,
            agent_run_id=agent_run_id,
            workflow_run_id=retrieval_run.get("workflow_run_id"),
            retrieval_run_id=retrieval_run_id,
        )
        return EvidenceLedgerPersistedOut(
            question=preview.question,
            entries=[EvidenceLedgerStoredEntryOut(**entry) for entry in persisted],
            summary=preview.summary,
            warnings=[
                *preview_warnings,
                *preview.warnings,
            ],
            stored_entry_count=len(persisted),
        )

    return run_with_trace(
        repository,
        endpoint="POST /retrieval-runs/{retrieval_run_id}/evidence-ledger",
        user_question=retrieval_run["question"],
        trace_json={
            "retrieval_run_id": str(retrieval_run_id),
            "workflow_trace_id": str(workflow_trace_id),
            "source_table": (retrieval_run.get("metadata_json") or {}).get("source_table"),
            "candidate_chunk_count": len(
                (retrieval_run.get("metadata_json") or {}).get("candidate_chunk_ids") or []
            ),
            "no_llm": True,
            "no_embeddings": True,
            "no_semantic_retrieval": True,
        },
        operation=operation,
        trace_from_result=lambda result: {
            "stored_entry_count": result.stored_entry_count,
            "supported_count": result.summary.supported_count,
            "blocked_count": result.summary.blocked_count,
        },
    )


def _candidates_from_retrieval_run(
    *,
    retrieval_run: dict,
    retrieval_run_id: UUID,
    repository: Repository,
) -> tuple[list[str], list[EvidenceLedgerCandidateIn]]:
    metadata = dict(retrieval_run.get("metadata_json") or {})
    warnings = [
        "Evidence Ledger entries were generated from a persisted retrieval_run over document_chunks.",
        "This handoff uses stored candidate_chunk_ids; it makes no LLM call, creates no embeddings, and does not perform semantic retrieval.",
        "This handoff does not judge final truth or provide financial advice.",
    ]
    if metadata.get("source_table") != "document_chunks":
        warnings.append(
            "Retrieval run is not backed by document_chunks metadata; no source chunks were loaded."
        )
        return warnings, []

    raw_document_id = metadata.get("document_id")
    if not raw_document_id:
        warnings.append("Retrieval run metadata did not include document_id.")
        return warnings, []

    try:
        document_id = UUID(str(raw_document_id))
    except ValueError:
        warnings.append("Retrieval run metadata included an invalid document_id.")
        return warnings, []

    candidate_chunk_ids = [
        str(chunk_id)
        for chunk_id in (metadata.get("candidate_chunk_ids") or [])
        if chunk_id
    ]
    if not candidate_chunk_ids:
        warnings.append("Retrieval run metadata had no candidate_chunk_ids.")
        return warnings, []

    chunks = list(repository.list_document_chunks(document_id=document_id, limit=100))
    chunks_by_id = {str(chunk["id"]): chunk for chunk in chunks}
    missing_chunk_ids = [
        chunk_id for chunk_id in candidate_chunk_ids if chunk_id not in chunks_by_id
    ]
    if missing_chunk_ids:
        warnings.append(
            "Some candidate_chunk_ids no longer resolve to document_chunks rows: "
            + ", ".join(missing_chunk_ids)
        )

    query_terms = set(_terms(retrieval_run["question"]))
    candidates: list[EvidenceLedgerCandidateIn] = []
    for chunk_id in candidate_chunk_ids:
        chunk = chunks_by_id.get(chunk_id)
        if chunk is None:
            continue
        matched_terms = sorted(query_terms.intersection(_terms(chunk["chunk_text"])))
        score = round(len(matched_terms) / max(len(query_terms), 1), 4)
        chunk_metadata = dict(chunk.get("metadata_json") or {})
        chunk_metadata.update(
            {
                "chunk_id": str(chunk["id"]),
                "document_id": str(document_id),
                "source_table": "document_chunks",
                "retrieval_run_id": str(retrieval_run_id),
                "persistence_boundary": (
                    "retrieval_run_linked_evidence_ledger_no_llm_no_embeddings"
                ),
            }
        )
        candidates.append(
            EvidenceLedgerCandidateIn(
                source_id=str(chunk["id"]),
                source_type=chunk["source_type"],
                chunk_strategy=chunk["chunk_strategy"],
                chunk_index=chunk["chunk_index"],
                text=chunk["chunk_text"],
                score=score,
                matched_terms=matched_terms,
                metadata=chunk_metadata,
            )
        )

    return warnings, candidates
