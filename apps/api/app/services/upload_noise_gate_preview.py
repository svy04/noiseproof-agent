from app.schemas import NoiseGatePreviewRequest, UploadNoiseGatePreviewOut
from app.services.noise_gate import preview_noise_gate
from app.services.upload_evidence_preview import preview_uploaded_evidence


def preview_uploaded_noise_gate(
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
) -> UploadNoiseGatePreviewOut:
    evidence = preview_uploaded_evidence(
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
    gate = preview_noise_gate(
        NoiseGatePreviewRequest(
            question=question,
            evidence_entries=evidence.evidence.entries,
        )
    )
    warnings = [
        "Upload Noise Gate preview is preview-only and does not create Noise Gate records.",
        "Upload Noise Gate preview does not create retrieval_runs, Evidence Ledger entries, documents, chunks, reports, workflow runs, or failure cases.",
    ]

    return UploadNoiseGatePreviewOut(
        filename=filename,
        content_type=content_type,
        byte_count=len(content),
        persistence_boundary="preview_only_not_persisted",
        source_type=evidence.source_type,
        question=question,
        status=gate.decision,
        retrieval=evidence.retrieval,
        evidence=evidence.evidence,
        gate=gate,
        warnings=warnings + evidence.warnings + gate.warnings,
    )
