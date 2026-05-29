from fastapi import APIRouter, Depends

from app.db import Repository, get_repository
from app.schemas import (
    EvidenceLedgerPersistedOut,
    EvidenceLedgerPreviewOut,
    EvidenceLedgerPreviewRequest,
    EvidenceLedgerStoredEntryOut,
)
from app.services.evidence_ledger import preview_evidence_ledger
from app.services.run_trace import run_with_trace

router = APIRouter(prefix="/evidence-ledgers", tags=["evidence-ledgers"])


@router.post("", response_model=EvidenceLedgerPersistedOut, status_code=201)
def create_evidence_ledger(
    payload: EvidenceLedgerPreviewRequest,
    repository: Repository = Depends(get_repository),
) -> EvidenceLedgerPersistedOut:
    def operation() -> EvidenceLedgerPersistedOut:
        preview = preview_evidence_ledger(payload)
        persisted = repository.create_evidence_ledger_entries(
            preview.question,
            preview.entries,
        )
        return EvidenceLedgerPersistedOut(
            question=preview.question,
            entries=[EvidenceLedgerStoredEntryOut(**entry) for entry in persisted],
            summary=preview.summary,
            warnings=preview.warnings,
            stored_entry_count=len(persisted),
        )

    return run_with_trace(
        repository,
        endpoint="POST /evidence-ledgers",
        user_question=payload.question,
        trace_json={"retrieval_result_count": len(payload.retrieval_results)},
        operation=operation,
        trace_from_result=lambda result: {
            "stored_entry_count": result.stored_entry_count,
            "supported_count": result.summary.supported_count,
            "contradicted_count": result.summary.contradicted_count,
            "blocked_count": result.summary.blocked_count,
        },
    )


@router.get("", response_model=list[EvidenceLedgerStoredEntryOut])
def list_evidence_ledger_entries(
    repository: Repository = Depends(get_repository),
) -> list[EvidenceLedgerStoredEntryOut]:
    return [
        EvidenceLedgerStoredEntryOut(**entry)
        for entry in repository.list_evidence_ledger_entries()
    ]


@router.post("/preview", response_model=EvidenceLedgerPreviewOut)
def create_evidence_ledger_preview(
    payload: EvidenceLedgerPreviewRequest,
    repository: Repository = Depends(get_repository),
) -> EvidenceLedgerPreviewOut:
    return run_with_trace(
        repository,
        endpoint="POST /evidence-ledgers/preview",
        user_question=payload.question,
        trace_json={"retrieval_result_count": len(payload.retrieval_results)},
        operation=lambda: preview_evidence_ledger(payload),
        trace_from_result=lambda result: {
            "supported_count": result.summary.supported_count,
            "contradicted_count": result.summary.contradicted_count,
            "blocked_count": result.summary.blocked_count,
        },
    )
