import json
from pathlib import Path
import sys
from io import StringIO


REPO_ROOT = Path(__file__).resolve().parents[3]

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from app.services.clamav_api_malicious_detection_harness import (
    ALLOW_ENV,
    PHASE_MARKER,
    build_malicious_detection_harness_report,
    main,
)


class RecordingClient:
    def __init__(self, *, upload_response=None, scan_response=None, error=None):
        self.upload_response = upload_response or (
            201,
            {"raw_file_id": "11111111-1111-4111-8111-111111111111"},
        )
        self.scan_response = scan_response or (
            201,
            {
                "id": "22222222-2222-4222-8222-222222222222",
                "raw_file_id": "11111111-1111-4111-8111-111111111111",
                "scanner_name": "clamav-clamd",
                "scan_status": "completed",
                "scan_verdict": "infected",
                "matched_signature": "Eicar-Test-Signature",
                "metadata_json": {
                    "clamd_command": "INSTREAM",
                    "response_boundary": "metadata_only_no_raw_bytes_no_download_url",
                },
            },
        )
        self.error = error
        self.upload_calls = []
        self.scan_calls = []

    def upload_raw_file(self, **kwargs):
        if self.error:
            raise self.error
        self.upload_calls.append(kwargs)
        return self.upload_response

    def scan_raw_file(self, raw_file_id):
        if self.error:
            raise self.error
        self.scan_calls.append(raw_file_id)
        return self.scan_response


def test_malicious_detection_harness_not_configured_does_not_call_api_or_claim_detection():
    client = RecordingClient()

    report = build_malicious_detection_harness_report(
        allow_test_signature_smoke=None,
        test_signature_text=None,
        client=client,
    )

    assert report["phase_marker"] == PHASE_MARKER
    assert report["harness_status"] == "not_configured"
    assert report["malicious_detection_verified"] is False
    assert report["payload_committed_to_repo"] is False
    assert report["raw_payload_logged"] is False
    assert report["api_calls_attempted"] is False
    assert report["scan_result_summary"] is None
    assert client.upload_calls == []
    assert client.scan_calls == []
    assert "not malware detection proof" in report["boundary"]


def test_malicious_detection_harness_classifies_verified_infected_without_payload_leak():
    signature_text = "owner-provided-runtime-placeholder-input"
    client = RecordingClient()

    report = build_malicious_detection_harness_report(
        allow_test_signature_smoke="1",
        test_signature_text=signature_text,
        client=client,
    )

    assert report["harness_status"] == "verified_infected"
    assert report["malicious_detection_verified"] is True
    assert report["payload_committed_to_repo"] is False
    assert report["raw_payload_logged"] is False
    assert report["payload_length_bytes"] == len(signature_text.encode("utf-8"))
    assert report["scan_result_summary"] == {
        "scanner_name": "clamav-clamd",
        "scan_status": "completed",
        "scan_verdict": "infected",
        "matched_signature": "Eicar-Test-Signature",
        "metadata_boundary": "metadata_only_no_raw_bytes_no_download_url",
    }
    assert client.upload_calls[0]["content_bytes"] == signature_text.encode("utf-8")
    assert signature_text not in json.dumps(report, sort_keys=True)


def test_malicious_detection_harness_classifies_blocked_environment_on_client_error():
    client = RecordingClient(error=OSError("host security blocked request"))

    report = build_malicious_detection_harness_report(
        allow_test_signature_smoke="1",
        test_signature_text="owner-provided-runtime-only-test-signature",
        client=client,
    )

    assert report["harness_status"] == "blocked_by_environment"
    assert report["malicious_detection_verified"] is False
    assert report["payload_committed_to_repo"] is False
    assert report["blocked_reason"] == "host security blocked request"
    assert "do not bypass OS security controls" in report["boundary"]


def test_malicious_detection_harness_command_prints_not_configured_json(capsys):
    exit_code = main([], env={})

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["harness_status"] == "not_configured"
    assert payload["malicious_detection_verified"] is False
    assert payload["payload_committed_to_repo"] is False


