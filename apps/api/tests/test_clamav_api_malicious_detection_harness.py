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
    signature_text = "owner-provided-runtime-only-test-signature"
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
        "NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1 "
        "<owner-provided-stdin> | "
        "uv run python -m app.services.clamav_api_malicious_detection_harness "
        "--signature-stdin --require-owner-input"
    )
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
