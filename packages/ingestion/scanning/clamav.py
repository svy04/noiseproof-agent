from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from shutil import which as default_which
from subprocess import CompletedProcess, TimeoutExpired, run as default_run
from typing import Callable, Sequence

from packages.ingestion.scanning.adapter import (
    ScanAdapterRequest,
    ScanAdapterResult,
    build_scan_error_result,
)

Runner = Callable[..., CompletedProcess[str]]
Which = Callable[[str], str | None]


class ClamAvScannerAdapter:
    scanner_name = "clamav-clamscan"

    def __init__(
        self,
        *,
        binary_name: str = "clamscan",
        which: Which = default_which,
        runner: Runner = default_run,
    ) -> None:
        self.binary_name = binary_name
        self.which = which
        self.runner = runner

    def scan(self, request: ScanAdapterRequest) -> ScanAdapterResult:
        started_at = _utc_now()
        if request.temporary_scan_path is None:
            return build_scan_error_result(
                request,
                scanner_name=self.scanner_name,
                failure_reason="missing_temporary_scan_path",
                error_message="missing temporary_scan_path for clamscan",
                started_at=started_at,
                metadata=_command_metadata(None, None),
            )

        binary_path = self.which(self.binary_name)
        if binary_path is None:
            return build_scan_error_result(
                request,
                scanner_name=self.scanner_name,
                failure_reason="missing_clamscan",
                error_message=f"missing clamscan binary: {self.binary_name}",
                started_at=started_at,
                metadata=_command_metadata(None, None),
            )

        command = [binary_path, "--no-summary", str(request.temporary_scan_path)]
        try:
            completed = self.runner(
                command,
                capture_output=True,
                text=True,
                timeout=request.scanner_timeout_seconds,
            )
        except TimeoutExpired:
            return build_scan_error_result(
                request,
                scanner_name=self.scanner_name,
                failure_reason="timeout",
                error_message="clamscan process exceeded timeout",
                started_at=started_at,
                metadata=_command_metadata(binary_path, command),
            )

        finished_at = _utc_now()
        metadata = {
            **_request_metadata(request),
            **_command_metadata(binary_path, command),
            "returncode": completed.returncode,
            "stdout_line_count": len((completed.stdout or "").splitlines()),
            "stderr_present": bool(completed.stderr),
        }

        if completed.returncode == 0:
            return ScanAdapterResult(
                raw_file_id=request.raw_file_id,
                scanner_name=self.scanner_name,
                scanner_version=None,
                signature_db_version=None,
                scan_started_at=started_at,
                scan_finished_at=finished_at,
                scan_status="completed",
                scan_verdict="clean",
                matched_signature=None,
                error_message=None,
                metadata=metadata,
            )

        if completed.returncode == 1:
            return ScanAdapterResult(
                raw_file_id=request.raw_file_id,
                scanner_name=self.scanner_name,
                scanner_version=None,
                signature_db_version=None,
                scan_started_at=started_at,
                scan_finished_at=finished_at,
                scan_status="completed",
                scan_verdict="infected",
                matched_signature=_matched_signature(completed.stdout or ""),
                error_message=None,
                metadata=metadata,
            )

        return build_scan_error_result(
            request,
            scanner_name=self.scanner_name,
            failure_reason="unknown_return_code",
            error_message=f"clamscan returned unexpected code {completed.returncode}",
            started_at=started_at,
            finished_at=finished_at,
            metadata=metadata,
        )


def _request_metadata(request: ScanAdapterRequest) -> dict[str, object]:
    return {
        "content_sha256": request.content_sha256,
        "byte_size": request.byte_size,
        "declared_content_type": request.declared_content_type,
        "original_filename_present": bool(request.original_filename),
        "temporary_scan_path_present": request.temporary_scan_path is not None,
        "scanner_timeout_seconds": request.scanner_timeout_seconds,
    }


def _command_metadata(binary_path: str | None, command: Sequence[str] | None) -> dict[str, object]:
    binary_label = Path(binary_path).name if binary_path else None
    return {
        "clamav_binary": binary_label,
        "clamav_command": _redacted_command(command),
    }


def _redacted_command(command: Sequence[str] | None) -> list[str]:
    if command is None:
        return []
    return [Path(command[0]).name, *command[1:-1], "<temporary_scan_path>"]


def _matched_signature(stdout: str) -> str | None:
    for line in stdout.splitlines():
        if " FOUND" not in line:
            continue
        before_found = line.rsplit(" FOUND", 1)[0]
        if ":" in before_found:
            return before_found.rsplit(":", 1)[1].strip() or None
        return before_found.strip() or None
    return None


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)
