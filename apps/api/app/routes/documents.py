import re
from collections import deque
from datetime import UTC, datetime
from hashlib import sha256
from secrets import compare_digest
from time import monotonic
from urllib.parse import unquote
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, File, Form, Header, HTTPException, Request, UploadFile
from fastapi.responses import Response

from app.db import Repository, get_repository
from app.schemas import (
    ChunkPreviewOut,
    ChunkPreviewRequest,
    DocumentChunkCreate,
    DocumentChunkOut,
    DocumentChunkRequest,
    DocumentCreate,
    DocumentOut,
    DocumentProfileOut,
    DocumentProfileRequest,
    DocumentRetrievalRunRequest,
    ParsePreviewOut,
    ParsePreviewRequest,
    RawFileDownloadApprovalCreate,
    RawFileDownloadApprovalOut,
    RawFileDownloadEventCreate,
    RawFileDownloadEventOut,
    RawFileDownloadReadinessOut,
    RawFileScanResultCreate,
    RawFileScanResultOut,
    RetrievalRunResponse,
    SemanticRetrievalPreviewOut,
    SemanticRetrievalPreviewRequest,
    SemanticRetrievalRunRequest,
    UploadChunkPreviewOut,
    UploadChunkPersistenceOut,
    UploadEvidencePreviewOut,
    UploadFailureCaseDraftPreviewOut,
    UploadIntakeManifestPreviewOut,
    UploadedFileIntakeManifestCreate,
    UploadedFileIntakeManifestOut,
    UploadedRawFileCreate,
    UploadedRawFileOut,
    UploadNoiseGatePreviewOut,
    UploadPreviewOut,
    UploadReportPreviewOut,
    UploadRetrievalPreviewOut,
)
from app.settings import Settings, get_settings
from app.services.chunk_preview import preview_chunks
from app.services.document_chunk_retrieval import run_document_chunk_retrieval
from app.services.document_profiler import profile_document
from app.services.parse_preview import preview_parse
from app.services.raw_file_scan_execution import (
    get_scanner_adapter,
    scan_uploaded_raw_file,
)
from app.services.run_trace import run_with_trace
from app.services.semantic_retrieval_preview import preview_semantic_retrieval
from app.services.semantic_retrieval_run import run_semantic_retrieval
from app.services.upload_chunk_preview import preview_uploaded_chunks
from app.services.upload_evidence_preview import preview_uploaded_evidence
from app.services.upload_failure_case_draft_preview import preview_uploaded_failure_case_draft
from app.services.upload_intake_manifest_preview import preview_uploaded_intake_manifest
from app.services.upload_noise_gate_preview import preview_uploaded_noise_gate
from app.services.upload_preview import preview_upload
from app.services.upload_report_preview import preview_uploaded_report
from app.services.upload_retrieval_preview import preview_uploaded_retrieval
from packages.ingestion.scanning import ScannerAdapter

router = APIRouter(prefix="/documents", tags=["documents"])


RAW_UPLOAD_GUARDED_DOWNLOAD_BOUNDARY = (
    "raw_upload_quarantine_db_bytea_guarded_download_endpoint"
)
DOWNLOAD_BLOCK_DETAIL = "latest clean scan result required before raw file download"
DOWNLOAD_APPROVAL_BLOCK_DETAIL = (
    "active download approval required before raw file download"
)
DOWNLOAD_WITH_APPROVAL_BOUNDARY = (
    "scan_first_latest_clean_result_and_active_approval_required"
)
DOWNLOAD_RATE_LIMIT_DETAIL = "raw file download rate limit exceeded"
DOWNLOAD_OPERATOR_TOKEN_DETAIL = "operator token required before raw file download"
DOWNLOAD_AUTHORIZATION_BOUNDARY = "local_v0_no_auth_not_production"
DOWNLOAD_OPERATOR_TOKEN_AUTHORIZATION_BOUNDARY = (
    "local_v0_operator_token_header_not_production"
)
DOWNLOAD_RATE_LIMIT_BOUNDARY = "local_v0_in_memory_fixed_window_not_production"
DOWNLOAD_RATE_LIMIT_ATTEMPTS = 5
DOWNLOAD_RATE_LIMIT_WINDOW_SECONDS = 60.0
DOWNLOAD_FILENAME_BOUNDARY = (
    "local_v0_content_disposition_filename_safety_not_production"
)
DOWNLOAD_READINESS_BOUNDARY = "download_readiness_preflight_no_raw_bytes_not_authorization"
DOWNLOAD_FILENAME_MAX_LENGTH = 120
SIGNATURE_VALIDATION_BOUNDARY = "local_v0_magic_prefix_allowlist_not_production"
EXTENSION_ALLOWLIST_BOUNDARY = "local_v0_extension_allowlist_not_production"
ALLOWED_RAW_FILE_EXTENSIONS = {
    ".csv",
    ".htm",
    ".html",
    ".markdown",
    ".md",
    ".pdf",
    ".txt",
}
PDF_PAGE_DIAGNOSTIC_METADATA_KEYS = (
    "page_diagnostics_available",
    "layout_block_diagnostics_available",
    "extraction_scope",
    "page_text_char_counts",
    "extracted_page_count",
    "empty_page_count",
    "text_block_count",
    "image_block_count",
)
SOURCE_TYPE_EXTENSIONS = {
    "csv": {".csv"},
    "html": {".html", ".htm"},
    "markdown": {".md", ".markdown", ".txt"},
    "md": {".md", ".markdown", ".txt"},
    "pdf": {".pdf"},
    "text": {".txt"},
    "txt": {".txt"},
}
DANGEROUS_INNER_EXTENSIONS = {
    ".bat",
    ".cmd",
    ".com",
    ".dll",
    ".exe",
    ".js",
    ".php",
    ".ps1",
    ".sh",
    ".vbs",
}
_download_attempt_windows: dict[tuple[str, str], deque[float]] = {}


def _safe_download_filename(filename: str | None, raw_file_id: UUID) -> str:
    fallback = f"raw-file-{raw_file_id}.bin"
    if not filename:
        return fallback
    decoded = unquote(filename)
    candidate = decoded.replace("\\", "/").split("/")[-1].strip()
    candidate = re.sub(r"[^A-Za-z0-9._-]+", "_", candidate).strip("._-")
    if not candidate:
        return fallback
    return _limit_download_filename(candidate, fallback)


def _limit_download_filename(candidate: str, fallback: str) -> str:
    if len(candidate) <= DOWNLOAD_FILENAME_MAX_LENGTH:
        return candidate

    stem = candidate
    extension = ""
    if "." in candidate:
        possible_stem, possible_extension = candidate.rsplit(".", 1)
        if possible_stem and re.fullmatch(r"[A-Za-z0-9]{1,16}", possible_extension):
            stem = possible_stem
            extension = f".{possible_extension}"

    max_stem_length = DOWNLOAD_FILENAME_MAX_LENGTH - len(extension)
    trimmed_stem = stem[:max_stem_length].rstrip("._-")
    if not trimmed_stem:
        return fallback
    return f"{trimmed_stem}{extension}"