def test_malicious_detection_harness_command_accepts_stdin_owner_input_without_payload_leak(capsys):
    signature_text = "owner-provided-runtime-only-test-signature"
    client = RecordingClient()

    exit_code = main(
        ["--signature-stdin"],
        env={ALLOW_ENV: "1"},
        stdin=StringIO(signature_text),
        client=client,
    )

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["harness_status"] == "verified_infected"
    assert payload["malicious_detection_verified"] is True
    assert payload["payload_committed_to_repo"] is False
    assert payload["raw_payload_logged"] is False
    assert payload["input_source"] == "stdin"
    assert signature_text not in json.dumps(payload, sort_keys=True)
    assert client.upload_calls[0]["content_bytes"] == signature_text.encode("utf-8")


def test_malicious_detection_harness_command_empty_stdin_is_not_configured(capsys):
    client = RecordingClient()

    exit_code = main(
        ["--signature-stdin"],
        env={ALLOW_ENV: "1"},
        stdin=StringIO(""),
        client=client,
    )

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["harness_status"] == "not_configured"
    assert payload["api_calls_attempted"] is False
    assert payload["input_source"] == "stdin"
    assert "stdin" in payload["blocked_reason"]
    assert client.upload_calls == []


def test_malicious_detection_harness_required_owner_input_exits_nonzero_without_stdin(capsys):
    client = RecordingClient()

    exit_code = main(
        ["--signature-stdin", "--require-owner-input"],
        env={ALLOW_ENV: "1"},
        stdin=StringIO(""),
        client=client,
    )

    assert exit_code == 4
    payload = json.loads(capsys.readouterr().out)
    assert payload["harness_status"] == "not_configured"
    assert payload["required_owner_input_missing"] is True
    assert payload["api_calls_attempted"] is False
    assert payload["input_source"] == "stdin"
    assert "owner-provided" in payload["blocked_reason"]
    assert client.upload_calls == []


def test_malicious_detection_harness_required_owner_input_still_allows_fake_verified_path(capsys):
    signature_text = "owner-provided-runtime-only-test-signature"
    client = RecordingClient()

    exit_code = main(
        ["--signature-stdin", "--require-owner-input"],
        env={ALLOW_ENV: "1"},
        stdin=StringIO(signature_text),
        client=client,
    )

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["harness_status"] == "verified_infected"
    assert payload["required_owner_input_missing"] is False
    assert payload["malicious_detection_verified"] is True
    assert signature_text not in json.dumps(payload, sort_keys=True)


def test_malicious_detection_harness_rejects_owner_runtime_output_path_inside_repository(
    capsys,
):
    signature_text = "owner-provided-runtime-only-test-signature"
    output_path = REPO_ROOT / ".tmp-owner-runtime-smoke-output.json"
    client = RecordingClient()

    try:
        exit_code = main(
            [
                "--signature-stdin",
                "--require-owner-input",
                "--output",
                str(output_path),
            ],
            env={ALLOW_ENV: "1"},
            stdin=StringIO(signature_text),
            client=client,
        )
    finally:
        output_path.unlink(missing_ok=True)

    assert exit_code == 6
    payload = json.loads(capsys.readouterr().out)
    assert payload["harness_status"] == "output_path_rejected"
    assert payload["api_calls_attempted"] is False
    assert payload["malicious_detection_verified"] is False
    assert payload["output_path_boundary"] == {
        "output_path_allowed": False,
        "required_location": "outside_repository",
    }
    assert "output path must be outside repository" in payload["blocked_reason"]
    assert output_path.exists() is False
    assert client.upload_calls == []
    assert signature_text not in json.dumps(payload, sort_keys=True)


