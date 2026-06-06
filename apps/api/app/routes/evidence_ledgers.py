from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID, uuid4

from app.db import Repository, get_repository
from app.schemas import (
    EvidenceLedgerPersistedOut,
    EvidenceLedgerPreviewOut,
    EvidenceLedgerPreviewRequest,
    EvidenceLedgerStoredEntryOut,
    FailureCaseDraftPreviewOut,
)
from app.services.evidence_quality_failure_case_draft import (
    evidence_quality_risk_reasons,
    preview_evidence_quality_failure_case_draft,
)
from app.services.evidence_ledger import preview_evidence_ledger
from app.services.run_trace import run_with_trace

router = APIRouter(prefix="/evidence-ledgers", tags=["evidence-ledgers"])


@router.post("", response_model=EvidenceLedgerPersistedOut, status_code=201)
def create_evidence_ledger(
    payload: EvidenceLedgerPreviewRequest,
    repository: Repository = Depends(get_repository),
) -> EvidenceLedgerPersistedOut:
    workflow_trace_id = uuid4()

    def operation(agent_run_id) -> EvidenceLedgerPersistedOut:
        preview = preview_evidence_ledger(payload)
        persisted = repository.create_evidence_ledger_entries(
            preview.question,
            preview.entries,
            workflow_trace_id=workflow_trace_id,
            agent_run_id=agent_run_id,
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
        trace_json={
            "retrieval_result_count": len(payload.retrieval_results),
            "workflow_trace_id": str(workflow_trace_id),
        },
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
    workflow_trace_id: UUID | None = None,
    status: str | None = None,
    repository: Repository = Depends(get_repository),
) -> list[EvidenceLedgerStoredEntryOut]:
    return [
        EvidenceLedgerStoredEntryOut(**entry)
        for entry in repository.list_evidence_ledger_entries(
            workflow_trace_id=workflow_trace_id,
            status=status,
        )
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
        operation=lambda _agent_run_id: preview_evidence_ledger(payload),
        trace_from_result=lambda result: {
            "supported_count": result.summary.supported_count,
            "contradicted_count": result.summary.contradicted_count,
            "blocked_count": result.summary.blocked_count,
        },
    )


@router.post(
    "/{entry_id}/failure-case-draft-preview",
    response_model=FailureCaseDraftPreviewOut,
)
def create_evidence_quality_failure_case_draft_preview(
    entry_id: UUID,
    repository: Repository = Depends(get_repository),
) -> FailureCaseDraftPreviewOut:
    entry = next(
        (
            row
            for row in repository.list_evidence_ledger_entries()
            if str(row.get("id")) == str(entry_id)
        ),
        None,
    )
    if entry is None:
        raise HTTPException(status_code=404, detail="evidence ledger entry not found")

    if not evidence_quality_risk_reasons(entry):
        raise HTTPException(
            status_code=409,
            detail="evidence ledger entry has no quality risk",
        )

    return preview_evidence_quality_failure_case_draft(entry)
