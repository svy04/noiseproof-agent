from uuid import uuid4
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.scanning import (
    ScanAdapterRequest,
    ScannerUnavailableAdapter,
    build_scan_error_result,
)


def test_unavailable_scanner_maps_missing_binary_to_scan_error_without_temp_path_leak():
    raw_file_id = uuid4()
    request = ScanAdapterRequest(
        raw_file_id=raw_file_id,
        storage_key="raw-uploads/generated-key.bin",
        original_filename="earnings.pdf",
        declared_content_type="application/pdf",
        byte_size=512,
        content_sha256="abc123",
        temporary_scan_path="C:/tmp/noiseproof/generated-key.bin",
        scanner_timeout_seconds=15,
        metadata={"source": "unit-test"},
    )

    result = ScannerUnavailableAdapter().scan(request)
    payload = result.to_raw_file_scan_result_payload()

    assert result.scan_status == "failed"
    assert result.scan_verdict == "scan_error"
    assert result.matched_signature is None
    assert "missing_scanner_binary" in result.error_message
    assert result.metadata["content_sha256"] == "abc123"
    assert result.metadata["temporary_scan_path_present"] is True
    assert "temporary_scan_path" not in result.metadata
    assert payload["raw_file_id"] == raw_file_id
    assert payload["scan_status"] == "failed"
    assert payload["scan_verdict"] == "scan_error"
    assert payload["metadata_json"]["failure_reason"] == "missing_scanner_binary"
    assert "temporary_scan_path" not in payload["metadata_json"]


def test_timeout_scan_result_is_not_clean():
    raw_file_id = uuid4()
    request = ScanAdapterRequest(
        raw_file_id=raw_file_id,
        storage_key="raw-uploads/generated-key.bin",
        original_filename="large.csv",
        declared_content_type="text/csv",
        byte_size=10_000,
        content_sha256="def456",
        temporary_scan_path=None,
        scanner_timeout_seconds=1,
    )

    result = build_scan_error_result(
        request,
        scanner_name="generic-scanner",
        failure_reason="timeout",
        error_message="scanner process exceeded timeout",
    )

    assert result.scan_status == "failed"
    assert result.scan_verdict == "scan_error"
    assert "timeout" in result.error_message
    assert result.metadata["failure_reason"] == "timeout"
    assert result.to_raw_file_scan_result_payload()["scan_verdict"] != "clean"