def test_malicious_detection_harness_writes_validator_handoff_report_outside_repository(
    capsys, tmp_path
):
    signature_text = "owner-provided-runtime-placeholder-input"
    report_path = tmp_path / "owner-runtime-smoke-validator-report.json"
    client = RecordingClient()

    exit_code = main(
        [
            "--signature-stdin",
            "--require-owner-input",
            "--owner-runtime-smoke-report",
            "--output",
            str(report_path),
        ],
        env={ALLOW_ENV: "1"},
        stdin=StringIO(signature_text),
        client=client,
    )

    assert exit_code == 0
    assert capsys.readouterr().out == ""
    report = json.loads(report_path.read_text(encoding="utf-8"))
    assert report == {
        "api_calls_attempted": True,
        "harness_status": "verified_infected",
        "input_source": "stdin",
        "malicious_detection_verified": True,
        "payload_committed_to_repo": False,
        "raw_payload_logged": False,
        "required_owner_input_missing": False,
        "scan_result_summary": {
            "matched_signature": "Eicar-Test-Signature",
            "metadata_boundary": "metadata_only_no_raw_bytes_no_download_url",
            "scan_status": "completed",
            "scan_verdict": "infected",
            "scanner_name": "clamav-clamd",
        },
    }
    assert "phase_marker" not in report
    assert "claims" not in report
    assert "payload_length_bytes" not in report
    assert signature_text not in json.dumps(report, sort_keys=True)

    validate_exit_code = main(
        ["--validate-owner-runtime-smoke-report", str(report_path)]
    )

    assert validate_exit_code == 0
    validation = json.loads(capsys.readouterr().out)
    assert validation["validation_status"] == "accepted"
    assert validation["accepted_owner_runtime_smoke"] is True


def test_malicious_detection_harness_prints_owner_runtime_smoke_packet_without_payload(capsys):
    client = RecordingClient()

    exit_code = main(
        ["--print-owner-runtime-smoke-packet"],
        env={},
        client=client,
    )

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["phase_marker"] == "ClamAV API endpoint malicious-detection owner runtime smoke packet v0"
    assert payload["packet_status"] == "ready_for_owner_input"
    assert payload["api_calls_attempted"] is False
    assert payload["payload_committed_to_repo"] is False
    assert payload["raw_payload_logged"] is False
    assert payload["required_input"] == "owner-provided runtime-only test signature via stdin"
    assert payload["command_template"] == (
        "cat <owner-provided-runtime-only-signature-file-outside-repo> | "
        "NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1 "
        "uv run python -m app.services.clamav_api_malicious_detection_harness "
        "--signature-stdin --require-owner-input "
        "--owner-runtime-smoke-report "
        "--output <runtime-report-path-outside-repo>"
    )
    assert payload["command_templates"] == {
        "posix": (
            "cat <owner-provided-runtime-only-signature-file-outside-repo> | "
            "NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1 "
            "uv run python -m app.services.clamav_api_malicious_detection_harness "
            "--signature-stdin --require-owner-input "
            "--owner-runtime-smoke-report "
            "--output <runtime-report-path-outside-repo>"
        ),
        "powershell": (
            "$env:NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE='1'; "
            "Get-Content -Raw -LiteralPath "
            "'<owner-provided-runtime-only-signature-file-outside-repo>' | "
            "uv run python -m app.services.clamav_api_malicious_detection_harness "
            "--signature-stdin --require-owner-input "
            "--owner-runtime-smoke-report "
            "--output '<runtime-report-path-outside-repo>'"
        ),
    }
    assert payload["post_run_validation_command"] == (
        "uv run python -m app.services.clamav_api_malicious_detection_harness "
        "--validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>"
    )
    assert payload["runtime_report_handling"] == {
        "write_report_outside_repo": True,
        "validate_metadata_only": True,
        "emit_validator_handoff_report": True,
        "do_not_commit_report_if_it_contains_payload_fields": True,
    }
    assert payload["success_criteria"] == {
        "scanner_name": "clamav-clamd",
        "scan_status": "completed",
        "scan_verdict": "infected",
        "matched_signature": "Eicar-Test-Signature",
    }
    assert payload["non_claims"]["malware_detection_proof"] is False
    assert client.upload_calls == []
    assert "owner-provided-runtime-only-test-signature" not in json.dumps(
        payload, sort_keys=True
    )


