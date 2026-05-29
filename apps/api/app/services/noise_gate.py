from dataclasses import asdict

from packages.ingestion.noise_gate import run_noise_gate
from packages.ingestion.types import EvidenceLedgerEntry

from app.schemas import NoiseGatePreviewOut, NoiseGatePreviewRequest


def preview_noise_gate(payload: NoiseGatePreviewRequest) -> NoiseGatePreviewOut:
    result = run_noise_gate(
        question=payload.question,
        entries=[
            EvidenceLedgerEntry(
                claim=entry.claim,
                source_id=entry.source_id,
                source_type=entry.source_type,
                source_date=entry.source_date,
                evidence_span=entry.evidence_span,
                confidence=entry.confidence,
                limitation=entry.limitation,
                contradicting_source_ids=entry.contradicting_source_ids,
                status=entry.status,
                matched_terms=entry.matched_terms,
                role=entry.role,
            )
            for entry in payload.evidence_entries
        ],
        draft_claims=payload.draft_claims,
    )
    return NoiseGatePreviewOut(**asdict(result))
