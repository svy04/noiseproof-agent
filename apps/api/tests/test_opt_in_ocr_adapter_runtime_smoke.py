import hashlib
import json
from pathlib import Path
import subprocess
import sys

from app.services.opt_in_ocr_adapter_runtime_smoke_command import main


REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "examples/pdf-extraction-quality/ocr-runtime-fixtures"
PACKET_PATH = FIXTURE_ROOT / "ocr-runtime-provenance.json"

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.opt_in_ocr_adapter_runtime_smoke import (
    REQUIRED_OPT_IN_OCR_FIXTURE_IDS,
    load_opt_in_ocr_fixture_provenance,
)


def _run_harness(*args, env=None):
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.opt_in_ocr_adapter_runtime_smoke_command",
            *args,
        ],
        cwd=REPO_ROOT / "apps/api",
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


def _load_stdout_json(result):
    assert result.stdout, result.stderr
    return json.loads(result.stdout)


def test_opt_in_ocr_fixture_provenance_commits_scannable_fixture_without_robust_claim():
    packet = load_opt_in_ocr_fixture_provenance(FIXTURE_ROOT)

    assert packet["packet"] == "opt_in_ocr_adapter_runtime_smoke_fixture_v0"
    assert packet["binary_pdf_fixtures_included"] is True
    assert packet["robust_pdf_extraction_claimed"] is False
    assert packet["ocr_claim_requires_owner_runtime"] is True
    assert [item["fixture_id"] for item in packet["fixtures"]] == (
        REQUIRED_OPT_IN_OCR_FIXTURE_IDS
    )

    fixture = packet["fixtures"][0]
    assert fixture["fixture_id"] == "ocr_smoke_text_image_pdf"
    assert fixture["expected_spans"] == ["ocr smoke text"]
    assert fixture["expected_min_image_blocks"] == 1
    assert fixture["expected_digital_text"] is False
    assert fixture["robust_pdf_extraction_claimed"] is False
    assert fixture["redistribution_allowed"] is True
    assert "not robust PDF extraction evidence" in packet["boundary_notes"]
    assert "not OCR evidence until owner-runtime smoke succeeds" in packet[
        "boundary_notes"
    ]

    file_path = FIXTURE_ROOT / fixture["path"]
    assert file_path.is_file()
    content = file_path.read_bytes()
    assert hashlib.sha256(content).hexdigest() == fixture["sha256"]
    assert len(content) == fixture["size_bytes"]


def test_opt_in_ocr_packet_and_discovery_do_not_attempt_ocr_by_default():
    packet_result = _run_harness("--print-owner-runtime-smoke-packet")

    assert packet_result.returncode == 0, packet_result.stderr
    packet = _load_stdout_json(packet_result)

    assert packet["phase_marker"] == "opt_in_ocr_adapter_runtime_smoke_v0"
    assert packet["packet_status"] == "ready_for_owner_runtime_input"
    assert packet["required_runtime_env"] == {
        "NOISEPROOF_ENABLE_PYMUPDF_OCR": "true",
        "NOISEPROOF_TESSDATA_PREFIX": "owner-provided-tessdata-path",
        "CI": "false",
    }
    assert packet["api_calls_attempted"] is False
    assert packet["ocr_calls_attempted"] is False
    assert packet["tessdata_path_printed"] is False
    assert packet["non_claims"]["robust_pdf_extraction"] is False
    assert packet["non_claims"]["ocr_evidence"] is False

    discovery_result = _run_harness(
        "--discover-owner-runtime-input",
        env={"CI": "false"},
    )

    assert discovery_result.returncode == 0, discovery_result.stderr
    discovery = _load_stdout_json(discovery_result)

    assert discovery["phase_marker"] == (
        "opt-in OCR adapter owner-runtime input discovery v0"
    )
    assert discovery["owner_runtime_input_status"] == "missing_tessdata_prefix"
    assert discovery["opt_in_enabled"] is False
    assert discovery["tessdata_prefix_present"] is False
    assert discovery["tessdata_path_printed"] is False
    assert discovery["ocr_calls_attempted"] is False
    assert discovery["non_claims"]["ocr_evidence"] is False


def test_opt_in_ocr_runner_blocks_missing_input_and_repository_output_before_ocr(
    capsys,
    tmp_path,
):
    calls = []
    report_path = tmp_path / "opt-in-ocr-smoke-report.json"

    class FakeOcrAdapter:
        def extract_text_from_pdf(self, **kwargs):
            calls.append(kwargs)
            return {"text": "ocr smoke text", "engine": "fake-pymupdf-ocr"}

    missing_input_exit = main(
        ["--run-owner-runtime-smoke", "--output", str(report_path)],
        env={"NOISEPROOF_ENABLE_PYMUPDF_OCR": "true", "CI": "false"},
        ocr_adapter=FakeOcrAdapter(),
    )
    missing_input = json.loads(capsys.readouterr().out)

    assert missing_input_exit == 4
    assert missing_input["phase_marker"] == "opt_in_ocr_adapter_runtime_smoke_v0"
    assert missing_input["run_status"] == "input_not_ready"
    assert missing_input["owner_runtime_input_status"] == "missing_tessdata_prefix"
    assert missing_input["ocr_calls_attempted"] is False
    assert report_path.exists() is False
    assert calls == []

    repo_report_path = REPO_ROOT / ".tmp-opt-in-ocr-report.json"
    tessdata_dir = tmp_path / "tessdata"
    tessdata_dir.mkdir()
    try:
        repo_output_exit = main(
            ["--run-owner-runtime-smoke", "--output", str(repo_report_path)],
            env={
                "NOISEPROOF_ENABLE_PYMUPDF_OCR": "true",
                "NOISEPROOF_TESSDATA_PREFIX": str(tessdata_dir),
                "CI": "false",
            },
            ocr_adapter=FakeOcrAdapter(),
        )
    finally:
        repo_report_path.unlink(missing_ok=True)
    repo_output = json.loads(capsys.readouterr().out)

    assert repo_output_exit == 5
    assert repo_output["run_status"] == "output_path_rejected"
    assert repo_output["ocr_calls_attempted"] is False
    assert str(tessdata_dir) not in json.dumps(repo_output, sort_keys=True)
    assert calls == []