def test_malicious_detection_harness_prints_owner_runtime_smoke_report_contract_without_payload(
    capsys,
):
    client = RecordingClient()

    exit_code = main(
        ["--print-owner-runtime-smoke-report-contract"],
        env={},
        client=client,
    )

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert (
        payload["phase_marker"]
        == "ClamAV API endpoint malicious-detection owner runtime smoke report contract v0"
    )
    assert payload["contract_status"] == "ready_for_owner_runtime_report"
    assert payload["accepted_report"]["harness_status"] == "verified_infected"
    assert payload["accepted_report"]["input_source"] == "stdin"
    assert payload["accepted_scan_result_summary"] == {
        "scanner_name": "clamav-clamd",
        "scan_status": "completed",
        "scan_verdict": "infected",
        "matched_signature": "Eicar-Test-Signature",
        "metadata_boundary": "metadata_only_no_raw_bytes_no_download_url",
    }
    assert "test_signature_text" in payload["forbidden_payload_fields"]
    assert "encoded_payload" in payload["forbidden_payload_fields"]
    assert "payload_base64" in payload["forbidden_payload_fields"]
    assert payload["accepted_validator_output"] == {
        "validation_status": "accepted",
        "accepted_owner_runtime_smoke": True,
        "missing_or_failed_checks": [],
    }
    assert payload["api_calls_attempted"] is False
    assert payload["payload_committed_to_repo"] is False
    assert payload["raw_payload_logged"] is False
    assert client.upload_calls == []
    assert client.scan_calls == []
    assert "owner-provided-runtime-only-test-signature" not in json.dumps(
        payload, sort_keys=True
    )


def test_malicious_detection_harness_prints_owner_runtime_smoke_report_schema_without_payload(
    capsys,
):
    client = RecordingClient()

    exit_code = main(
        ["--print-owner-runtime-smoke-report-schema"],
        env={},
        client=client,
    )

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert (
        payload["phase_marker"]
        == "ClamAV API endpoint malicious-detection owner runtime smoke report schema v0"
    )
    assert payload["schema_status"] == "ready_for_owner_runtime_report"
    schema = payload["json_schema"]
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["title"] == "NoiseProof ClamAV owner runtime smoke report"
    assert schema["type"] == "object"
    assert schema["additionalProperties"] is False
    assert schema["properties"]["harness_status"] == {"const": "verified_infected"}
    assert schema["properties"]["malicious_detection_verified"] == {"const": True}
    assert schema["properties"]["api_calls_attempted"] == {"const": True}
    assert schema["properties"]["payload_committed_to_repo"] == {"const": False}
    assert schema["properties"]["raw_payload_logged"] == {"const": False}
    assert schema["properties"]["input_source"] == {"const": "stdin"}
    assert schema["properties"]["required_owner_input_missing"] == {"const": False}
    summary_schema = schema["properties"]["scan_result_summary"]
    assert summary_schema["additionalProperties"] is False
    assert summary_schema["properties"]["scanner_name"] == {"const": "clamav-clamd"}
    assert summary_schema["properties"]["scan_status"] == {"const": "completed"}
    assert summary_schema["properties"]["scan_verdict"] == {"const": "infected"}
    assert summary_schema["properties"]["matched_signature"] == {
        "const": "Eicar-Test-Signature"
    }
    assert summary_schema["properties"]["metadata_boundary"] == {
        "const": "metadata_only_no_raw_bytes_no_download_url"
    }
    assert "test_signature_text" in payload["forbidden_payload_fields"]
    assert "encoded_payload" in payload["forbidden_payload_fields"]
    assert payload["api_calls_attempted"] is False
    assert payload["payload_committed_to_repo"] is False
    assert payload["raw_payload_logged"] is False
    assert payload["non_claims"]["validator_replacement"] is False
    assert client.upload_calls == []
    assert client.scan_calls == []
    assert "owner-provided-runtime-only-test-signature" not in json.dumps(
        payload, sort_keys=True
    )