def _content_type_for_download(content_type: str | None) -> str:
    if not content_type:
        return "application/octet-stream"
    return content_type


def _metadata_datetime(value: object) -> object:
    if isinstance(value, datetime):
        return value.isoformat().replace("+00:00", "Z")
    return value


def _pdf_page_diagnostic_metadata(metadata: dict | None) -> dict:
    source = metadata or {}
    return {
        key: source[key]
        for key in PDF_PAGE_DIAGNOSTIC_METADATA_KEYS
        if key in source
    }


def _download_rate_limit_client_host(request: Request) -> str:
    if request.client is None:
        return "unknown-client"
    return request.client.host or "unknown-client"


def _consume_download_attempt(raw_file_id: UUID, request: Request) -> bool:
    key = (str(raw_file_id), _download_rate_limit_client_host(request))
    now = monotonic()
    attempts = _download_attempt_windows.setdefault(key, deque())
    while attempts and now - attempts[0] >= DOWNLOAD_RATE_LIMIT_WINDOW_SECONDS:
        attempts.popleft()
    if len(attempts) >= DOWNLOAD_RATE_LIMIT_ATTEMPTS:
        return False
    attempts.append(now)
    return True


def _raw_file_download_authorization_boundary(settings: Settings) -> str:
    if settings.raw_file_download_operator_token:
        return DOWNLOAD_OPERATOR_TOKEN_AUTHORIZATION_BOUNDARY
    return DOWNLOAD_AUTHORIZATION_BOUNDARY


def _operator_token_allows_download(
    *,
    settings: Settings,
    operator_token: str | None,
) -> bool:
    configured_token = settings.raw_file_download_operator_token
    if not configured_token:
        return True
    if operator_token is None:
        return False
    return compare_digest(operator_token, configured_token)


def _record_raw_file_download_event(
    *,
    repository: Repository,
    raw_file_id: UUID,
    latest_scan_result: dict | None,
    download_result: str,
    blocked_reason: str | None,
    http_status_code: int,
    authorization_boundary: str = DOWNLOAD_AUTHORIZATION_BOUNDARY,
    metadata_json: dict | None = None,
) -> dict:
    payload = RawFileDownloadEventCreate(
        raw_file_id=raw_file_id,
        latest_scan_result_id=(
            latest_scan_result.get("id") if latest_scan_result is not None else None
        ),
        download_result=download_result,
        blocked_reason=blocked_reason,
        http_status_code=http_status_code,
        authorization_boundary=authorization_boundary,
        rate_limit_boundary=DOWNLOAD_RATE_LIMIT_BOUNDARY,
        filename_boundary=DOWNLOAD_FILENAME_BOUNDARY,
        client_host_boundary="local_request_client_host_not_identity",
        metadata_json=metadata_json or {},
    )
    return repository.create_raw_file_download_event(payload)


def _readiness_check(
    name: str,
    status: str,
    detail: str,
    boundary: str | None = None,
) -> dict:
    return {
        "name": name,
        "status": status,
        "detail": detail,
        "boundary": boundary,
    }


def _build_raw_file_download_readiness(
    *,
    raw_file_id: UUID,
    repository: Repository,
    now: datetime,
    authorization_boundary: str = DOWNLOAD_AUTHORIZATION_BOUNDARY,
) -> dict | None:
    raw_file = repository.get_uploaded_raw_file_for_scan(raw_file_id)
    if raw_file is None:
        return None

    checks = [
        _readiness_check(
            "raw_file_exists",
            "passed",
            "uploaded raw file metadata exists",
            "raw_upload_quarantine_db_bytea_guarded_download_endpoint",
        )
    ]
    latest_results = list(
        repository.list_raw_file_scan_results(raw_file_id=raw_file_id, limit=1)
    )
    latest_result = latest_results[0] if latest_results else None
    latest_scan_result_id = latest_result.get("id") if latest_result else None

    if (
        latest_result is None
        or latest_result.get("scan_status") != "completed"
        or latest_result.get("scan_verdict") != "clean"
    ):
        checks.append(
            _readiness_check(
                "latest_clean_scan",
                "failed",
                DOWNLOAD_BLOCK_DETAIL,
                "scan_first_latest_clean_result_required",
            )
        )
        checks.append(
            _readiness_check(
                "quarantine_status",
                "skipped",
                "quarantine status is not evaluated until a latest clean scan exists",
            )
        )
        checks.append(
            _readiness_check(
                "active_download_approval",
                "skipped",
                "approval is not evaluated until a latest clean scan exists",
                "local_v0_manual_operator_approval_not_production_auth",
            )
        )
        return {
            "raw_file_id": raw_file_id,
            "decision": "blocked",
            "blocked_reason": (
                "missing_clean_scan" if latest_result is None else "latest_scan_not_clean"
            ),
            "http_status_code_if_download_attempted": 409,
            "latest_scan_result_id": latest_scan_result_id,
            "active_approval_id": None,
            "approval_boundary": None,
            "identity_boundary": None,
            "raw_bytes_returned": False,
            "rate_limit_consumed": False,
            "readiness_boundary": DOWNLOAD_READINESS_BOUNDARY,
            "authorization_boundary": authorization_boundary,
            "rate_limit_boundary": DOWNLOAD_RATE_LIMIT_BOUNDARY,
            "checks": checks,
        }

    checks.append(
        _readiness_check(
            "latest_clean_scan",
            "passed",
            "latest scan result is completed / clean",
            "scan_first_latest_clean_result_required",
        )
    )

    if raw_file.get("quarantine_status") != "stored_quarantined":
        checks.append(
            _readiness_check(
                "quarantine_status",
                "failed",
                "raw file quarantine status does not allow controlled download",
            )
        )
        checks.append(
            _readiness_check(
                "active_download_approval",
                "skipped",
                "approval is not evaluated until quarantine status allows download",
                "local_v0_manual_operator_approval_not_production_auth",
            )
        )
        return {
            "raw_file_id": raw_file_id,
            "decision": "blocked",
            "blocked_reason": "quarantine_status_blocked",
            "http_status_code_if_download_attempted": 409,
            "latest_scan_result_id": latest_scan_result_id,
            "active_approval_id": None,
            "approval_boundary": None,
            "identity_boundary": None,
            "raw_bytes_returned": False,
            "rate_limit_consumed": False,
            "readiness_boundary": DOWNLOAD_READINESS_BOUNDARY,
            "authorization_boundary": authorization_boundary,
            "rate_limit_boundary": DOWNLOAD_RATE_LIMIT_BOUNDARY,
            "checks": checks,
        }

    checks.append(
        _readiness_check(
            "quarantine_status",
            "passed",
            "raw file remains in stored_quarantined status",
            "raw_upload_quarantine_db_bytea_guarded_download_endpoint",
        )
    )
    active_approval = repository.find_active_raw_file_download_approval(
        raw_file_id=raw_file_id,
        latest_scan_result_id=latest_result["id"],
        now=now,
    )
    if active_approval is None:
        matching_approvals = [
            approval
            for approval in repository.list_raw_file_download_approvals(
                raw_file_id=raw_file_id,
                limit=100,
            )
            if str(approval.get("latest_scan_result_id")) == str(latest_result["id"])
        ]
        checks.append(
            _readiness_check(
                "active_download_approval",
                "failed",
                DOWNLOAD_APPROVAL_BLOCK_DETAIL,
                "local_v0_manual_operator_approval_not_production_auth",
            )
        )
        return {
            "raw_file_id": raw_file_id,
            "decision": "blocked",
            "blocked_reason": (
                "revoked_or_expired_download_approval"
                if matching_approvals
                else "missing_download_approval"
            ),
            "http_status_code_if_download_attempted": 409,
            "latest_scan_result_id": latest_scan_result_id,
            "active_approval_id": None,
            "approval_boundary": None,
            "identity_boundary": None,
            "raw_bytes_returned": False,
            "rate_limit_consumed": False,
            "readiness_boundary": DOWNLOAD_READINESS_BOUNDARY,
            "authorization_boundary": authorization_boundary,
            "rate_limit_boundary": DOWNLOAD_RATE_LIMIT_BOUNDARY,
            "checks": checks,
        }

    checks.append(
        _readiness_check(
            "active_download_approval",
            "passed",
            "active local manual approval matches the latest clean scan result",
            active_approval.get("approval_boundary"),
        )
    )
    return {
        "raw_file_id": raw_file_id,
        "decision": "allowed",
        "blocked_reason": None,
        "http_status_code_if_download_attempted": 200,
        "latest_scan_result_id": latest_scan_result_id,
        "active_approval_id": active_approval.get("id"),
        "approval_boundary": active_approval.get("approval_boundary"),
        "identity_boundary": active_approval.get("identity_boundary"),
        "raw_bytes_returned": False,
        "rate_limit_consumed": False,
        "readiness_boundary": DOWNLOAD_READINESS_BOUNDARY,
        "authorization_boundary": authorization_boundary,
        "rate_limit_boundary": DOWNLOAD_RATE_LIMIT_BOUNDARY,
        "checks": checks,
    }


