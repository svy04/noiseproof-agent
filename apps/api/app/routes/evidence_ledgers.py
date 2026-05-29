from fastapi import APIRouter

from app.schemas import EvidenceLedgerPreviewOut, EvidenceLedgerPreviewRequest
from app.services.evidence_ledger import preview_evidence_ledger

router = APIRouter(prefix="/evidence-ledgers", tags=["evidence-ledgers"])


@router.post("/preview", response_model=EvidenceLedgerPreviewOut)
def create_evidence_ledger_preview(
    payload: EvidenceLedgerPreviewRequest,
) -> EvidenceLedgerPreviewOut:
    return preview_evidence_ledger(payload)
