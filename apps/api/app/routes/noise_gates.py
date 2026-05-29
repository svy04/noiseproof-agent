from fastapi import APIRouter, Depends

from app.db import Repository, get_repository
from app.schemas import NoiseGatePreviewOut, NoiseGatePreviewRequest
from app.services.noise_gate import preview_noise_gate
from app.services.run_trace import run_with_trace

router = APIRouter(prefix="/noise-gates", tags=["noise-gates"])


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