def _validate_raw_file_extension(
    *,
    filename: str | None,
    source_type: str | None,
    content_type: str | None,
) -> dict:
    declared_source_type = (source_type or "unknown").strip().lower() or "unknown"
    client_filename = filename or ""
    decoded_filename = unquote(client_filename)
    basename = decoded_filename.replace("\\", "/").split("/")[-1].strip()
    extensions = _filename_extensions(basename)
    normalized_extension = extensions[-1] if extensions else ""
    decision, block_reason = _extension_allowlist_decision(
        declared_source_type=declared_source_type,
        decoded_filename=decoded_filename,
        normalized_extension=normalized_extension,
        extensions=extensions,
    )
    warnings = [
        f"extension_boundary: {EXTENSION_ALLOWLIST_BOUNDARY}",
        f"declared_source_type: {declared_source_type}",
        f"declared_content_type: {content_type or 'unknown'}",
        f"client_filename: {client_filename or 'unknown'}",
        f"decoded_filename: {decoded_filename or 'unknown'}",
        f"client_filename_extension: {normalized_extension or 'none'}",
        f"extension_decision: {decision}",
        "Content-Type header can be spoofed; local extension validation treats it as metadata only.",
        "Extension validation is local v0 and should not be used on its own.",
    ]
    if client_filename != decoded_filename:
        warnings.append("filename was URL-decoded before extension validation")
    if "\\" in decoded_filename or "/" in decoded_filename:
        warnings.append("path components ignored before extension validation")
    if len(extensions) > 1:
        warnings.append("double extension detected before extension validation")

    return {
        "accepted": decision == "allowed",
        "block_reason": block_reason,
        "declared_source_type": declared_source_type,
        "declared_content_type": content_type or "unknown",
        "client_filename": client_filename or "unknown",
        "decoded_filename": decoded_filename or "unknown",
        "client_filename_extension": normalized_extension or "none",
        "extension_decision": decision,
        "extension_boundary": EXTENSION_ALLOWLIST_BOUNDARY,
        "warnings": warnings,
    }


def _filename_extensions(basename: str) -> list[str]:
    parts = basename.lower().split(".")
    if len(parts) < 2:
        return []
    return [f".{part}" for part in parts[1:] if part]


def _extension_allowlist_decision(
    *,
    declared_source_type: str,
    decoded_filename: str,
    normalized_extension: str,
    extensions: list[str],
) -> tuple[str, str | None]:
    if "\x00" in decoded_filename:
        return "blocked", "filename contains null byte"
    if not normalized_extension:
        return "missing", "missing filename extension"
    if normalized_extension not in ALLOWED_RAW_FILE_EXTENSIONS:
        return "blocked", "filename extension not allowed"
    if any(
        extension in DANGEROUS_INNER_EXTENSIONS for extension in extensions[:-1]
    ):
        return "blocked", "suspicious double extension"

    expected_extensions = SOURCE_TYPE_EXTENSIONS.get(declared_source_type)
    if expected_extensions is not None and normalized_extension not in expected_extensions:
        return "mismatch", "filename extension source_type mismatch"
    return "allowed", None


def _validate_raw_file_signature(
    *,
    source_type: str | None,
    content_type: str | None,
    content: bytes,
) -> dict:
    declared_source_type = (source_type or "unknown").strip().lower() or "unknown"
    detected_signature_type, confidence, detection_warnings = _detect_signature_type(
        content,
        declared_source_type=declared_source_type,
    )
    warnings = [
        f"signature_boundary: {SIGNATURE_VALIDATION_BOUNDARY}",
        f"declared_source_type: {declared_source_type}",
        f"declared_content_type: {content_type or 'unknown'}",
        f"detected_signature_type: {detected_signature_type}",
        f"signature_confidence: {confidence}",
        "Content-Type header can be spoofed; local signature validation treats it as metadata only.",
        "File signature validation is local v0 and should not be used on its own.",
        *detection_warnings,
    ]

    accepted, block_reason = _signature_validation_decision(
        declared_source_type=declared_source_type,
        detected_signature_type=detected_signature_type,
    )
    result = {
        "accepted": accepted,
        "block_reason": block_reason,
        "declared_source_type": declared_source_type,
        "declared_content_type": content_type or "unknown",
        "detected_signature_type": detected_signature_type,
        "signature_confidence": confidence,
        "signature_boundary": SIGNATURE_VALIDATION_BOUNDARY,
        "warnings": warnings,
    }
    return result


def _detect_signature_type(
    content: bytes,
    *,
    declared_source_type: str,
) -> tuple[str, str, list[str]]:
    prefix = content[:4096]
    if prefix.startswith(b"%PDF-"):
        return "pdf", "high", []
    if _has_binary_control_bytes(prefix):
        return "binary", "medium", ["binary control-byte signal present"]

    text = prefix.decode("utf-8", errors="ignore").lstrip("\ufeff\r\n\t ")
    lowered = text[:512].lower()
    if lowered.startswith("<!doctype html") or "<html" in lowered:
        return "html", "medium", []
    if declared_source_type == "markdown" and text.strip():
        return "markdown", "low", ["text-like markdown signature only"]
    if "," in text and "\n" in text:
        return "csv", "medium", []
    if text.strip():
        return "text", "low", ["text-like signature without a stronger local v0 match"]
    return "unknown", "low", ["empty or unknown signature prefix"]


