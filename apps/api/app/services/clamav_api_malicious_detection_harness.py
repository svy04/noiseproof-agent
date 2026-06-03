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
OWNER_RUNTIME_SMOKE_PACKET_PHASE_MARKER = (
    "ClamAV API endpoint malicious-detection owner runtime smoke packet v0"
)
OWNER_RUNTIME_SMOKE_VALIDATOR_PHASE_MARKER = (
    "ClamAV API endpoint malicious-detection owner runtime smoke validator v0"
)
OWNER_RUNTIME_SMOKE_REPORT_CONTRACT_PHASE_MARKER = (
    "ClamAV API endpoint malicious-detection owner runtime smoke report contract v0"
)
OWNER_RUNTIME_SMOKE_REPORT_SCHEMA_PHASE_MARKER = (
    "ClamAV API endpoint malicious-detection owner runtime smoke report schema v0"
)
OWNER_RUNTIME_SMOKE_ACCEPTED_SUMMARY = {
    "scanner_name": "clamav-clamd",
    "scan_status": "completed",
    "scan_verdict": "infected",
    "matched_signature": "Eicar-Test-Signature",
    "metadata_boundary": "metadata_only_no_raw_bytes_no_download_url",
}
OWNER_RUNTIME_SMOKE_FORBIDDEN_PAYLOAD_KEYS = {
    "content_bytes",
    "download_url",
    "encoded_payload",
    "payload",
    "payload_base64",
    "raw_bytes",
    "raw_payload",
    "signature_text",
    "test_signature",
    "test_signature_text",
}
OWNER_RUNTIME_SMOKE_EXPECTED_TOP_LEVEL_FIELDS = {
    "api_calls_attempted",
    "harness_status",
    "input_source",
    "malicious_detection_verified",
    "payload_committed_to_repo",
    "raw_payload_logged",
    "required_owner_input_missing",
    "scan_result_summary",
}


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
    require_owner_input: bool = False,
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
            "required_owner_input_missing": require_owner_input,
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
        "required_owner_input_missing": False,
        "blocked_reason": None,
        "scan_result_summary": summary,
    }


def build_owner_runtime_smoke_packet() -> dict[str, object]:
    return {
        "phase_marker": OWNER_RUNTIME_SMOKE_PACKET_PHASE_MARKER,
        "packet_status": "ready_for_owner_input",
        "api_calls_attempted": False,
        "payload_committed_to_repo": False,
        "raw_payload_logged": False,
        "required_input": "owner-provided runtime-only test signature via stdin",
        "command_template": (
            "NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1 "
            "<owner-provided-stdin> | "
            "uv run python -m app.services.clamav_api_malicious_detection_harness "
            "--signature-stdin --require-owner-input"
        ),
        "success_criteria": {
            "scanner_name": "clamav-clamd",
            "scan_status": "completed",
            "scan_verdict": "infected",
            "matched_signature": "Eicar-Test-Signature",
        },
        "failure_states": [
            "not_configured",
            "blocked_by_environment",
            "unexpected_clean",
            "scan_error",
        ],
        "non_claims": {
            "malware_detection_proof": False,
            "production_malware_scanning_evidence": False,
            "hosted_deployment_verified": False,
            "external_reviewer_feedback": False,
            "product_complete": False,
        },
        "boundary": [
            "does not include a test signature payload",
            "does not call the API",
            "does not upload raw bytes",
            "does not call the scan endpoint",
            "not malware detection proof",
            "owner-provided runtime smoke remains pending",
        ],
    }


def build_owner_runtime_smoke_report_contract() -> dict[str, object]:
    return {
        "phase_marker": OWNER_RUNTIME_SMOKE_REPORT_CONTRACT_PHASE_MARKER,
        "contract_status": "ready_for_owner_runtime_report",
        "api_calls_attempted": False,
        "payload_committed_to_repo": False,
        "raw_payload_logged": False,
        "validator_command": (
            "uv run python -m app.services.clamav_api_malicious_detection_harness "
            "--validate-owner-runtime-smoke-report path/to/owner-runtime-smoke-report.json"
        ),
        "accepted_report": {
            "harness_status": "verified_infected",
            "malicious_detection_verified": True,
            "api_calls_attempted": True,
            "payload_committed_to_repo": False,
            "raw_payload_logged": False,
            "input_source": "stdin",
            "required_owner_input_missing": False,
        },
        "accepted_scan_result_summary": dict(OWNER_RUNTIME_SMOKE_ACCEPTED_SUMMARY),
        "forbidden_payload_fields": sorted(OWNER_RUNTIME_SMOKE_FORBIDDEN_PAYLOAD_KEYS),
        "accepted_validator_output": {
            "validation_status": "accepted",
            "accepted_owner_runtime_smoke": True,
            "missing_or_failed_checks": [],
        },
        "rejected_validator_output": {
            "validation_status": "rejected",
            "accepted_owner_runtime_smoke": False,
            "missing_or_failed_checks": "non-empty",
        },
        "non_claims": {
            "endpoint_malicious_detection_runtime_proof": False,
            "production_malware_scanning_evidence": False,
            "hosted_deployment_verified": False,
            "external_reviewer_feedback": False,
            "product_complete": False,
        },
        "boundary": [
            "contract only",
            "does not include a test signature payload",
            "does not call the API",
            "does not upload raw bytes",
            "does not call the scan endpoint",
            "not endpoint malicious-detection runtime proof",
            "owner-provided runtime smoke remains pending",
        ],
    }


