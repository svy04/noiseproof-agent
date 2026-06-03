from __future__ import annotations

import socket
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Protocol

from packages.ingestion.scanning.adapter import (
    ScanAdapterRequest,
    ScanAdapterResult,
    build_scan_error_result,
)


class ClamdConnection(Protocol):
    def __enter__(self) -> "ClamdConnection": ...

    def __exit__(self, exc_type, exc, traceback) -> bool | None: ...

    def sendall(self, payload: bytes) -> None: ...

    def recv(self, buffer_size: int) -> bytes: ...


ConnectionFactory = Callable[[tuple[str, int], float], ClamdConnection]


class ClamdScannerAdapter:
    scanner_name = "clamav-clamd"

    def __init__(
        self,
        *,
        host: str = "clamav",
        port: int = 3310,
        connection_factory: ConnectionFactory | None = None,
        chunk_size: int = 64 * 1024,
    ) -> None:
        self.host = host
        self.port = port
        self.connection_factory = connection_factory or socket.create_connection
        self.chunk_size = chunk_size

    def scan(self, request: ScanAdapterRequest) -> ScanAdapterResult:
        started_at = _utc_now()
        if request.temporary_scan_path is None:
            return build_scan_error_result(
                request,
                scanner_name=self.scanner_name,
                failure_reason="missing_temporary_scan_path",
                error_message="missing temporary_scan_path for clamd INSTREAM",
                started_at=started_at,
                metadata=_adapter_metadata(self, bytes_streamed=0, chunk_count=0),
            )

        scan_path = Path(request.temporary_scan_path)
        try:
            response, bytes_streamed, chunk_count = self._scan_path(
                scan_path,
                timeout=float(request.scanner_timeout_seconds),
            )
        except (TimeoutError, socket.timeout):
            return build_scan_error_result(
                request,
                scanner_name=self.scanner_name,
                failure_reason="timeout",
                error_message="clamd INSTREAM scan exceeded timeout",
                started_at=started_at,
                metadata=_adapter_metadata(self, bytes_streamed=0, chunk_count=0),
            )
        except FileNotFoundError:
            return build_scan_error_result(
                request,
                scanner_name=self.scanner_name,
                failure_reason="temporary_scan_file_unreadable",
                error_message="temporary scan file could not be read",
                started_at=started_at,
                metadata=_adapter_metadata(self, bytes_streamed=0, chunk_count=0),
            )
        except OSError as exc:
            return build_scan_error_result(
                request,
                scanner_name=self.scanner_name,
                failure_reason="clamd_unavailable",
                error_message=str(exc),
                started_at=started_at,
                metadata=_adapter_metadata(self, bytes_streamed=0, chunk_count=0),
            )

        finished_at = _utc_now()
        metadata = {
            **_request_metadata(request),
            **_adapter_metadata(
                self,
                bytes_streamed=bytes_streamed,
                chunk_count=chunk_count,
                response=response,
            ),
        }

        if response.endswith(" OK"):
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

        if response.endswith(" FOUND") or " FOUND" in response:
            return ScanAdapterResult(
                raw_file_id=request.raw_file_id,
                scanner_name=self.scanner_name,
                scanner_version=None,
                signature_db_version=None,
                scan_started_at=started_at,
                scan_finished_at=finished_at,
                scan_status="completed",
                scan_verdict="infected",
                matched_signature=_matched_signature(response),
                error_message=None,
                metadata=metadata,
            )

        if response.endswith(" ERROR") or " ERROR" in response:
            return build_scan_error_result(
                request,
                scanner_name=self.scanner_name,
                failure_reason="clamd_scan_error",
                error_message=response,
                started_at=started_at,
                finished_at=finished_at,
                metadata=metadata,
            )

        return build_scan_error_result(
            request,
            scanner_name=self.scanner_name,
            failure_reason="clamd_unexpected_response",
            error_message=response or "empty clamd response",
            started_at=started_at,
            finished_at=finished_at,
            metadata=metadata,
        )

    def _scan_path(self, scan_path: Path, *, timeout: float) -> tuple[str, int, int]:
        bytes_streamed = 0
        chunk_count = 0
        with self.connection_factory((self.host, self.port), timeout) as connection:
            connection.sendall(b"zINSTREAM\0")
            with scan_path.open("rb") as handle:
                while True:
                    chunk = handle.read(self.chunk_size)
                    if not chunk:
                        break
                    chunk_count += 1
                    bytes_streamed += len(chunk)
                    connection.sendall(len(chunk).to_bytes(4, "big") + chunk)
            connection.sendall((0).to_bytes(4, "big"))
            response = _receive_response(connection)
        return response, bytes_streamed, chunk_count


def _receive_response(connection: ClamdConnection) -> str:
    parts = []
    while True:
        chunk = connection.recv(4096)
        if not chunk:
            break
        parts.append(chunk)
        if b"\0" in chunk:
            break
    return b"".join(parts).decode("utf-8", errors="replace").strip("\0\r\n ")


def _request_metadata(request: ScanAdapterRequest) -> dict[str, object]:
    return {
        "content_sha256": request.content_sha256,
        "byte_size": request.byte_size,
        "declared_content_type": request.declared_content_type,
        "original_filename_present": bool(request.original_filename),
        "temporary_scan_path_present": request.temporary_scan_path is not None,
        "scanner_timeout_seconds": request.scanner_timeout_seconds,
    }


def _adapter_metadata(
    adapter: ClamdScannerAdapter,
    *,
    bytes_streamed: int,
    chunk_count: int,
    response: str | None = None,
) -> dict[str, object]:
    metadata: dict[str, object] = {
        "clamd_host": adapter.host,
        "clamd_port": adapter.port,
        "clamd_transport": "tcp",
        "clamd_command": "INSTREAM",
        "bytes_streamed": bytes_streamed,
        "chunk_count": chunk_count,
    }
    if response is not None:
        metadata["clamd_response"] = response
    return metadata


def _matched_signature(response: str) -> str | None:
    before_found = response.rsplit(" FOUND", 1)[0]
    if ":" in before_found:
        return before_found.rsplit(":", 1)[1].strip() or None
    return before_found.strip() or None


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)