def _has_binary_control_bytes(prefix: bytes) -> bool:
    allowed_controls = {9, 10, 12, 13}
    return any(byte < 32 and byte not in allowed_controls for byte in prefix)


def _signature_validation_decision(
    *,
    declared_source_type: str,
    detected_signature_type: str,
) -> tuple[bool, str | None]:
    if detected_signature_type == "binary":
        return False, "unsupported binary signature"
    if declared_source_type == "pdf" and detected_signature_type != "pdf":
        return False, "file signature mismatch"
    if declared_source_type == "html" and detected_signature_type != "html":
        return False, "file signature mismatch"
    if declared_source_type in {"csv", "markdown"}:
        return detected_signature_type in {
            declared_source_type,
            "csv",
            "markdown",
            "text",
        }, None
    if declared_source_type in {"unknown", "txt", "text"}:
        return detected_signature_type in {"csv", "markdown", "html", "text"}, None
    return detected_signature_type != "unknown", None


@router.post("", response_model=DocumentOut, status_code=201)
def create_document(
    payload: DocumentCreate,
    repository: Repository = Depends(get_repository),
) -> dict:
    return repository.create_document(payload)


@router.get("", response_model=list[DocumentOut])
def list_documents(repository: Repository = Depends(get_repository)) -> list[dict]:
    return list(repository.list_documents())


@router.post("/{document_id}/chunks", response_model=DocumentChunkOut, status_code=201)
def create_document_chunk(
    document_id: UUID,
    payload: DocumentChunkRequest,
    repository: Repository = Depends(get_repository),
) -> dict:
    return repository.create_document_chunk(
        DocumentChunkCreate(document_id=document_id, **payload.model_dump())
    )


@router.get("/{document_id}/chunks", response_model=list[DocumentChunkOut])
def list_document_chunks(
    document_id: UUID,
    limit: int = 20,
    repository: Repository = Depends(get_repository),
) -> list[dict]:
    return list(repository.list_document_chunks(document_id=document_id, limit=limit))


@router.post(
    "/{document_id}/retrieval-runs",
    response_model=RetrievalRunResponse,
    status_code=201,
)
def create_document_retrieval_run(
    document_id: UUID,
    payload: DocumentRetrievalRunRequest,
    repository: Repository = Depends(get_repository),
) -> RetrievalRunResponse:
    return run_document_chunk_retrieval(document_id, payload, repository)


@router.post(
    "/{document_id}/semantic-retrieval-preview",
    response_model=SemanticRetrievalPreviewOut,
)
def semantic_retrieval_preview(
    document_id: UUID,
    payload: SemanticRetrievalPreviewRequest,
    repository: Repository = Depends(get_repository),
) -> SemanticRetrievalPreviewOut:
    return run_with_trace(
        repository,
        endpoint="POST /documents/{document_id}/semantic-retrieval-preview",
        user_question=payload.question,
        trace_json={
            "document_id": str(document_id),
            "retrieval_mode": "semantic_preview",
            "persistence_boundary": "preview_only_not_persisted",
            "query_vector_source": "caller_provided_vector",
        },
        operation=lambda _agent_run_id: preview_semantic_retrieval(
            document_id=document_id,
            payload=payload,
            repository=repository,
        ),
    )


@router.post(
    "/{document_id}/semantic-retrieval-runs",
    response_model=RetrievalRunResponse,
    status_code=201,
)
def create_semantic_retrieval_run(
    document_id: UUID,
    payload: SemanticRetrievalRunRequest,
    repository: Repository = Depends(get_repository),
) -> RetrievalRunResponse:
    return run_with_trace(
        repository,
        endpoint="POST /documents/{document_id}/semantic-retrieval-runs",
        user_question=payload.question,
        trace_json={
            "document_id": str(document_id),
            "retrieval_mode": "semantic_persisted",
            "persistence_boundary": "semantic_retrieval_run_only_no_evidence_ledger",
            "query_vector_source": "caller_provided_vector",
        },
        operation=lambda _agent_run_id: run_semantic_retrieval(
            document_id=document_id,
            payload=payload,
            repository=repository,
        ),
    )


@router.post("/profile", response_model=DocumentProfileOut)
def profile_document_text(
    payload: DocumentProfileRequest,
    repository: Repository = Depends(get_repository),
) -> DocumentProfileOut:
    def operation(_agent_run_id) -> DocumentProfileOut:
        return profile_document(payload)

    return run_with_trace(
        repository,
        endpoint="POST /documents/profile",
        user_question=f"profile document: {payload.source_type}",
        trace_json={"source_type": payload.source_type},
        operation=operation,
    )


@router.post("/parse-preview", response_model=ParsePreviewOut)
def parse_document_preview(
    payload: ParsePreviewRequest,
    repository: Repository = Depends(get_repository),
) -> ParsePreviewOut:
    return run_with_trace(
        repository,
        endpoint="POST /documents/parse-preview",
        user_question=f"parse preview: {payload.source_type}",
        trace_json={"source_type": payload.source_type},
        operation=lambda _agent_run_id: preview_parse(payload),
    )


@router.post("/upload-preview", response_model=UploadPreviewOut)
async def upload_document_preview(
    file: UploadFile = File(...),
    source_type: str | None = Form(default=None),
    repository: Repository = Depends(get_repository),
) -> UploadPreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-preview",
        user_question=f"upload preview: {source_type or file.filename or 'unknown'}",
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "persistence_boundary": "preview_only_not_persisted",
        },
        operation=lambda _agent_run_id: preview_upload(
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
        ),
    )


@router.post("/upload-intake-manifest-preview", response_model=UploadIntakeManifestPreviewOut)
async def upload_document_intake_manifest_preview(
    file: UploadFile = File(...),
    source_type: str | None = Form(default=None),
    repository: Repository = Depends(get_repository),
) -> UploadIntakeManifestPreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-intake-manifest-preview",
        user_question=f"upload intake manifest preview: {source_type or file.filename or 'unknown'}",
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "persistence_boundary": "preview_only_not_persisted",
        },
        operation=lambda _agent_run_id: preview_uploaded_intake_manifest(
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
        ),
    )


