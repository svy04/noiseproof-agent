from __future__ import annotations

import argparse
import json
import os
import sys
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Protocol, TextIO
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


PHASE_MARKER = "ClamAV API endpoint malicious-detection test harness v0"
ALLOW_ENV = "NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE"
SIGNATURE_ENV = "NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT"
API_BASE_URL_ENV = "NOISEPROOF_API_BASE_URL"


class EndpointClient(Protocol):
    def upload_raw_file(self, **kwargs) -> tuple[int, dict]: ...

    def scan_raw_file(self, raw_file_id: str) -> tuple[int, dict]: ...


@dataclass
class UrllibEndpointClient:
    api_base_url: str
    timeout_seconds: float = 30.0

    def upload_raw_file(
        self,
        *,
        source_type: str,
        filename: str,
        content_type: str,
        content_bytes: bytes,
    ) -> tuple[int, dict]:
        boundary = f"noiseproof-{uuid.uuid4().hex}"
        body = _multipart_body(
            boundary=boundary,
            fields={"source_type": source_type},
            file_field="file",
            filename=filename,
            content_type=content_type,
            content_bytes=content_bytes,
        )
        return self._request_json(
            "/documents/upload-raw-files",
            method="POST",
            body=body,
            headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        )

    def scan_raw_file(self, raw_file_id: str) -> tuple[int, dict]:
        return self._request_json(
            f"/documents/upload-raw-files/{raw_file_id}/scan",
            method="POST",
            body=b"",
            headers={"Content-Type": "application/json"},
        )

    def _request_json(
        self,
        path: str,
        *,
        method: str,
        body: bytes,
        headers: Mapping[str, str],
    ) -> tuple[int, dict]:
        url = f"{self.api_base_url.rstrip('/')}{path}"
        request = Request(url, data=body, method=method, headers=dict(headers))
        try:
            with urlopen(request, timeout=self.timeout_seconds) as response:
                return response.status, _read_json_response(response.read())
        except HTTPError as exc:
            return exc.code, _read_json_response(exc.read())


def build_malicious_detection_harness_report(
    *,
    allow_test_signature_smoke: str | None,
    test_signature_text: str | None,
    input_source: str = "environment",
    client: EndpointClient | None = None,
    api_base_url: str = "http://localhost:8000",
    timeout_seconds: float = 30.0,
) -> dict[str, object]:
    base_report = _base_report()
    if allow_test_signature_smoke != "1" or not test_signature_text:
        if input_source == "stdin":
            blocked_reason = (
                "set NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1 and provide "
                "owner-provided test signature text on stdin"
            )
        else:
            blocked_reason = (
                "set NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1 and provide "
                "NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT"
            )
        return {
            **base_report,
            "harness_status": "not_configured",
            "api_calls_attempted": False,
            "payload_length_bytes": 0,
            "input_source": input_source,
            "blocked_reason": blocked_reason,
            "scan_result_summary": None,
        }

    content_bytes = test_signature_text.encode("utf-8")
    endpoint_client = client or UrllibEndpointClient(
        api_base_url=api_base_url,
        timeout_seconds=timeout_seconds,
    )

    try:
        upload_status, upload_body = endpoint_client.upload_raw_file(
            source_type="text",
            filename="owner-provided-runtime-only-test-signature.txt",
            content_type="text/plain",
            content_bytes=content_bytes,
        )
        raw_file_id = str(upload_body.get("raw_file_id") or upload_body.get("id") or "")
        if upload_status not in {200, 201} or not raw_file_id:
            return _blocked_report(
                base_report,
                payload_length_bytes=len(content_bytes),
                input_source=input_source,
                reason=f"upload_failed status={upload_status}",
            )

        scan_status, scan_body = endpoint_client.scan_raw_file(raw_file_id)
        if scan_status not in {200, 201}:
            return _blocked_report(
                base_report,
                payload_length_bytes=len(content_bytes),
                input_source=input_source,
                reason=f"scan_failed status={scan_status}",
                scan_body=scan_body,
            )
    except (OSError, URLError) as exc:
        return _blocked_report(
            base_report,
            payload_length_bytes=len(content_bytes),
            input_source=input_source,
            reason=str(exc),
        )

    summary = _scan_result_summary(scan_body)
    harness_status = _classify_scan_result(summary)

    return {
        **base_report,
        "harness_status": harness_status,
        "malicious_detection_verified": harness_status == "verified_infected",
        "api_calls_attempted": True,
        "payload_length_bytes": len(content_bytes),
        "input_source": input_source,
        "blocked_reason": None,
        "scan_result_summary": summary,
    }