def build_owner_runtime_smoke_report_schema() -> dict[str, object]:
    summary_properties = {
        field: {"const": value}
        for field, value in OWNER_RUNTIME_SMOKE_ACCEPTED_SUMMARY.items()
    }
    return {
        "phase_marker": OWNER_RUNTIME_SMOKE_REPORT_SCHEMA_PHASE_MARKER,
        "schema_status": "ready_for_owner_runtime_report",
        "api_calls_attempted": False,
        "payload_committed_to_repo": False,
        "raw_payload_logged": False,
        "json_schema": {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "NoiseProof ClamAV owner runtime smoke report",
            "type": "object",
            "additionalProperties": False,
            "required": [
                "harness_status",
                "malicious_detection_verified",
                "api_calls_attempted",
                "payload_committed_to_repo",
                "raw_payload_logged",
                "input_source",
                "required_owner_input_missing",
                "scan_result_summary",
            ],
            "properties": {
                "harness_status": {"const": "verified_infected"},
                "malicious_detection_verified": {"const": True},
                "api_calls_attempted": {"const": True},
                "payload_committed_to_repo": {"const": False},
                "raw_payload_logged": {"const": False},
                "input_source": {"const": "stdin"},
                "required_owner_input_missing": {"const": False},
                "scan_result_summary": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": list(OWNER_RUNTIME_SMOKE_ACCEPTED_SUMMARY),
                    "properties": summary_properties,
                },
            },
        },
        "forbidden_payload_fields": sorted(OWNER_RUNTIME_SMOKE_FORBIDDEN_PAYLOAD_KEYS),
        "non_claims": {
            "validator_replacement": False,
            "endpoint_malicious_detection_runtime_proof": False,
            "production_malware_scanning_evidence": False,
            "hosted_deployment_verified": False,
            "external_reviewer_feedback": False,
            "product_complete": False,
        },
        "boundary": [
            "schema artifact only",
            "validator remains authoritative",
            "does not include a test signature payload",
            "does not call the API",
            "does not upload raw bytes",
            "does not call the scan endpoint",
            "not endpoint malicious-detection runtime proof",
            "owner-provided runtime smoke remains pending",
        ],
    }


def validate_owner_runtime_smoke_report(report: Mapping[str, object]) -> dict[str, object]:
    missing_or_failed_checks: list[str] = []
    forbidden_payload_fields = _find_forbidden_payload_fields(report)
    for field_path in forbidden_payload_fields:
        missing_or_failed_checks.append(f"forbidden payload field present: {field_path}")
    unexpected_fields = _find_unexpected_owner_runtime_report_fields(report)
    for field_path in unexpected_fields:
        missing_or_failed_checks.append(f"unexpected field present: {field_path}")

    expected_top_level = {
        "harness_status": "verified_infected",
        "malicious_detection_verified": True,
        "api_calls_attempted": True,
        "payload_committed_to_repo": False,
        "raw_payload_logged": False,
        "input_source": "stdin",
        "required_owner_input_missing": False,
    }
    for field, expected_value in expected_top_level.items():
        if report.get(field) != expected_value:
            formatted = str(expected_value).lower()
            missing_or_failed_checks.append(f"{field} must be {formatted}")

    summary = report.get("scan_result_summary")
    if not isinstance(summary, Mapping):
        missing_or_failed_checks.append("scan_result_summary must be present")
        summary = {}
    for field, expected_value in OWNER_RUNTIME_SMOKE_ACCEPTED_SUMMARY.items():
        if summary.get(field) != expected_value:
            missing_or_failed_checks.append(f"scan_result_summary.{field} must be {expected_value}")

    accepted = not missing_or_failed_checks
    return {
        "phase_marker": OWNER_RUNTIME_SMOKE_VALIDATOR_PHASE_MARKER,
        "validation_status": "accepted" if accepted else "rejected",
        "accepted_owner_runtime_smoke": accepted,
        "missing_or_failed_checks": missing_or_failed_checks,
        "forbidden_payload_fields": forbidden_payload_fields,
        "unexpected_fields": unexpected_fields,
        "reported_payload_committed_to_repo": report.get("payload_committed_to_repo"),
        "reported_raw_payload_logged": report.get("raw_payload_logged"),
        "payload_committed_to_repo": False,
        "raw_payload_logged": False,
        "scan_result_summary": {
            key: summary.get(key) for key in OWNER_RUNTIME_SMOKE_ACCEPTED_SUMMARY
        },
        "non_claims": {
            "production_malware_scanning_evidence": False,
            "hosted_deployment_verified": False,
            "external_reviewer_feedback": False,
            "product_complete": False,
        },
        "boundary": [
            "validates owner-provided runtime smoke metadata only",
            "does not include a test signature payload",
            "does not call the API",
            "does not upload raw bytes",
            "does not call the scan endpoint",
            "not production malware scanning evidence",
        ],
    }