@router.post(
    "/upload-intake-manifests",
    response_model=UploadedFileIntakeManifestOut,
    status_code=201,
)
async def upload_document_intake_manifest(
    file: UploadFile = File(...),
    source_type: str | None = Form(default=None),
    repository: Repository = Depends(get_repository),
) -> dict:
    content = await file.read()

    def operation(_agent_run_id) -> dict:
        preview = preview_uploaded_intake_manifest(
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
        )
        payload = UploadedFileIntakeManifestCreate(
            content_sha256=preview.content_sha256,
            filename=preview.filename,
            source_type=preview.source_type,
            content_type=preview.content_type,
            size_bytes=preview.byte_count,
            parser=preview.parser,
            profile_json=preview.profile.model_dump(),
            storage_decision=preview.storage_decision,
            replayable=preview.replayable,
            persistence_boundary="manifest_only_no_raw_file_storage",
            warnings_json=preview.warnings,
        )
        return repository.create_uploaded_file_intake_manifest(payload)

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-intake-manifests",
        user_question=f"upload intake manifest persist: {source_type or file.filename or 'unknown'}",
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "persistence_boundary": "manifest_only_no_raw_file_storage",
            "raw_file_storage": False,
        },
        operation=operation,
    )


@router.get(
    "/upload-intake-manifests",
    response_model=list[UploadedFileIntakeManifestOut],
)
def list_upload_document_intake_manifests(
    limit: int = 20,
    repository: Repository = Depends(get_repository),
) -> list[dict]:
    return list(repository.list_uploaded_file_intake_manifests(limit=limit))


@router.post(
    "/upload-raw-files",
    response_model=UploadedRawFileOut,
    status_code=201,
)
async def upload_document_raw_file(
    file: UploadFile = File(...),
    source_type: str | None = Form(default=None),
    repository: Repository = Depends(get_repository),
    settings: Settings = Depends(get_settings),
) -> dict:
    content = await file.read()
    byte_count = len(content)
    if byte_count > settings.max_raw_upload_bytes:
        raise HTTPException(
            status_code=413,
            detail=(
                f"raw upload size {byte_count} exceeds max_raw_upload_bytes "
                f"{settings.max_raw_upload_bytes}"
            ),
        )

    extension_result = _validate_raw_file_extension(
        filename=file.filename,
        source_type=source_type,
        content_type=file.content_type,
    )
    if not extension_result["accepted"]:
        raise HTTPException(
            status_code=415,
            detail={
                "block_reason": extension_result["block_reason"],
                "declared_source_type": extension_result["declared_source_type"],
                "declared_content_type": extension_result["declared_content_type"],
                "client_filename": extension_result["client_filename"],
                "decoded_filename": extension_result["decoded_filename"],
                "client_filename_extension": extension_result[
                    "client_filename_extension"
                ],
                "extension_decision": extension_result["extension_decision"],
                "extension_boundary": extension_result["extension_boundary"],
                "warnings": extension_result["warnings"],
            },
        )

    signature_result = _validate_raw_file_signature(
        source_type=source_type,
        content_type=file.content_type,
        content=content,
    )
    if not signature_result["accepted"]:
        raise HTTPException(
            status_code=415,
            detail={
                "block_reason": signature_result["block_reason"],
                "declared_source_type": signature_result["declared_source_type"],
                "declared_content_type": signature_result["declared_content_type"],
                "detected_signature_type": signature_result["detected_signature_type"],
                "signature_confidence": signature_result["signature_confidence"],
                "signature_boundary": signature_result["signature_boundary"],
                "warnings": signature_result["warnings"],
            },
        )

    warnings = [
        "Raw upload storage is quarantine-only and stores bytes in PostgreSQL bytea.",
        "The original filename is recorded as metadata only and is not used as a storage key.",
        "Raw byte retrieval requires the explicit scan-first download endpoint and a latest clean scan result.",
        "No malware scan completeness, robust PDF extraction, parsing guarantee, hosted deployment evidence, or production authorization is claimed.",
        *extension_result["warnings"],
        *signature_result["warnings"],
    ]
    payload = UploadedRawFileCreate(
        content_sha256=sha256(content).hexdigest(),
        storage_key=uuid4().hex,
        filename=file.filename,
        source_type=source_type or "unknown",
        content_type=file.content_type,
        size_bytes=byte_count,
        storage_backend="postgres_bytea",
        quarantine_status="stored_quarantined",
        persistence_boundary=RAW_UPLOAD_GUARDED_DOWNLOAD_BOUNDARY,
        raw_file_storage=True,
        raw_bytes=content,
        warnings_json=warnings,
    )
    return repository.create_uploaded_raw_file(payload)


@router.get(
    "/upload-raw-files",
    response_model=list[UploadedRawFileOut],
)
def list_upload_document_raw_files(
    limit: int = 20,
    repository: Repository = Depends(get_repository),
) -> list[dict]:
    return list(repository.list_uploaded_raw_files(limit=limit))


@router.post(
    "/upload-raw-files/{raw_file_id}/scan-results",
    response_model=RawFileScanResultOut,
    status_code=201,
)
def create_upload_raw_file_scan_result(
    raw_file_id: UUID,
    payload: RawFileScanResultCreate,
    repository: Repository = Depends(get_repository),
) -> dict:
    if payload.raw_file_id != raw_file_id:
        raise HTTPException(
            status_code=400,
            detail="raw_file_id path/body mismatch",
        )
    return repository.create_raw_file_scan_result(payload)


@router.get(
    "/upload-raw-files/{raw_file_id}/scan-results",
    response_model=list[RawFileScanResultOut],
)
def list_upload_raw_file_scan_results(
    raw_file_id: UUID,
    scan_status: str | None = None,
    scan_verdict: str | None = None,
    limit: int = 20,
    repository: Repository = Depends(get_repository),
) -> list[dict]:
    return list(
        repository.list_raw_file_scan_results(
            raw_file_id=raw_file_id,
            scan_status=scan_status,
            scan_verdict=scan_verdict,
            limit=limit,
        )
    )


@router.post(
    "/upload-raw-files/{raw_file_id}/scan",
    response_model=RawFileScanResultOut,
    status_code=201,
)
def execute_upload_raw_file_scan(
    raw_file_id: UUID,
    repository: Repository = Depends(get_repository),
    settings: Settings = Depends(get_settings),
    scanner: ScannerAdapter = Depends(get_scanner_adapter),
) -> dict:
    result = scan_uploaded_raw_file(
        raw_file_id,
        repository=repository,
        scanner=scanner,
        settings=settings,
    )
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="uploaded raw file not found",
        )
    return result


@router.get(
    "/upload-raw-files/{raw_file_id}/download-events",
    response_model=list[RawFileDownloadEventOut],
)
def list_upload_raw_file_download_events(
    raw_file_id: UUID,
    limit: int = 20,
    repository: Repository = Depends(get_repository),
) -> list[dict]:
    return list(
        repository.list_raw_file_download_events(
            raw_file_id=raw_file_id,
            limit=limit,
        )
    )


@router.post(
    "/upload-raw-files/{raw_file_id}/download-approvals",
    response_model=RawFileDownloadApprovalOut,
    status_code=201,
)
def create_upload_raw_file_download_approval(
    raw_file_id: UUID,
    payload: RawFileDownloadApprovalCreate,
    repository: Repository = Depends(get_repository),
) -> dict:
    if payload.raw_file_id != raw_file_id:
        raise HTTPException(
            status_code=400,
            detail="raw_file_id path/body mismatch",
        )
    return repository.create_raw_file_download_approval(payload)


