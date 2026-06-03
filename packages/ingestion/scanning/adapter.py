from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Protocol
from uuid import UUID

SENSITIVE_METADATA_KEYS = {"temporary_scan_path", "raw_bytes", "file_bytes"}


@dataclass(frozen=True)
class ScanAdapterRequest:
    raw_file_id: UUID
    storage_key: str
    original_filename: str | None
    declared_content_type: str | None
    byte_size: int
    content_sha256: str
    temporary_scan_path: str | Path | None
    scanner_timeout_seconds: int = 30
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ScanAdapterResult:
    raw_file_id: UUID
    scanner_name: str
    scanner_version: str | None
    signature_db_version: str | None
    scan_started_at: datetime
    scan_finished_at: datetime
    scan_status: str
    scan_verdict: str
    matched_signature: str | None
    error_message: str | None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_raw_file_scan_result_payload(self) -> dict[str, Any]:
        return {
            "raw_file_id": self.raw_file_id,
            "scanner_name": self.scanner_name,
            "scanner_version": self.scanner_version,
            "signature_db_version": self.signature_db_version,
            "scan_started_at": self.scan_started_at,
            "scan_finished_at": self.scan_finished_at,
            "scan_status": self.scan_status,
            "scan_verdict": self.scan_verdict,
            "matched_signature": self.matched_signature,
            "error_message": self.error_message,
            "metadata_json": dict(self.metadata),
        }


class ScannerAdapter(Protocol):
    scanner_name: str

    def scan(self, request: ScanAdapterRequest) -> ScanAdapterResult: ...


class ScannerUnavailableAdapter:
    scanner_name = "scanner-unavailable"

    def __init__(
        self,
        *,
        failure_reason: str = "missing_scanner_binary",
        error_message: str = "missing_scanner_binary: no scanner adapter is configured",
    ) -> None:
        self.failure_reason = failure_reason
        self.error_message = error_message

    def scan(self, request: ScanAdapterRequest) -> ScanAdapterResult:
        return build_scan_error_result(
            request,
            scanner_name=self.scanner_name,
            failure_reason=self.failure_reason,
            error_message=self.error_message,
        )


def build_scan_error_result(
    request: ScanAdapterRequest,
    *,
    scanner_name: str,
    failure_reason: str,
    error_message: str,
    scanner_version: str | None = None,
    signature_db_version: str | None = None,
    started_at: datetime | None = None,
    finished_at: datetime | None = None,
    metadata: dict[str, Any] | None = None,
) -> ScanAdapterResult:
    started = started_at or _utc_now()
    finished = finished_at or _utc_now()
    merged_metadata = _base_metadata(request, failure_reason)
    merged_metadata.update(_public_metadata(metadata or {}))
    safe_error_message = _error_message_with_reason(failure_reason, error_message)
    return ScanAdapterResult(
        raw_file_id=request.raw_file_id,
        scanner_name=scanner_name,
        scanner_version=scanner_version,
        signature_db_version=signature_db_version,
        scan_started_at=started,
        scan_finished_at=finished,
        scan_status="failed",
        scan_verdict="scan_error",
        matched_signature=None,
        error_message=safe_error_message,
        metadata=merged_metadata,
    )


def _base_metadata(request: ScanAdapterRequest, failure_reason: str) -> dict[str, Any]:
    return {
        **_public_metadata(request.metadata),
        "failure_reason": failure_reason,
        "content_sha256": request.content_sha256,
        "byte_size": request.byte_size,
        "declared_content_type": request.declared_content_type,
        "original_filename_present": bool(request.original_filename),
        "temporary_scan_path_present": request.temporary_scan_path is not None,
        "scanner_timeout_seconds": request.scanner_timeout_seconds,
    }


def _public_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in metadata.items()
        if key not in SENSITIVE_METADATA_KEYS
    }


def _error_message_with_reason(failure_reason: str, error_message: str) -> str:
    if failure_reason in error_message:
        return error_message
    return f"{failure_reason}: {error_message}"


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)
