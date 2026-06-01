from app.schemas import (
    EvidenceLedgerCandidateIn,
    EvidenceLedgerPreviewRequest,
    UploadEvidencePreviewOut,
)
from app.services.evidence_ledger import preview_evidence_ledger
from app.services.upload_retrieval_preview import preview_uploaded_retrieval


def preview_uploaded_evidence(
    *,
    question: str,
    filename: str | None,
    content_type: str | None,
    source_type: str | None,
    content: bytes,
    strategy: str,
    top_k: int,
    max_characters: int,
    overlap: int,
) -> UploadEvidencePreviewOut:
    retrieval = preview_uploaded_retrieval(
        question=question,
        filename=filename,
        content_type=content_type,
        source_type=source_type,
        content=content,
        strategy=strategy,
        top_k=top_k,
        max_characters=max_characters,
        overlap=overlap,
    )
    evidence = preview_evidence_ledger(
        EvidenceLedgerPreviewRequest(
            question=question,
            retrieval_results=[
                EvidenceLedgerCandidateIn(**candidate.model_dump())
                for candidate in retrieval.results
            ],
        )
    )
    warnings = [
        "Upload Evidence Ledger preview is preview-only and does not create Evidence Ledger entries.",
        "Upload Evidence Ledger preview does not create retrieval_runs, documents, chunks, Noise Gate records, or reports.",
    ]

    return UploadEvidencePreviewOut(
        filename=filename,
        content_type=content_type,
        byte_count=len(content),
        persistence_boundary="preview_only_not_persisted",
        source_type=retrieval.source_type,
        question=question,
        status="blocked" if retrieval.status == "blocked" else "completed",
        retrieval=retrieval,
        evidence=evidence,
        warnings=warnings + retrieval.warnings + evidence.warnings,
    )