@router.get(
    "/upload-raw-files/{raw_file_id}/download-approvals",
    response_model=list[RawFileDownloadApprovalOut],
)
def list_upload_raw_file_download_approvals(
    raw_file_id: UUID,
    approval_status: str | None = None,
    limit: int = 20,
    repository: Repository = Depends(get_repository),
) -> list[dict]:
    return list(
        repository.list_raw_file_download_approvals(
            raw_file_id=raw_file_id,
            approval_status=approval_status,
            limit=limit,
        )
    )


@router.get(
    "/upload-raw-files/{raw_file_id}/download-readiness",
    response_model=RawFileDownloadReadinessOut,
)
def get_upload_raw_file_download_readiness(
    raw_file_id: UUID,
    repository: Repository = Depends(get_repository),
    settings: Settings = Depends(get_settings),
) -> dict:
    readiness = _build_raw_file_download_readiness(
        raw_file_id=raw_file_id,
        repository=repository,
        now=datetime.now(UTC),
        authorization_boundary=_raw_file_download_authorization_boundary(settings),
    )
    if readiness is None:
        raise HTTPException(
            status_code=404,
            detail="uploaded raw file not found",
        )
    return readiness


@router.get("/upload-raw-files/{raw_file_id}/download")
def download_upload_raw_file(
    raw_file_id: UUID,
    request: Request,
    repository: Repository = Depends(get_repository),
    settings: Settings = Depends(get_settings),
    operator_token: str | None = Header(
        default=None,
        alias="X-NoiseProof-Operator-Token",
    ),
) -> Response:
    raw_file = repository.get_uploaded_raw_file_for_scan(raw_file_id)
    if raw_file is None:
        raise HTTPException(
            status_code=404,
            detail="uploaded raw file not found",
        )
    authorization_boundary = _raw_file_download_authorization_boundary(settings)
    if not _operator_token_allows_download(
        settings=settings,
        operator_token=operator_token,
    ):
        _record_raw_file_download_event(
            repository=repository,
            raw_file_id=raw_file_id,
            latest_scan_result=None,
            download_result="blocked",
            blocked_reason="operator_token_missing_or_invalid",
            http_status_code=403,
            authorization_boundary=authorization_boundary,
            metadata_json={
                "detail": DOWNLOAD_OPERATOR_TOKEN_DETAIL,
                "token_present": operator_token is not None,
                "operator_token_configured": True,
                "rate_limit_consumed": False,
            },
        )
        raise HTTPException(
            status_code=403,
            detail=DOWNLOAD_OPERATOR_TOKEN_DETAIL,
            headers={
                "X-NoiseProof-Authorization-Boundary": authorization_boundary,
            },
        )
    if not _consume_download_attempt(raw_file_id, request):
        _record_raw_file_download_event(
            repository=repository,
            raw_file_id=raw_file_id,
            latest_scan_result=None,
            download_result="blocked",
            blocked_reason="rate_limited",
            http_status_code=429,
            authorization_boundary=authorization_boundary,
            metadata_json={
                "detail": DOWNLOAD_RATE_LIMIT_DETAIL,
            },
        )
        raise HTTPException(
            status_code=429,
            detail=DOWNLOAD_RATE_LIMIT_DETAIL,
            headers={
                "X-NoiseProof-Download-Rate-Limit-Boundary": DOWNLOAD_RATE_LIMIT_BOUNDARY,
                "X-NoiseProof-Authorization-Boundary": authorization_boundary,
            },
        )

    latest_results = list(
        repository.list_raw_file_scan_results(raw_file_id=raw_file_id, limit=1)
    )
    latest_result = latest_results[0] if latest_results else None
    if (
        latest_result is None
        or latest_result.get("scan_status") != "completed"
        or latest_result.get("scan_verdict") != "clean"
    ):
        _record_raw_file_download_event(
            repository=repository,
            raw_file_id=raw_file_id,
            latest_scan_result=latest_result,
            download_result="blocked",
            blocked_reason=(
                "missing_clean_scan" if latest_result is None else "latest_scan_not_clean"
            ),
            http_status_code=409,
            authorization_boundary=authorization_boundary,
            metadata_json={
                "detail": DOWNLOAD_BLOCK_DETAIL,
                "latest_scan_status": (
                    latest_result.get("scan_status") if latest_result else None
                ),
                "latest_scan_verdict": (
                    latest_result.get("scan_verdict") if latest_result else None
                ),
            },
        )
        raise HTTPException(status_code=409, detail=DOWNLOAD_BLOCK_DETAIL)

    if raw_file.get("quarantine_status") != "stored_quarantined":
        _record_raw_file_download_event(
            repository=repository,
            raw_file_id=raw_file_id,
            latest_scan_result=latest_result,
            download_result="blocked",
            blocked_reason="quarantine_status_blocked",
            http_status_code=409,
            authorization_boundary=authorization_boundary,
            metadata_json={
                "detail": "raw file quarantine status does not allow controlled download",
                "quarantine_status": raw_file.get("quarantine_status"),
            },
        )
        raise HTTPException(
            status_code=409,
            detail="raw file quarantine status does not allow controlled download",
        )

    active_approval = repository.find_active_raw_file_download_approval(
        raw_file_id=raw_file_id,
        latest_scan_result_id=latest_result["id"],
        now=datetime.now(UTC),
    )
    if active_approval is None:
        matching_approvals = [
            approval
            for approval in repository.list_raw_file_download_approvals(
                raw_file_id=raw_file_id,
                limit=100,
            )
            if str(approval.get("latest_scan_result_id")) == str(latest_result["id"])
        ]
        blocked_reason = (
            "revoked_or_expired_download_approval"
            if matching_approvals
            else "missing_download_approval"
        )
        _record_raw_file_download_event(
            repository=repository,
            raw_file_id=raw_file_id,
            latest_scan_result=latest_result,
            download_result="blocked",
            blocked_reason=blocked_reason,
            http_status_code=409,
            authorization_boundary=authorization_boundary,
            metadata_json={
                "detail": DOWNLOAD_APPROVAL_BLOCK_DETAIL,
                "latest_scan_status": latest_result.get("scan_status"),
                "latest_scan_verdict": latest_result.get("scan_verdict"),
                "approval_candidate_count": len(matching_approvals),
            },
        )
        raise HTTPException(status_code=409, detail=DOWNLOAD_APPROVAL_BLOCK_DETAIL)

    filename = _safe_download_filename(raw_file.get("filename"), raw_file_id)
    _record_raw_file_download_event(
        repository=repository,
        raw_file_id=raw_file_id,
        latest_scan_result=latest_result,
        download_result="allowed",
        blocked_reason=None,
        http_status_code=200,
        authorization_boundary=authorization_boundary,
        metadata_json={
            "content_disposition_filename": filename,
            "content_type": _content_type_for_download(raw_file.get("content_type")),
            "download_approval_id": str(active_approval.get("id")),
            "approval_boundary": active_approval.get("approval_boundary"),
            "identity_boundary": active_approval.get("identity_boundary"),
            "approved_by_label": active_approval.get("approved_by_label"),
            "approval_status": active_approval.get("approval_status"),
            "approval_expires_at": _metadata_datetime(
                active_approval.get("expires_at")
            ),
            "approval_latest_scan_result_id": str(
                active_approval.get("latest_scan_result_id")
            ),
            "approval_scan_result_matches_latest": str(
                active_approval.get("latest_scan_result_id")
            )
            == str(latest_result["id"]),
        },
    )
    headers = {
        "Content-Disposition": f'attachment; filename="{filename}"',
        "X-Content-Type-Options": "nosniff",
        "X-NoiseProof-Download-Boundary": DOWNLOAD_WITH_APPROVAL_BOUNDARY,
        "X-NoiseProof-Authorization-Boundary": authorization_boundary,
        "X-NoiseProof-Download-Rate-Limit-Boundary": DOWNLOAD_RATE_LIMIT_BOUNDARY,
        "X-NoiseProof-Download-Filename-Boundary": DOWNLOAD_FILENAME_BOUNDARY,
    }
    return Response(
        content=bytes(raw_file["raw_bytes"]),
        media_type=_content_type_for_download(raw_file.get("content_type")),
        headers=headers,
    )


