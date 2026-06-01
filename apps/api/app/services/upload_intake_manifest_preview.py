from __future__ import annotations

from hashlib import sha256

from app.schemas import UploadIntakeManifestPreviewOut
from app.services.upload_preview import preview_upload


def preview_uploaded_intake_manifest(
    *,
    filename: str | None,
    content_type: str | None,
    source_type: str | None,
    content: bytes,
) -> UploadIntakeManifestPreviewOut:
    preview = preview_upload(
        filename=filename,
        content_type=content_type,
        source_type=source_type,
        content=content,
    )
    content_hash = sha256(content).hexdigest()
    source_uri = f"upload://{filename}" if filename else "upload://unnamed"
    warnings = [
        "Upload intake manifest preview is preview-only and does not create documents, file storage, chunks, or retrieval runs.",
        "This manifest is not replayable because raw uploaded bytes are not persisted.",
        "Future persistence must define retention, privacy, and replay boundaries before storing raw upload content.",
    ]

    return UploadIntakeManifestPreviewOut(
        filename=filename,
        content_type=content_type,
        byte_count=len(content),
        content_sha256=content_hash,
        source_type=preview.source_type,
        parser=preview.parser,
        profile=preview.profile,
        parse_warnings=preview.warnings,
        manifest={
            "source_uri": source_uri,
            "filename": filename,
            "content_type": content_type,
            "byte_count": len(content),
            "content_sha256": content_hash,
            "source_type": preview.source_type,
            "parser": preview.parser,
            "profile": preview.profile.model_dump(),
            "future_persistence_candidate": "uploaded_file_intake",
            "minimum_future_storage_fields": [
                "source_uri",
                "filename",
                "content_type",
                "byte_count",
                "content_sha256",
                "source_type",
                "parser",
                "profile_json",
                "retention_boundary",
            ],
        },
        storage_decision="do_not_persist_raw_upload_yet",
        replayable=False,
        persistence_boundary="preview_only_not_persisted",
        warnings=warnings + preview.warnings,
    )