def test_owner_runtime_smoke_validator_accepts_verified_infected_metadata_report(
    capsys, tmp_path
):
    report_path = tmp_path / "owner-runtime-smoke-report.json"
    report_path.write_text(
        json.dumps(
            {
                "harness_status": "verified_infected",
                "malicious_detection_verified": True,
                "api_calls_attempted": True,
                "payload_committed_to_repo": False,
                "raw_payload_logged": False,
                "input_source": "stdin",
                "required_owner_input_missing": False,
                "scan_result_summary": {
                    "scanner_name": "clamav-clamd",
                    "scan_status": "completed",
                    "scan_verdict": "infected",
                    "matched_signature": "Eicar-Test-Signature",
                    "metadata_boundary": "metadata_only_no_raw_bytes_no_download_url",
                },
            }
        ),
        encoding="utf-8",
    )

    exit_code = main(["--validate-owner-runtime-smoke-report", str(report_path)])

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert (
        payload["phase_marker"]
        == "ClamAV API endpoint malicious-detection owner runtime smoke validator v0"
    )
    assert payload["validation_status"] == "accepted"
    assert payload["accepted_owner_runtime_smoke"] is True
    assert payload["missing_or_failed_checks"] == []
    assert payload["payload_committed_to_repo"] is False
    assert payload["raw_payload_logged"] is False
    assert payload["non_claims"]["production_malware_scanning_evidence"] is False


def test_owner_runtime_smoke_validator_accepts_windows_bom_json_report(
    capsys, tmp_path
):
    report_path = tmp_path / "owner-runtime-smoke-report.json"
    report_path.write_text(
        json.dumps(
            {
                "harness_status": "verified_infected",
                "malicious_detection_verified": True,
                "api_calls_attempted": True,
                "payload_committed_to_repo": False,
                "raw_payload_logged": False,
                "input_source": "stdin",
                "required_owner_input_missing": False,
                "scan_result_summary": {
                    "scanner_name": "clamav-clamd",
                    "scan_status": "completed",
                    "scan_verdict": "infected",
                    "matched_signature": "Eicar-Test-Signature",
                    "metadata_boundary": "metadata_only_no_raw_bytes_no_download_url",
                },
            }
        ),
        encoding="utf-8-sig",
    )

    exit_code = main(["--validate-owner-runtime-smoke-report", str(report_path)])

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["validation_status"] == "accepted"
    assert payload["accepted_owner_runtime_smoke"] is True


def test_owner_runtime_smoke_validator_rejects_report_path_inside_repository(
    capsys,
):
    report_path = REPO_ROOT / ".tmp-owner-runtime-smoke-report.json"
    report_path.write_text(
        json.dumps(
            {
                "harness_status": "verified_infected",
                "malicious_detection_verified": True,
                "api_calls_attempted": True,
                "payload_committed_to_repo": False,
                "raw_payload_logged": False,
                "input_source": "stdin",
                "required_owner_input_missing": False,
                "scan_result_summary": {
                    "scanner_name": "clamav-clamd",
                    "scan_status": "completed",
                    "scan_verdict": "infected",
                    "matched_signature": "Eicar-Test-Signature",
                    "metadata_boundary": "metadata_only_no_raw_bytes_no_download_url",
                },
            }
        ),
        encoding="utf-8",
    )
    try:
        exit_code = main(["--validate-owner-runtime-smoke-report", str(report_path)])
    finally:
        report_path.unlink(missing_ok=True)

    assert exit_code == 5
    payload = json.loads(capsys.readouterr().out)
    assert payload["validation_status"] == "rejected"
    assert payload["accepted_owner_runtime_smoke"] is False
    assert payload["report_path_boundary"] == {
        "report_path_allowed": False,
        "required_location": "outside_repository",
    }
    assert "report path must be outside repository" in payload[
        "missing_or_failed_checks"
    ]
    assert payload["non_claims"]["production_malware_scanning_evidence"] is False