def main(
    argv: list[str] | None = None,
    *,
    env: Mapping[str, str] | None = None,
    stdin: TextIO | None = None,
    client: EndpointClient | None = None,
) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Run the opt-in ClamAV API endpoint malicious-detection test harness. "
            "The test signature must be supplied at runtime through the environment."
        )
    )
    parser.add_argument(
        "--api-base-url",
        default=None,
        help=f"API base URL. Defaults to {API_BASE_URL_ENV} or http://localhost:8000.",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=float,
        default=30.0,
        help="HTTP timeout for each endpoint request.",
    )
    parser.add_argument(
        "--signature-stdin",
        action="store_true",
        help=(
            "Read the owner-provided test signature from stdin. The raw input is "
            "not printed in the report."
        ),
    )
    parser.add_argument("--output", help="Optional JSON report output path.")
    args = parser.parse_args(argv)

    source_env = env if env is not None else os.environ
    input_source = "stdin" if args.signature_stdin else "environment"
    if args.signature_stdin:
        stdin_source = stdin if stdin is not None else sys.stdin
        test_signature_text = stdin_source.read().rstrip("\r\n")
    else:
        test_signature_text = source_env.get(SIGNATURE_ENV)
    report = build_malicious_detection_harness_report(
        allow_test_signature_smoke=source_env.get(ALLOW_ENV),
        test_signature_text=test_signature_text,
        input_source=input_source,
        client=client,
        api_base_url=args.api_base_url
        or source_env.get(API_BASE_URL_ENV, "http://localhost:8000"),
        timeout_seconds=args.timeout_seconds,
    )
    payload = json.dumps(report, indent=2, sort_keys=True)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)

    return _exit_code_for_status(str(report["harness_status"]))


def _base_report() -> dict[str, object]:
    return {
        "phase_marker": PHASE_MARKER,
        "payload_committed_to_repo": False,
        "raw_payload_logged": False,
        "malicious_detection_verified": False,
        "claims": {
            "production_malware_scanning_evidence": False,
            "hosted_deployment_verified": False,
            "external_reviewer_feedback": False,
            "product_complete": False,
        },
        "boundary": [
            "owner-provided runtime-only test signature",
            "do not store the test signature payload or an encoded form in the repository",
            "do not bypass OS security controls",
            "not malware detection proof",
            "not production malware scanning evidence",
            "not hosted deployment evidence",
            "not external reviewer feedback",
            "not product-complete",
        ],
    }


def _blocked_report(
    base_report: dict[str, object],
    *,
    payload_length_bytes: int,
    input_source: str,
    reason: str,
    scan_body: dict | None = None,
) -> dict[str, object]:
    return {
        **base_report,
        "harness_status": "blocked_by_environment",
        "api_calls_attempted": True,
        "payload_length_bytes": payload_length_bytes,
        "input_source": input_source,
        "blocked_reason": reason,
        "scan_result_summary": _scan_result_summary(scan_body or {})
        if scan_body
        else None,
    }


def _scan_result_summary(scan_body: dict) -> dict[str, object | None]:
    metadata = scan_body.get("metadata_json") if isinstance(scan_body, dict) else None
    if not isinstance(metadata, dict):
        metadata = {}
    return {
        "scanner_name": scan_body.get("scanner_name"),
        "scan_status": scan_body.get("scan_status"),
        "scan_verdict": scan_body.get("scan_verdict"),
        "matched_signature": scan_body.get("matched_signature"),
        "metadata_boundary": metadata.get("response_boundary"),
    }


def _classify_scan_result(summary: dict[str, object | None]) -> str:
    scanner_name = summary.get("scanner_name")
    scan_status = summary.get("scan_status")
    scan_verdict = summary.get("scan_verdict")
    matched_signature = summary.get("matched_signature")

    if (
        scanner_name == "clamav-clamd"
        and scan_status == "completed"
        and scan_verdict == "infected"
        and matched_signature == "Eicar-Test-Signature"
    ):
        return "verified_infected"
    if scan_status == "completed" and scan_verdict == "clean":
        return "unexpected_clean"
    if scan_status == "failed" or scan_verdict == "scan_error":
        return "scan_error"
    return "blocked_by_environment"


def _exit_code_for_status(status: str) -> int:
    if status in {"not_configured", "verified_infected"}:
        return 0
    if status in {"unexpected_clean", "scan_error"}:
        return 2
    return 3


def _multipart_body(
    *,
    boundary: str,
    fields: Mapping[str, str],
    file_field: str,
    filename: str,
    content_type: str,
    content_bytes: bytes,
) -> bytes:
    chunks: list[bytes] = []
    for name, value in fields.items():
        chunks.extend(
            [
                f"--{boundary}\r\n".encode("utf-8"),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(
                    "utf-8"
                ),
                value.encode("utf-8"),
                b"\r\n",
            ]
        )
    chunks.extend(
        [
            f"--{boundary}\r\n".encode("utf-8"),
            (
                f'Content-Disposition: form-data; name="{file_field}"; '
                f'filename="{filename}"\r\n'
            ).encode("utf-8"),
            f"Content-Type: {content_type}\r\n\r\n".encode("utf-8"),
            content_bytes,
            b"\r\n",
            f"--{boundary}--\r\n".encode("utf-8"),
        ]
    )
    return b"".join(chunks)


def _read_json_response(raw_body: bytes) -> dict:
    if not raw_body:
        return {}
    try:
        payload = json.loads(raw_body.decode("utf-8"))
    except json.JSONDecodeError:
        return {"response_body_parse_error": True}
    return payload if isinstance(payload, dict) else {"response_json": payload}


if __name__ == "__main__":
    raise SystemExit(main())