def test_opt_in_ocr_runner_writes_and_validates_metadata_report_with_fake_adapter(
    capsys,
    tmp_path,
):
    report_path = tmp_path / "opt-in-ocr-smoke-report.json"
    tessdata_dir = tmp_path / "tessdata"
    tessdata_dir.mkdir()
    calls = []

    class FakeOcrAdapter:
        def extract_text_from_pdf(self, **kwargs):
            calls.append(kwargs)
            return {
                "text": "ocr smoke text",
                "engine": "fake-pymupdf-ocr",
                "page_count": 1,
                "ocr_page_count": 1,
            }

    exit_code = main(
        ["--run-owner-runtime-smoke", "--output", str(report_path)],
        env={
            "NOISEPROOF_ENABLE_PYMUPDF_OCR": "true",
            "NOISEPROOF_TESSDATA_PREFIX": str(tessdata_dir),
            "CI": "false",
        },
        ocr_adapter=FakeOcrAdapter(),
    )

    assert exit_code == 0
    assert capsys.readouterr().out == ""
    report = json.loads(report_path.read_text(encoding="utf-8"))
    assert report["phase_marker"] == "opt_in_ocr_adapter_runtime_smoke_v0"
    assert report["run_source"] == "owner_runtime_pymupdf_ocr_smoke"
    assert report["fixture_root"] == (
        "examples/pdf-extraction-quality/ocr-runtime-fixtures"
    )
    assert report["fixture_id"] == "ocr_smoke_text_image_pdf"
    assert report["ocr_engine"] == "fake-pymupdf-ocr"
    assert report["ocr_performed"] is True
    assert report["ocr_page_count"] == 1
    assert report["expected_spans"] == ["ocr smoke text"]
    assert report["expected_spans_found"] is True
    assert report["recognized_text"] == "ocr smoke text"
    assert report["ocr_calls_attempted"] is True
    assert report["tessdata_path_printed"] is False
    assert report["tessdata_path_committed_to_repo"] is False
    assert report["robust_pdf_extraction_claimed"] is False
    assert report["can_claim_robust_pdf_extraction"] is False
    assert report["non_claims"]["image_chart_interpretation"] is False
    assert str(tessdata_dir) not in json.dumps(report, sort_keys=True)
    assert len(calls) == 1
    assert calls[0]["language"] == "eng"

    validate_exit = main(["--validate-owner-runtime-smoke-report", str(report_path)])
    validation = json.loads(capsys.readouterr().out)
    assert validate_exit == 0
    assert validation["validation_status"] == "accepted"
    assert validation["accepted_owner_runtime_smoke"] is True
    assert validation["missing_or_failed_checks"] == []
    assert validation["ocr_calls_attempted"] is False


def test_opt_in_ocr_runtime_smoke_docs_and_ci_are_wired():
    review_path = REPO_ROOT / "docs/review/opt-in-ocr-adapter-runtime-smoke.md"
    assert review_path.is_file()

    review = review_path.read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (
        REPO_ROOT / "docs/application/portfolio-index.md"
    ).read_text(encoding="utf-8")
    application_ready = (
        REPO_ROOT / "docs/review/application-ready-review.md"
    ).read_text(encoding="utf-8")
    proof_gap_registry = (
        REPO_ROOT / "apps/api/app/services/proof_gap_registry.py"
    ).read_text(encoding="utf-8")
    ci = (REPO_ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")

    assert "Opt-in OCR Adapter Runtime Smoke" in review
    assert "opt_in_ocr_adapter_runtime_smoke_v0" in review
    assert "owner_runtime_input_status -> missing_tessdata_prefix" in review
    assert "not robust PDF extraction evidence" in review
    assert "not OCR evidence until owner runtime succeeds" in review
    assert "Opt-in OCR adapter runtime smoke harness v0: implemented" in readme
    assert "Phase 878 - Opt-in OCR Adapter Runtime Smoke Harness v0" in goal
    assert "Phase 878 adds opt-in OCR adapter runtime smoke harness v0" in runbook
    assert "docs/review/opt-in-ocr-adapter-runtime-smoke.md" in portfolio
    assert "Latest opt-in OCR adapter runtime smoke harness" in application_ready
    assert "Check opt-in OCR adapter runtime input discovery missing state" in ci
    assert (
        "digital_pdf_text_diagnostics_plus_multi_fixture_gap_matrix_plus_missing_runtime_observation_pack_plus_ocr_layout_image_adapter_runtime_pack_plus_committed_ocr_layout_image_binary_fixture_provenance_plus_opt_in_ocr_adapter_runtime_smoke_harness"
        in proof_gap_registry
    )
    assert "owner_runtime_pymupdf_ocr_smoke_with_tessdata_v0" in proof_gap_registry