def _find_forbidden_payload_fields(
    value: object, *, prefix: str = ""
) -> list[str]:
    if isinstance(value, Mapping):
        found: list[str] = []
        for key, child_value in value.items():
            key_text = str(key)
            field_path = f"{prefix}.{key_text}" if prefix else key_text
            if key_text.lower() in OWNER_RUNTIME_SMOKE_FORBIDDEN_PAYLOAD_KEYS:
                found.append(field_path)
            found.extend(_find_forbidden_payload_fields(child_value, prefix=field_path))
        return sorted(found)
    if isinstance(value, list):
        found = []
        for index, child_value in enumerate(value):
            field_path = f"{prefix}[{index}]" if prefix else f"[{index}]"
            found.extend(_find_forbidden_payload_fields(child_value, prefix=field_path))
        return sorted(found)
    return []


def _find_unexpected_owner_runtime_report_fields(
    report: Mapping[str, object]
) -> list[str]:
    unexpected = [
        key
        for key in report
        if str(key) not in OWNER_RUNTIME_SMOKE_EXPECTED_TOP_LEVEL_FIELDS
    ]
    summary = report.get("scan_result_summary")
    if isinstance(summary, Mapping):
        for key in summary:
            key_text = str(key)
            if key_text not in OWNER_RUNTIME_SMOKE_ACCEPTED_SUMMARY:
                unexpected.append(f"scan_result_summary.{key_text}")
    return sorted(str(field) for field in unexpected)


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
    parser.add_argument(
        "--require-owner-input",
        action="store_true",
        help=(
            "Return a non-zero exit code if the owner-provided test signature is "
            "missing."
        ),
    )
    parser.add_argument(
        "--print-owner-runtime-smoke-packet",
        action="store_true",
        help=(
            "Print a no-payload packet describing the owner-provided runtime "
            "smoke contract."
        ),
    )
    parser.add_argument(
        "--print-owner-runtime-smoke-report-contract",
        action="store_true",
        help=(
            "Print the no-payload JSON metadata contract expected by the "
            "owner runtime smoke report validator."
        ),
    )
    parser.add_argument(
        "--print-owner-runtime-smoke-report-schema",
        action="store_true",
        help=(
            "Print the no-payload JSON Schema-shaped accepted report shape "
            "for the owner runtime smoke report validator."
        ),
    )
    parser.add_argument(
        "--validate-owner-runtime-smoke-report",
        help=(
            "Validate a future owner-provided runtime smoke JSON report without "
            "including or reading a test signature payload."
        ),
    )
    parser.add_argument("--output", help="Optional JSON report output path.")
    args = parser.parse_args(argv)

    source_env = env if env is not None else os.environ
    if args.validate_owner_runtime_smoke_report:
        report = validate_owner_runtime_smoke_report(
            _read_json_report(Path(args.validate_owner_runtime_smoke_report))
        )
    elif args.print_owner_runtime_smoke_report_contract:
        report = build_owner_runtime_smoke_report_contract()
    elif args.print_owner_runtime_smoke_report_schema:
        report = build_owner_runtime_smoke_report_schema()
    elif args.print_owner_runtime_smoke_packet:
        report = build_owner_runtime_smoke_packet()
    else:
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
            require_owner_input=args.require_owner_input,
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

    if (
        args.print_owner_runtime_smoke_packet
        or args.print_owner_runtime_smoke_report_contract
        or args.print_owner_runtime_smoke_report_schema
    ):
        return 0
    if args.validate_owner_runtime_smoke_report:
        return 0 if report["accepted_owner_runtime_smoke"] is True else 5
    return _exit_code_for_status(str(report["harness_status"]), report)


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
        "required_owner_input_missing": False,
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


def _exit_code_for_status(status: str, report: Mapping[str, object] | None = None) -> int:
    if report and report.get("required_owner_input_missing") is True:
        return 4
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


def _read_json_report(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise ValueError("owner runtime smoke report must be a JSON object")
    return payload


if __name__ == "__main__":
    raise SystemExit(main())