@router.post(
    "/upload-parsed-documents",
    response_model=DocumentOut,
    status_code=201,
)
async def upload_parsed_document(
    file: UploadFile = File(...),
    source_type: str | None = Form(default=None),
    title: str | None = Form(default=None),
    repository: Repository = Depends(get_repository),
) -> dict:
    content = await file.read()

    def operation(_agent_run_id) -> dict:
        preview = preview_upload(
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
        )
        failure_case_candidate = (
            preview.failure_case_candidate.model_dump()
            if preview.failure_case_candidate
            else None
        )
        parse_warnings = [
            warning
            for warning in preview.warnings
            if "does not create documents" not in warning
        ]
        parse_warnings.append(
            "Upload parsed document persistence stores document metadata/profile only and "
            "does not store raw uploaded bytes or parsed text."
        )
        payload = DocumentCreate(
            source_type=preview.source_type,
            source_uri=f"upload://{file.filename}" if file.filename else "upload://unnamed",
            filename=file.filename,
            title=title or file.filename,
            profile_json={
                "persistence_boundary": "document_metadata_and_profile_only_no_raw_file_storage",
                "raw_file_storage": False,
                "parsed_text_storage": False,
                "parser": preview.parser,
                "metadata": preview.metadata,
                "profile": preview.profile.model_dump(),
                "parse_warnings": parse_warnings,
                "failure_case_candidate": failure_case_candidate,
                "upload": {
                    "filename": preview.filename,
                    "content_type": preview.content_type,
                    "byte_count": preview.byte_count,
                },
            },
            extraction_quality=preview.profile.extraction_quality,
            status="parsed_metadata_only",
        )
        return repository.create_document(payload)

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-parsed-documents",
        user_question=f"upload parsed document persist: {source_type or file.filename or 'unknown'}",
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "persistence_boundary": "document_metadata_and_profile_only_no_raw_file_storage",
            "raw_file_storage": False,
            "parsed_text_storage": False,
        },
        operation=operation,
    )


@router.post("/upload-chunk-preview", response_model=UploadChunkPreviewOut)
async def upload_document_chunk_preview(
    file: UploadFile = File(...),
    source_type: str | None = Form(default=None),
    max_characters: int = Form(default=500),
    overlap: int = Form(default=0),
    repository: Repository = Depends(get_repository),
) -> UploadChunkPreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-chunk-preview",
        user_question=f"upload chunk preview: {source_type or file.filename or 'unknown'}",
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "max_characters": max_characters,
            "overlap": overlap,
            "persistence_boundary": "preview_only_not_persisted",
        },
        operation=lambda _agent_run_id: preview_uploaded_chunks(
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
            max_characters=max_characters,
            overlap=overlap,
        ),
    )


@router.post("/upload-chunks", response_model=UploadChunkPersistenceOut, status_code=201)
async def upload_document_chunks(
    file: UploadFile = File(...),
    source_type: str | None = Form(default=None),
    title: str | None = Form(default=None),
    strategy: str = Form(default="fixed-window"),
    max_characters: int = Form(default=500),
    overlap: int = Form(default=0),
    repository: Repository = Depends(get_repository),
) -> dict:
    content = await file.read()

    def operation(_agent_run_id) -> dict:
        preview = preview_uploaded_chunks(
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
            max_characters=max_characters,
            overlap=overlap,
        )
        selected_strategy = next(
            (
                chunk_strategy
                for chunk_strategy in preview.strategies
                if chunk_strategy.strategy == strategy
            ),
            None,
        )
        if selected_strategy is None and preview.strategies:
            selected_strategy = preview.strategies[0]

        selected_chunks = selected_strategy.chunks if selected_strategy else []
        chunk_strategy_name = selected_strategy.strategy if selected_strategy else strategy
        warnings = [
            warning
            for warning in preview.parse_warnings
            if "does not create documents, chunks, or retrieval runs" not in warning
        ]
        warnings.append(
            "Upload chunk handoff creates document metadata and derived chunk rows only; "
            "it does not store raw uploaded bytes or full parsed text."
        )
        if selected_strategy is None:
            warnings.append(
                "No chunk strategy produced chunks; the document metadata was persisted without chunk rows."
            )

        document = repository.create_document(
            DocumentCreate(
                source_type=preview.source_type,
                source_uri=f"upload://{file.filename}" if file.filename else "upload://unnamed",
                filename=file.filename,
                title=title or file.filename,
                profile_json={
                    "persistence_boundary": "document_metadata_and_chunks_only_no_raw_file_storage",
                    "handoff_boundary": "explicit_upload_to_chunks_no_raw_file_storage",
                    "raw_file_storage": False,
                    "parsed_text_storage": False,
                    "parser": preview.parser,
                    "profile": preview.profile.model_dump(),
                    "chunk_strategy": chunk_strategy_name,
                    "chunk_count": len(selected_chunks),
                    "chunk_metrics": selected_strategy.metrics if selected_strategy else {},
                    "chunk_warnings": selected_strategy.warnings if selected_strategy else [],
                    "parse_warnings": warnings,
                    **(
                        _pdf_page_diagnostic_metadata(preview.metadata)
                        if preview.source_type == "pdf"
                        else {}
                    ),
                    "upload": {
                        "filename": preview.filename,
                        "content_type": preview.content_type,
                        "byte_count": preview.byte_count,
                    },
                },
                extraction_quality=preview.profile.extraction_quality,
                status=(
                    "chunked_metadata_only"
                    if selected_chunks
                    else "chunk_handoff_no_chunks"
                ),
            )
        )

        persisted_chunks = []
        for chunk in selected_chunks:
            metadata = dict(chunk.metadata)
            metadata.update(
                {
                    "parser": preview.parser,
                    "handoff_boundary": "explicit_upload_to_chunks_no_raw_file_storage",
                    "raw_file_storage": False,
                    "parsed_text_storage": False,
                    "source_profile": preview.profile.model_dump(),
                }
            )
            if preview.source_type == "pdf":
                metadata.update(
                    {
                        "digital_pdf_text_extraction": (
                            preview.parser == "pdf-pymupdf"
                        ),
                        "robust_pdf_extraction": False,
                        **_pdf_page_diagnostic_metadata(preview.metadata),
                    }
                )
            persisted_chunks.append(
                repository.create_document_chunk(
                    DocumentChunkCreate(
                        document_id=document["id"],
                        source_type=preview.source_type,
                        source_uri=f"upload://{file.filename}" if file.filename else "upload://unnamed",
                        filename=file.filename,
                        chunk_strategy=chunk_strategy_name,
                        chunk_index=chunk.chunk_index,
                        chunk_text=chunk.text,
                        character_start=chunk.metadata.get("start"),
                        character_end=chunk.metadata.get("end"),
                        metadata_json=metadata,
                        persistence_boundary="chunk_text_only_no_raw_file_storage",
                    )
                )
            )

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "source_type": preview.source_type,
            "parser": preview.parser,
            "chunk_strategy": chunk_strategy_name,
            "chunk_count": len(persisted_chunks),
            "persistence_boundary": "chunk_text_only_no_raw_file_storage",
            "handoff_boundary": "explicit_upload_to_chunks_no_raw_file_storage",
            "raw_file_storage": False,
            "parsed_text_storage": False,
            "document": document,
            "chunks": persisted_chunks,
            "warnings": warnings,
        }

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-chunks",
        user_question=f"upload chunks persist: {source_type or file.filename or 'unknown'}",
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "strategy": strategy,
            "max_characters": max_characters,
            "overlap": overlap,
            "persistence_boundary": "chunk_text_only_no_raw_file_storage",
            "handoff_boundary": "explicit_upload_to_chunks_no_raw_file_storage",
            "raw_file_storage": False,
            "parsed_text_storage": False,
        },
        operation=operation,
    )


