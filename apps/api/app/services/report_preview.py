from dataclasses import asdict

from packages.ingestion.reports import create_report_preview
from packages.ingestion.types import EvidenceLedgerEntry

from app.schemas import ReportPreviewOut, ReportPreviewRequest


def preview_report(payload: ReportPreviewRequest) -> ReportPreviewOut:
    preview = create_report_preview(
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
    return ReportPreviewOut(**asdict(preview))
