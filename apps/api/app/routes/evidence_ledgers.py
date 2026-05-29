from fastapi import APIRouter, Depends

from app.db import Repository, get_repository
from app.schemas import EvidenceLedgerPreviewOut, EvidenceLedgerPreviewRequest
from app.services.evidence_ledger import preview_evidence_ledger
from app.services.run_trace import run_with_trace

router = APIRouter(prefix="/evidence-ledgers", tags=["evidence-ledgers"])


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