@router.post("/upload-retrieval-preview", response_model=UploadRetrievalPreviewOut)
async def upload_document_retrieval_preview(
    file: UploadFile = File(...),
    question: str = Form(...),
    source_type: str | None = Form(default=None),
    strategy: str = Form(default="fixed-window"),
    top_k: int = Form(default=5),
    max_characters: int = Form(default=500),
    overlap: int = Form(default=0),
    repository: Repository = Depends(get_repository),
) -> UploadRetrievalPreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-retrieval-preview",
        user_question=question,
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "strategy": strategy,
            "top_k": top_k,
            "max_characters": max_characters,
            "overlap": overlap,
            "persistence_boundary": "preview_only_not_persisted",
        },
        operation=lambda _agent_run_id: preview_uploaded_retrieval(
            question=question,
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
            strategy=strategy,
            top_k=top_k,
            max_characters=max_characters,
            overlap=overlap,
        ),
    )


@router.post("/upload-evidence-preview", response_model=UploadEvidencePreviewOut)
async def upload_document_evidence_preview(
    file: UploadFile = File(...),
    question: str = Form(...),
    source_type: str | None = Form(default=None),
    strategy: str = Form(default="fixed-window"),
    top_k: int = Form(default=5),
    max_characters: int = Form(default=500),
    overlap: int = Form(default=0),
    repository: Repository = Depends(get_repository),
) -> UploadEvidencePreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-evidence-preview",
        user_question=question,
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "strategy": strategy,
            "top_k": top_k,
            "max_characters": max_characters,
            "overlap": overlap,
            "persistence_boundary": "preview_only_not_persisted",
        },
        operation=lambda _agent_run_id: preview_uploaded_evidence(
            question=question,
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
            strategy=strategy,
            top_k=top_k,
            max_characters=max_characters,
            overlap=overlap,
        ),
    )


@router.post("/upload-noise-gate-preview", response_model=UploadNoiseGatePreviewOut)
async def upload_document_noise_gate_preview(
    file: UploadFile = File(...),
    question: str = Form(...),
    source_type: str | None = Form(default=None),
    strategy: str = Form(default="fixed-window"),
    top_k: int = Form(default=5),
    max_characters: int = Form(default=500),
    overlap: int = Form(default=0),
    repository: Repository = Depends(get_repository),
) -> UploadNoiseGatePreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-noise-gate-preview",
        user_question=question,
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "strategy": strategy,
            "top_k": top_k,
            "max_characters": max_characters,
            "overlap": overlap,
            "persistence_boundary": "preview_only_not_persisted",
        },
        operation=lambda _agent_run_id: preview_uploaded_noise_gate(
            question=question,
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
            strategy=strategy,
            top_k=top_k,
            max_characters=max_characters,
            overlap=overlap,
        ),
    )


@router.post("/upload-report-preview", response_model=UploadReportPreviewOut)
async def upload_document_report_preview(
    file: UploadFile = File(...),
    question: str = Form(...),
    source_type: str | None = Form(default=None),
    strategy: str = Form(default="fixed-window"),
    top_k: int = Form(default=5),
    max_characters: int = Form(default=500),
    overlap: int = Form(default=0),
    repository: Repository = Depends(get_repository),
) -> UploadReportPreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-report-preview",
        user_question=question,
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "strategy": strategy,
            "top_k": top_k,
            "max_characters": max_characters,
            "overlap": overlap,
            "persistence_boundary": "preview_only_not_persisted",
        },
        operation=lambda _agent_run_id: preview_uploaded_report(
            question=question,
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
            strategy=strategy,
            top_k=top_k,
            max_characters=max_characters,
            overlap=overlap,
        ),
    )


@router.post("/upload-failure-case-draft-preview", response_model=UploadFailureCaseDraftPreviewOut)
async def upload_document_failure_case_draft_preview(
    file: UploadFile = File(...),
    question: str = Form(...),
    source_type: str | None = Form(default=None),
    strategy: str = Form(default="fixed-window"),
    top_k: int = Form(default=5),
    max_characters: int = Form(default=500),
    overlap: int = Form(default=0),
    repository: Repository = Depends(get_repository),
) -> UploadFailureCaseDraftPreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-failure-case-draft-preview",
        user_question=question,
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "strategy": strategy,
            "top_k": top_k,
            "max_characters": max_characters,
            "overlap": overlap,
            "persistence_boundary": "preview_only_not_persisted",
        },
        operation=lambda _agent_run_id: preview_uploaded_failure_case_draft(
            question=question,
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
            strategy=strategy,
            top_k=top_k,
            max_characters=max_characters,
            overlap=overlap,
        ),
    )


@router.post("/chunk-preview", response_model=ChunkPreviewOut)
def chunk_document_preview(
    payload: ChunkPreviewRequest,
    repository: Repository = Depends(get_repository),
) -> ChunkPreviewOut:
    return run_with_trace(
        repository,
        endpoint="POST /documents/chunk-preview",
        user_question=f"chunk preview: {payload.source_type}",
        trace_json={
            "source_type": payload.source_type,
            "max_characters": payload.max_characters,
            "overlap": payload.overlap,
        },
        operation=lambda _agent_run_id: preview_chunks(payload),
    )
