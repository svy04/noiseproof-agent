from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
from uuid import UUID

from fastapi import Depends

from app.db import Repository
from app.schemas import RawFileScanResultCreate
from app.settings import Settings, get_settings
from packages.ingestion.scanning import (
    ClamAvScannerAdapter,
    ClamdScannerAdapter,
    ScanAdapterRequest,
    ScannerAdapter,
    ScannerUnavailableAdapter,
    build_scan_error_result,
)

SENSITIVE_SCAN_METADATA_KEYS = {"temporary_scan_path", "raw_bytes", "file_bytes"}


def get_scanner_adapter(
    settings: Settings = Depends(get_settings),
) -> ScannerAdapter:
    scanner_name = settings.noiseproof_scanner.strip().lower()
    if scanner_name == "clamav":
        return ClamAvScannerAdapter()
    if scanner_name == "clamd":
        return ClamdScannerAdapter(host=settings.clamd_host, port=settings.clamd_port)
    return ScannerUnavailableAdapter(
        failure_reason="scanner_not_configured",
        error_message=(
            "scanner_not_configured: set NOISEPROOF_SCANNER=clamav or "
            "NOISEPROOF_SCANNER=clamd only after the runtime and signature "
            "database are verified"
        ),
    )


def scan_uploaded_raw_file(
    raw_file_id: UUID,
    *,
    repository: Repository,
    scanner: ScannerAdapter,
    settings: Settings,
) -> dict | None:
    raw_file = repository.get_uploaded_raw_file_for_scan(raw_file_id)
    if raw_file is None:
        return None

    with TemporaryDirectory(prefix="noiseproof-scan-") as temp_dir:
        scan_path = _temporary_scan_path(temp_dir, raw_file)
        scan_path.write_bytes(bytes(raw_file["raw_bytes"]))
        request = _scan_request(
            raw_file=raw_file,
            raw_file_id=raw_file_id,
            scan_path=scan_path,
            settings=settings,
        )
        try:
            result = scanner.scan(request)
        except Exception as exc:  # pragma: no cover - defensive adapter boundary
            result = build_scan_error_result(
                request,
                scanner_name=getattr(scanner, "scanner_name", "unknown-scanner"),
                failure_reason="scanner_adapter_exception",
                error_message=str(exc),
            )

        payload = result.to_raw_file_scan_result_payload()
        payload["metadata_json"] = _sanitize_scan_metadata(
            {
                **payload.get("metadata_json", {}),
                "raw_file_id": str(raw_file_id),
                "scanner_execution_boundary": "stored_raw_bytes_to_temp_file_to_adapter",
                "response_boundary": "metadata_only_no_raw_bytes_no_download_url",
            }
        )
        return repository.create_raw_file_scan_result(
            RawFileScanResultCreate(**payload)
        )


def _temporary_scan_path(temp_dir: str, raw_file: dict) -> Path:
    storage_key = str(raw_file.get("storage_key") or raw_file["id"])
    safe_storage_key = "".join(
        character if character.isalnum() or character in {"-", "_"} else "_"
        for character in storage_key
    )
    return Path(temp_dir) / f"{safe_storage_key}.scan"


def _scan_request(
    *,
    raw_file: dict,
    raw_file_id: UUID,
    scan_path: Path,
    settings: Settings,
) -> ScanAdapterRequest:
    return ScanAdapterRequest(
        raw_file_id=raw_file_id,
        storage_key=str(raw_file["storage_key"]),
        original_filename=raw_file.get("filename"),
        declared_content_type=raw_file.get("content_type"),
        byte_size=int(raw_file.get("size_bytes") or 0),
        content_sha256=str(raw_file["content_sha256"]),
        temporary_scan_path=scan_path,
        scanner_timeout_seconds=settings.raw_file_scanner_timeout_seconds,
        metadata={
            "raw_file_id": str(raw_file_id),
            "storage_backend": raw_file.get("storage_backend"),
            "quarantine_status": raw_file.get("quarantine_status"),
            "scanner_execution_boundary": "stored_raw_bytes_to_temp_file_to_adapter",
            "response_boundary": "metadata_only_no_raw_bytes_no_download_url",
        },
    )


def _sanitize_scan_metadata(metadata: dict) -> dict:
    return {
        key: value
        for key, value in metadata.items()
        if key not in SENSITIVE_SCAN_METADATA_KEYS
    }
