import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
CHECK_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-dependency-check.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-ocr-dependency-check-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_dependency_check import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    build_source_policy_no_native_text_ocr_dependency_check_report,
    build_source_policy_no_native_text_ocr_dependency_check_summary,
    load_source_policy_no_native_text_ocr_dependency_check,
    probe_tesseract_dependency,
)


class _FakeCompletedProcess:
    def __init__(self, returncode: int, stdout: str = "", stderr: str = "") -> None:
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


def test_probe_tesseract_dependency_missing_keeps_paths_out():
    result = probe_tesseract_dependency(
        lookup_command=lambda name: None,
        run_command=lambda args: _FakeCompletedProcess(99, "", "should not run"),
    )

    assert result["dependency_check_status"] == "checked_missing_tesseract_command"
    assert result["tesseract_command_present"] is False
    assert result["version_check_performed"] is False
    assert result["language_list_check_performed"] is False
    assert result["eng_language_available"] is False
    assert result["local_paths_printed"] is False
    assert result["local_paths_committed"] is False
    assert result["tesseract_path_committed"] is False
    assert result["tessdata_path_committed"] is False
    assert result["ocr_execution_performed"] is False
    assert result["can_claim_ocr_dependency_available"] is False


def test_probe_tesseract_dependency_present_reports_only_sanitized_facts():
    secret_path = "C:/secret/Tesseract-OCR/tesseract.exe"

    def run_command(args):
        assert args[0] == "tesseract"
        if args[1] == "--version":
            return _FakeCompletedProcess(0, "tesseract 5.3.0\n leptonica-1.82.0\n")
        if args[1] == "--list-langs":
            return _FakeCompletedProcess(0, "List of available languages (2):\neng\nkor\n")
        raise AssertionError(args)

    result = probe_tesseract_dependency(
        lookup_command=lambda name: secret_path,
        run_command=run_command,
    )
    serialized = str(result)

    assert result["dependency_check_status"] == "checked_dependency_available"
    assert result["tesseract_command_present"] is True
    assert result["version_check_performed"] is True
    assert result["language_list_check_performed"] is True
    assert result["tesseract_version_reported"] is True
    assert result["detected_language_count"] == 2
    assert result["eng_language_available"] is True
    assert result["local_paths_printed"] is False
    assert result["local_paths_committed"] is False
    assert result["can_claim_ocr_dependency_available"] is True
    assert secret_path not in serialized


def test_source_policy_no_native_text_ocr_dependency_check_commits_missing_state():
    check = load_source_policy_no_native_text_ocr_dependency_check(CHECK_PATH)
    summary = build_source_policy_no_native_text_ocr_dependency_check_summary(check)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == "source_policy_no_native_text_ocr_readiness_review_v0"
    assert summary["dependency_check_status"] == "checked_missing_tesseract_command"
    assert summary["fixture_id"] == "nara_911_mfr_00282_no_native_text_candidate"
    assert summary["tesseract_command_present"] is False
    assert summary["version_check_performed"] is False
    assert summary["language_list_check_performed"] is False
    assert summary["eng_language_available"] is False
    assert summary["local_paths_printed"] is False
    assert summary["local_paths_committed"] is False
    assert summary["tesseract_path_committed"] is False
    assert summary["tessdata_path_committed"] is False
    assert summary["ocr_execution_performed"] is False
    assert summary["ocr_quality_eval_performed"] is False
    assert summary["can_claim_ocr_dependency_check"] is True
    assert summary["can_claim_ocr_dependency_available"] is False
    assert summary["can_claim_ocr_execution"] is False
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_source_policy_no_native_text_ocr_dependency_check_report_is_current():
    check = load_source_policy_no_native_text_ocr_dependency_check(CHECK_PATH)
    summary = build_source_policy_no_native_text_ocr_dependency_check_summary(check)
    report = build_source_policy_no_native_text_ocr_dependency_check_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text OCR Dependency Check" in report
    assert "source_policy_no_native_text_ocr_dependency_check_v0" in report
    assert "dependency_check_status -> checked_missing_tesseract_command" in report
    assert "tesseract_command_present -> false" in report
    assert "version_check_performed -> false" in report
    assert "language_list_check_performed -> false" in report
    assert "eng_language_available -> false" in report
    assert "local_paths_printed -> false" in report
    assert "local_paths_committed -> false" in report
    assert "can_claim_ocr_dependency_available -> false" in report
    assert "can_claim_ocr_execution -> false" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "source_policy_no_native_text_ocr_dependency_resolution_v0" in report
    assert "not OCR execution evidence" in report
    assert "not OCR quality evidence" in report
    assert "not robust PDF extraction evidence" in report


def test_source_policy_no_native_text_ocr_dependency_check_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_ocr_dependency_check_command",
            "--check-packet",
            str(CHECK_PATH),
            "--output",
            str(REPORT_PATH),
            "--check",
        ],
        cwd=REPO_ROOT / "apps/api",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "source_policy_no_native_text_ocr_dependency_check_report_current" in result.stdout
    assert "dependency_check_status=checked_missing_tesseract_command" in result.stdout
    assert "can_claim_ocr_dependency_available=false" in result.stdout
    assert "can_claim_ocr_execution=false" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_no_native_text_ocr_dependency_check_docs_and_surfaces_are_linked():
    review_path = (
        REPO_ROOT / "docs/review/source-policy-no-native-text-ocr-dependency-check.md"
    )
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-source-policy-no-native-text-ocr-dependency-check.md"
    )
    assert review_path.is_file()
    assert spec_path.is_file()
    assert REPORT_PATH.is_file()

    surfaces = [
        review_path.read_text(encoding="utf-8"),
        (REPO_ROOT / "README.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/MASTER-SPEC.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8"),
        (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / "docs/review/external-reader-proof-path.md").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / "docs/review/proof-gap-action-surface.md").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / "apps/api/app/services/proof_gap_registry.py").read_text(
            encoding="utf-8"
        ),
        (REPO_ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8"),
    ]

    for surface in surfaces:
        assert "source_policy_no_native_text_ocr_dependency_check_v0" in surface
        assert "source_policy_no_native_text_ocr_dependency_resolution_v0" in surface

    for boundary in [
        "not OCR dependency availability evidence",
        "not OCR execution evidence",
        "not OCR quality evidence",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not rendered visual fidelity evidence",
        "not image/chart interpretation evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in surfaces[0]
