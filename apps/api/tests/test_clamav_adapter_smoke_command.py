import json
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from app.services.clamav_adapter_smoke_command import (
    build_clamav_adapter_smoke_report,
    main,
)


def test_clamav_adapter_smoke_report_is_deterministic_and_boundary_limited():
    report = build_clamav_adapter_smoke_report(binary_probe=lambda _: None)

    assert report["phase_marker"] == "uploaded raw file ClamAV adapter runtime smoke v0"
    assert report["smoke_status"] == "passed"
    assert report["real_clamav_runtime_verified"] is False
    assert report["clamav_binary_present"] is False
    assert report["claims"]["malware_scanning_evidence"] is False
    assert report["claims"]["clamav_installation_verified"] is False
    assert report["claims"]["endpoint_behavior_verified"] is False

    scenarios = {scenario["name"]: scenario for scenario in report["scenarios"]}
    assert scenarios["missing_binary"]["scan_status"] == "failed"
    assert scenarios["missing_binary"]["scan_verdict"] == "scan_error"
    assert scenarios["missing_binary"]["failure_reason"] == "missing_clamscan"
    assert scenarios["clean_output"]["scan_status"] == "completed"
    assert scenarios["clean_output"]["scan_verdict"] == "clean"
    assert scenarios["infected_output"]["scan_status"] == "completed"
    assert scenarios["infected_output"]["scan_verdict"] == "infected"
    assert scenarios["infected_output"]["matched_signature"] == "Eicar-Test-Signature"
    assert scenarios["timeout"]["scan_verdict"] == "scan_error"
    assert scenarios["timeout"]["failure_reason"] == "timeout"
    assert scenarios["unknown_return_code"]["scan_verdict"] == "scan_error"

    assert all(
        scenario["temporary_scan_path_leaked"] is False
        for scenario in report["scenarios"]
    )


def test_clamav_adapter_smoke_command_prints_json_without_real_runtime_claim(capsys):
    exit_code = main([])

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["smoke_status"] == "passed"
    assert payload["real_clamav_runtime_verified"] is False
    assert "not malware scanning evidence" in payload["boundary"]
