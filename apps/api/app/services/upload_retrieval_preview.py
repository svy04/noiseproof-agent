from packages.ingestion.retrieval import retrieve_candidates
from packages.ingestion.types import ChunkOptions, RetrievalSource

from app.schemas import UploadRetrievalPreviewOut
from app.services.upload_preview import infer_upload_source_type, parse_uploaded_content

TRADING_DRIFT_TERMS = ("buy", "sell", "target price", "매수", "매도", "목표가")


def preview_uploaded_retrieval(
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
) -> UploadRetrievalPreviewOut:
    warnings: list[str] = [
        "Upload retrieval preview is preview-only and does not create retrieval_runs.",
        "Upload retrieval preview does not create documents, chunks, Evidence Ledger entries, Noise Gate records, or reports.",
        "File upload preview does not claim robust PDF extraction.",
    ]
    inferred_source_type = infer_upload_source_type(
        source_type=source_type,
        filename=filename,
        content_type=content_type,
        warnings=warnings,
    )
    trading_boundary = _trading_advice_boundary(question)
    if trading_boundary is not None:
        warnings.append("Question drifts toward buy/sell or financial advice; retrieval preview is blocked.")
        return UploadRetrievalPreviewOut(
            filename=filename,
            content_type=content_type,
            byte_count=len(content),
            persistence_boundary="preview_only_not_persisted",
            source_type=inferred_source_type,
            question=question,
            strategy=strategy,
            status="blocked",
            result_count=0,
            hit_rate=0.0,
            citation_coverage=0.0,
            missing_evidence_count=1,
            trading_advice_boundary=trading_boundary,
            results=[],
            warnings=warnings,
        )

    parsed, _profile = parse_uploaded_content(
        filename=filename,
        content_type=content_type,
        source_type=source_type,
        content=content,
        warnings=warnings,
    )
    source_id = f"upload://{filename}" if filename else "upload://unnamed"
    result = retrieve_candidates(
        question=question,
        sources=[
            RetrievalSource(
                source_id=source_id,
                source_type=parsed.source_type,
                content=parsed.text,
                content_bytes=content,
                filename=filename,
                source_uri=source_id,
            )
        ],
        strategy=strategy,
        top_k=top_k,
        options=ChunkOptions(max_characters=max_characters, overlap=overlap),
    )

    return UploadRetrievalPreviewOut(
        filename=filename,
        content_type=content_type,
        byte_count=len(content),
        persistence_boundary="preview_only_not_persisted",
        source_type=parsed.source_type,
        question=question,
        strategy=result.strategy,
        status="completed" if result.result_count else "no_results",
        result_count=result.result_count,
        hit_rate=result.hit_rate,
        citation_coverage=result.citation_coverage,
        missing_evidence_count=result.missing_evidence_count,
        trading_advice_boundary=None,
        results=[candidate.__dict__ for candidate in result.results],
        warnings=warnings + parsed.warnings + result.warnings,
    )


def _trading_advice_boundary(question: str) -> str | None:
    lowered = (question or "").lower()
    if any(term in lowered for term in TRADING_DRIFT_TERMS):
        return "question_contains_trading_advice_drift"
    return None
