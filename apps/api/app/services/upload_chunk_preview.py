from dataclasses import asdict

from app.schemas import ChunkStrategyOut, UploadChunkPreviewOut
from app.services.upload_preview import parse_uploaded_content
from packages.ingestion.chunking import compare_chunk_strategies
from packages.ingestion.types import ChunkOptions


def preview_uploaded_chunks(
    *,
    filename: str | None,
    content_type: str | None,
    source_type: str | None,
    content: bytes,
    max_characters: int,
    overlap: int,
) -> UploadChunkPreviewOut:
    warnings: list[str] = [
        "Upload chunk preview is preview-only and does not create documents, chunks, or retrieval runs.",
        "File upload preview does not claim robust PDF extraction.",
    ]
    parsed, profile = parse_uploaded_content(
        filename=filename,
        content_type=content_type,
        source_type=source_type,
        content=content,
        warnings=warnings,
    )
    strategies = compare_chunk_strategies(
        parsed,
        ChunkOptions(max_characters=max_characters, overlap=overlap),
    )

    return UploadChunkPreviewOut(
        filename=filename,
        content_type=content_type,
        byte_count=len(content),
        persistence_boundary="preview_only_not_persisted",
        source_type=parsed.source_type,
        parser=parsed.parser,
        profile=profile,
        parse_warnings=warnings + parsed.warnings,
        failure_case_candidate=(
            asdict(parsed.failure_case_candidate)
            if parsed.failure_case_candidate is not None
            else None
        ),
        strategies=[ChunkStrategyOut(**asdict(strategy)) for strategy in strategies],
    )
