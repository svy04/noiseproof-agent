from app.schemas import ChunkPreviewRequest, UploadChunkPreviewOut
from app.services.chunk_preview import preview_chunks
from app.services.upload_preview import decode_upload_content, infer_upload_source_type


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
    inferred_source_type = infer_upload_source_type(
        source_type=source_type,
        filename=filename,
        content_type=content_type,
        warnings=warnings,
    )
    text = decode_upload_content(content, warnings)
    chunked = preview_chunks(
        ChunkPreviewRequest(
            source_type=inferred_source_type,
            content=text,
            filename=filename,
            source_uri=f"upload://{filename}" if filename else "upload://unnamed",
            max_characters=max_characters,
            overlap=overlap,
        )
    )

    return UploadChunkPreviewOut(
        filename=filename,
        content_type=content_type,
        byte_count=len(content),
        persistence_boundary="preview_only_not_persisted",
        source_type=chunked.source_type,
        parser=chunked.parser,
        profile=chunked.profile,
        parse_warnings=warnings + chunked.parse_warnings,
        failure_case_candidate=chunked.failure_case_candidate,
        strategies=chunked.strategies,
    )