def test_owner_runtime_smoke_validator_rejects_payload_leak_fields_even_when_metadata_matches(
    capsys, tmp_path
):
    report_path = tmp_path / "owner-runtime-smoke-report.json"
    report_path.write_text(
        json.dumps(
            {
                "harness_status": "verified_infected",
                "malicious_detection_verified": True,
                "api_calls_attempted": True,
                "payload_committed_to_repo": False,
                "raw_payload_logged": False,
                "input_source": "stdin",
                "required_owner_input_missing": False,
                "test_signature_text": "redacted-placeholder",
                "scan_result_summary": {
                    "scanner_name": "clamav-clamd",
                    "scan_status": "completed",
                    "scan_verdict": "infected",
                    "matched_signature": "Eicar-Test-Signature",
                    "metadata_boundary": "metadata_only_no_raw_bytes_no_download_url",
                    "encoded_payload": "redacted-placeholder",
                },
            }
        ),
        encoding="utf-8",
    )

    exit_code = main(["--validate-owner-runtime-smoke-report", str(report_path)])

    assert exit_code == 5
    payload = json.loads(capsys.readouterr().out)
    assert payload["validation_status"] == "rejected"
    assert payload["accepted_owner_runtime_smoke"] is False
    assert payload["forbidden_payload_fields"] == [
        "scan_result_summary.encoded_payload",
        "test_signature_text",
    ]
    assert "forbidden payload field present: test_signature_text" in payload[
        "missing_or_failed_checks"
    ]
    assert (
        "forbidden payload field present: scan_result_summary.encoded_payload"
        in payload["missing_or_failed_checks"]
    )
    assert "redacted-placeholder" not in json.dumps(payload, sort_keys=True)


def test_owner_runtime_smoke_validator_rejects_unknown_fields_even_when_metadata_matches(
    capsys, tmp_path
):
    report_path = tmp_path / "owner-runtime-smoke-report.json"
    report_path.write_text(
        json.dumps(
            {
                "harness_status": "verified_infected",
                "malicious_detection_verified": True,
                "api_calls_attempted": True,
                "payload_committed_to_repo": False,
                "raw_payload_logged": False,
                "input_source": "stdin",
                "required_owner_input_missing": False,
                "template_status": "not_runtime_evidence",
                "scan_result_summary": {
                    "scanner_name": "clamav-clamd",
                    "scan_status": "completed",
                    "scan_verdict": "infected",
                    "matched_signature": "Eicar-Test-Signature",
                    "metadata_boundary": "metadata_only_no_raw_bytes_no_download_url",
                    "extra_note": "unexpected",
                },
            }
        ),
        encoding="utf-8",
    )

    exit_code = main(["--validate-owner-runtime-smoke-report", str(report_path)])

    assert exit_code == 5
    payload = json.loads(capsys.readouterr().out)
    assert payload["validation_status"] == "rejected"
    assert payload["accepted_owner_runtime_smoke"] is False
    assert payload["unexpected_fields"] == [
        "scan_result_summary.extra_note",
        "template_status",
    ]
    assert "unexpected field present: template_status" in payload[
        "missing_or_failed_checks"
    ]
    assert "unexpected field present: scan_result_summary.extra_note" in payload[
        "missing_or_failed_checks"
    ]
    assert payload["non_claims"]["production_malware_scanning_evidence"] is False


def test_owner_runtime_smoke_validator_rejects_not_configured_or_payload_leaky_report(
    capsys, tmp_path
):
    report_path = tmp_path / "owner-runtime-smoke-report.json"
    report_path.write_text(
        json.dumps(
            {
                "harness_status": "not_configured",
                "malicious_detection_verified": False,
                "api_calls_attempted": False,
                "payload_committed_to_repo": True,
                "raw_payload_logged": True,
                "input_source": "environment",
                "required_owner_input_missing": True,
                "scan_result_summary": None,
            }
        ),
        encoding="utf-8",
    )

    exit_code = main(["--validate-owner-runtime-smoke-report", str(report_path)])

    assert exit_code == 5
    payload = json.loads(capsys.readouterr().out)
    assert payload["validation_status"] == "rejected"
    assert payload["accepted_owner_runtime_smoke"] is False
    assert "harness_status must be verified_infected" in payload[
        "missing_or_failed_checks"
    ]
    assert "payload_committed_to_repo must be false" in payload[
        "missing_or_failed_checks"
    ]
    assert "raw_payload_logged must be false" in payload["missing_or_failed_checks"]
    assert payload["non_claims"]["production_malware_scanning_evidence"] is False
