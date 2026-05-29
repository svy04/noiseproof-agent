from fastapi import APIRouter, Depends
from uuid import uuid4

from app.db import Repository, get_repository
from app.schemas import NoiseGatePreviewOut, NoiseGatePreviewRequest, NoiseGateStoredRecordOut
from app.services.noise_gate import preview_noise_gate
from app.services.run_trace import run_with_trace

router = APIRouter(prefix="/noise-gates", tags=["noise-gates"])


@router.post("", response_model=NoiseGateStoredRecordOut, status_code=201)
def create_noise_gate_record(
    payload: NoiseGatePreviewRequest,
    repository: Repository = Depends(get_repository),
) -> NoiseGateStoredRecordOut:
    workflow_trace_id = uuid4()

    def operation() -> NoiseGateStoredRecordOut:
        preview = preview_noise_gate(payload)
        persisted = repository.create_noise_gate_record(
            preview,
            evidence_entry_count=len(payload.evidence_entries),
            draft_claim_count=len(payload.draft_claims),
            workflow_trace_id=workflow_trace_id,
        )
        return NoiseGateStoredRecordOut(**persisted)

    return run_with_trace(
        repository,
        endpoint="POST /noise-gates",
        user_question=payload.question,
        trace_json={
            "evidence_entry_count": len(payload.evidence_entries),
            "workflow_trace_id": str(workflow_trace_id),
        },
        operation=operation,
        trace_from_result=lambda result: {
            "decision": result.decision,
            "final_response_allowed": result.final_response_allowed,
            "blocked_claim_count": len(result.blocked_claims),
            "downgraded_claim_count": len(result.downgraded_claims),
            "evidence_entry_count": result.evidence_entry_count,
            "draft_claim_count": result.draft_claim_count,
        },
    )


@router.get("", response_model=list[NoiseGateStoredRecordOut])
def list_noise_gate_records(
    repository: Repository = Depends(get_repository),
) -> list[NoiseGateStoredRecordOut]:
    return [
        NoiseGateStoredRecordOut(**record)
        for record in repository.list_noise_gate_records()
    ]


@router.post("/preview", response_model=NoiseGatePreviewOut)
def create_noise_gate_preview(
    payload: NoiseGatePreviewRequest,
    repository: Repository = Depends(get_repository),
) -> NoiseGatePreviewOut:
    return run_with_trace(
        repository,
        endpoint="POST /noise-gates/preview",
        user_question=payload.question,
        trace_json={"evidence_entry_count": len(payload.evidence_entries)},
        operation=lambda: preview_noise_gate(payload),
        trace_from_result=lambda result: {
            "decision": result.decision,
            "final_response_allowed": result.final_response_allowed,
            "blocked_claim_count": len(result.blocked_claims),
            "downgraded_claim_count": len(result.downgraded_claims),
        },
    )
