from uuid import uuid4
from subprocess import CompletedProcess, TimeoutExpired
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.scanning import (
    ClamAvScannerAdapter,
    ClamdScannerAdapter,
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


def test_clamav_adapter_missing_binary_is_scan_error_not_clean():
    request = _scan_request()
    adapter = ClamAvScannerAdapter(which=lambda _: None)

    result = adapter.scan(request)

    assert result.scan_status == "failed"
    assert result.scan_verdict == "scan_error"
    assert result.metadata["failure_reason"] == "missing_clamscan"
    assert result.to_raw_file_scan_result_payload()["scan_verdict"] != "clean"


def test_clamav_adapter_requires_temporary_scan_path():
    request = _scan_request(temporary_scan_path=None)
    adapter = ClamAvScannerAdapter(which=lambda _: "C:/tools/clamscan.exe")

    result = adapter.scan(request)

    assert result.scan_status == "failed"
    assert result.scan_verdict == "scan_error"
    assert result.metadata["failure_reason"] == "missing_temporary_scan_path"


def test_clamav_adapter_maps_clean_output_without_remove_flag():
    commands = []

    def runner(command, **kwargs):
        commands.append(command)
        return CompletedProcess(command, 0, stdout="C:/tmp/file.bin: OK\n", stderr="")

    request = _scan_request()
    adapter = ClamAvScannerAdapter(
        which=lambda _: "C:/tools/clamscan.exe",
        runner=runner,
    )

    result = adapter.scan(request)

    assert result.scan_status == "completed"
    assert result.scan_verdict == "clean"
    assert result.matched_signature is None
    assert "--remove" not in commands[0]
    assert "--no-summary" in commands[0]
    assert str(request.temporary_scan_path) in commands[0]
    assert result.metadata["temporary_scan_path_present"] is True
    assert "temporary_scan_path" not in result.metadata


def test_clamav_adapter_maps_infected_output_to_signature():
    def runner(command, **kwargs):
        return CompletedProcess(
            command,
            1,
            stdout="C:/tmp/file.bin: Eicar-Test-Signature FOUND\n",
            stderr="",
        )

    result = ClamAvScannerAdapter(
        which=lambda _: "C:/tools/clamscan.exe",
        runner=runner,
    ).scan(_scan_request())

    assert result.scan_status == "completed"
    assert result.scan_verdict == "infected"
    assert result.matched_signature == "Eicar-Test-Signature"


def test_clamav_adapter_timeout_and_unknown_return_code_are_scan_errors():
    def timeout_runner(command, **kwargs):
        raise TimeoutExpired(cmd=command, timeout=kwargs["timeout"])

    timeout_result = ClamAvScannerAdapter(
        which=lambda _: "C:/tools/clamscan.exe",
        runner=timeout_runner,
    ).scan(_scan_request())

    assert timeout_result.scan_status == "failed"
    assert timeout_result.scan_verdict == "scan_error"
    assert timeout_result.metadata["failure_reason"] == "timeout"

    def unknown_runner(command, **kwargs):
        return CompletedProcess(command, 7, stdout="unexpected", stderr="weird")

    unknown_result = ClamAvScannerAdapter(
        which=lambda _: "C:/tools/clamscan.exe",
        runner=unknown_runner,
    ).scan(_scan_request())

    assert unknown_result.scan_status == "failed"
    assert unknown_result.scan_verdict == "scan_error"
    assert unknown_result.metadata["failure_reason"] == "unknown_return_code"


def test_clamd_adapter_streams_file_bytes_and_maps_clean_response(tmp_path):
    scan_path = tmp_path / "sample.bin"
    scan_path.write_bytes(b"clean bytes")
    connection = FakeClamdConnection(response=b"stream: OK\x00")
    adapter = ClamdScannerAdapter(
        host="clamav",
        port=3310,
        connection_factory=_fake_factory(connection),
        chunk_size=4,
    )

    result = adapter.scan(_scan_request(temporary_scan_path=scan_path))

    assert result.scan_status == "completed"
    assert result.scan_verdict == "clean"
    assert result.matched_signature is None
    assert connection.address == ("clamav", 3310)
    assert connection.timeout == 3
    assert connection.sent[0] == b"zINSTREAM\x00"
    assert connection.sent[-1] == b"\x00\x00\x00\x00"
    assert _instream_payload(connection.sent[1:-1]) == b"clean bytes"
    assert result.metadata["clamd_command"] == "INSTREAM"
    assert result.metadata["clamd_transport"] == "tcp"
    assert result.metadata["chunk_count"] == 3
    assert result.metadata["bytes_streamed"] == len(b"clean bytes")
    assert "temporary_scan_path" not in result.metadata


def test_clamd_adapter_maps_found_response_to_infected_signature(tmp_path):
    scan_path = tmp_path / "eicar.bin"
    scan_path.write_bytes(b"not the real payload")
    connection = FakeClamdConnection(
        response=b"stream: Eicar-Test-Signature FOUND\x00"
    )
    adapter = ClamdScannerAdapter(
        connection_factory=_fake_factory(connection),
    )

    result = adapter.scan(_scan_request(temporary_scan_path=scan_path))

    assert result.scan_status == "completed"
    assert result.scan_verdict == "infected"
    assert result.matched_signature == "Eicar-Test-Signature"


def test_clamd_adapter_maps_missing_temp_path_and_unavailable_service_to_scan_error(tmp_path):
    missing_path_result = ClamdScannerAdapter().scan(
        _scan_request(temporary_scan_path=None)
    )

    assert missing_path_result.scan_status == "failed"
    assert missing_path_result.scan_verdict == "scan_error"
    assert missing_path_result.metadata["failure_reason"] == "missing_temporary_scan_path"

    def unavailable_connection(address, timeout):
        raise OSError("connection refused")

    scan_path = tmp_path / "sample.bin"
    scan_path.write_bytes(b"bytes")
    unavailable_result = ClamdScannerAdapter(
        connection_factory=unavailable_connection,
    ).scan(_scan_request(temporary_scan_path=scan_path))

    assert unavailable_result.scan_status == "failed"
    assert unavailable_result.scan_verdict == "scan_error"
    assert unavailable_result.metadata["failure_reason"] == "clamd_unavailable"
    assert unavailable_result.to_raw_file_scan_result_payload()["scan_verdict"] != "clean"


def test_clamd_adapter_maps_timeout_and_unexpected_response_to_scan_error(tmp_path):
    scan_path = tmp_path / "sample.bin"
    scan_path.write_bytes(b"bytes")

    timeout_result = ClamdScannerAdapter(
        connection_factory=lambda address, timeout: FakeClamdConnection(
            response=b"",
            recv_error=TimeoutError("timed out"),
        ),
    ).scan(_scan_request(temporary_scan_path=scan_path))

    assert timeout_result.scan_status == "failed"
    assert timeout_result.scan_verdict == "scan_error"
    assert timeout_result.metadata["failure_reason"] == "timeout"

    unexpected_result = ClamdScannerAdapter(
        connection_factory=lambda address, timeout: FakeClamdConnection(
            response=b"stream: WHAT\x00",
        ),
    ).scan(_scan_request(temporary_scan_path=scan_path))

    assert unexpected_result.scan_status == "failed"
    assert unexpected_result.scan_verdict == "scan_error"
    assert unexpected_result.metadata["failure_reason"] == "clamd_unexpected_response"


def _scan_request(temporary_scan_path="C:/tmp/noiseproof/generated-key.bin"):
    return ScanAdapterRequest(
        raw_file_id=uuid4(),
        storage_key="raw-uploads/generated-key.bin",
        original_filename="sample.bin",
        declared_content_type="application/octet-stream",
        byte_size=64,
        content_sha256="abc123",
        temporary_scan_path=temporary_scan_path,
        scanner_timeout_seconds=3,
    )


def _fake_factory(connection: "FakeClamdConnection"):
    def factory(address, timeout):
        connection.address = address
        connection.timeout = timeout
        return connection

    return factory


class FakeClamdConnection:
    def __init__(self, *, response: bytes, recv_error: Exception | None = None):
        self.response = response
        self.recv_error = recv_error
        self.sent = []
        self.address = None
        self.timeout = None
        self._response_sent = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def sendall(self, payload: bytes):
        self.sent.append(payload)

    def recv(self, buffer_size: int):
        if self.recv_error is not None:
            raise self.recv_error
        if self._response_sent:
            return b""
        self._response_sent = True
        return self.response


def _instream_payload(chunks):
    payload = b""
    for chunk in chunks:
        size = int.from_bytes(chunk[:4], "big")
        payload += chunk[4 : 4 + size]
    return payload
