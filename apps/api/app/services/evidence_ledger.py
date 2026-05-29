from dataclasses import asdict

from packages.ingestion.evidence import create_evidence_ledger
from packages.ingestion.types import EvidenceLedgerCandidate

from app.schemas import EvidenceLedgerPreviewOut, EvidenceLedgerPreviewRequest


def preview_evidence_ledger(payload: EvidenceLedgerPreviewRequest) -> EvidenceLedgerPreviewOut:
    ledger = create_evidence_ledger(
        question=payload.question,
        candidates=[
            EvidenceLedgerCandidate(
                source_id=candidate.source_id,
                source_type=candidate.source_type,
                chunk_strategy=candidate.chunk_strategy,
                chunk_index=candidate.chunk_index,
                text=candidate.text,
                score=candidate.score,
                matched_terms=candidate.matched_terms,
                metadata=candidate.metadata,
            )
            for candidate in payload.retrieval_results
        ],
    )
    return EvidenceLedgerPreviewOut(**asdict(ledger))
