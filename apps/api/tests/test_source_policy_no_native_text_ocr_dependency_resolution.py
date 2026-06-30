import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
RESOLUTION_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-dependency-resolution.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-ocr-dependency-resolution-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_dependency_check import (  # noqa: E402
    probe_tesseract_dependency,
)
from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_dependency_resolution import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    build_source_policy_no_native_text_ocr_dependency_resolution_report,
    build_source_policy_no_native_text_ocr_dependency_resolution_summary,
    load_source_policy_no_native_text_ocr_dependency_resolution,
)


class _FakeCompletedProcess:
    def __init__(self, returncode: int, stdout: str = "", stderr: str = "") -> None:
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


def test_probe_tesseract_dependency_parses_version_from_stderr_without_path_leak():
    secret_path = "C:/secret/Tesseract-OCR/tesseract.exe"

    def run_command(args):
        assert args[0] == "tesseract"
        if args[1] == "--version":
            return _FakeCompletedProcess(0, "", "tesseract v5.5.0.20241111\n")
        if args[1] == "--list-langs":
            return _FakeCompletedProcess(0, "List of available languages (2):\neng\nosd\n")
        raise AssertionError(args)

    result = probe_tesseract_dependency(
        lookup_command=lambda name: secret_path,
        run_command=run_command,
    )
    serialized = str(result)

    assert result["dependency_check_status"] == "checked_dependency_available"
    assert result["tesseract_command_present"] is True
    assert result["version_check_performed"] is True
    assert result["tesseract_version_reported"] is True
    assert result["tesseract_version"] == "5.5.0.20241111"
    assert result["language_list_check_performed"] is True
    assert result["detected_language_count"] == 2
    assert result["eng_language_available"] is True
    assert result["can_claim_ocr_dependency_available"] is True
    assert secret_path not in serialized


def test_source_policy_no_native_text_ocr_dependency_resolution_commits_sanitized_availability():
    resolution = load_source_policy_no_native_text_ocr_dependency_resolution(
        RESOLUTION_PATH
    )
    summary = build_source_policy_no_native_text_ocr_dependency_resolution_summary(
        resolution
    )

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == "source_policy_no_native_text_ocr_dependency_check_v0"
    assert summary["dependency_resolution_status"] == "resolved_dependency_available"
    assert summary["installation_method"] == "winget"
    assert summary["installation_package_id"] == "tesseract-ocr.tesseract"
    assert summary["installed_package_version"] == "5.5.0.20241111"
    assert summary["codex_parent_path_inheritance_mismatch"] is True
    assert summary["owner_runtime_path_refresh_performed"] is True
    assert summary["tesseract_command_present"] is True
    assert summary["version_check_performed"] is True
    assert summary["language_list_check_performed"] is True
    assert summary["tesseract_version_reported"] is True
    assert summary["tesseract_version"] == "5.5.0.20241111"
    assert summary["detected_language_count"] == 2
    assert summary["eng_language_available"] is True
    assert summary["local_path_discovery_performed"] is True
    assert summary["local_paths_committed"] is False
    assert summary["tesseract_path_committed"] is False
    assert summary["tessdata_path_committed"] is False
    assert summary["ocr_execution_performed"] is False
    assert summary["ocr_quality_eval_performed"] is False
    assert summary["can_claim_ocr_dependency_available"] is True
    assert summary["can_claim_ocr_execution"] is False
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_source_policy_no_native_text_ocr_dependency_resolution_report_is_current_and_bounded():
    resolution = load_source_policy_no_native_text_ocr_dependency_resolution(
        RESOLUTION_PATH
    )
    summary = build_source_policy_no_native_text_ocr_dependency_resolution_summary(
        resolution
    )
    report = build_source_policy_no_native_text_ocr_dependency_resolution_report(
        summary
    )

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text OCR Dependency Resolution" in report
    assert "source_policy_no_native_text_ocr_dependency_resolution_v0" in report
    assert "dependency_resolution_status -> resolved_dependency_available" in report
    assert "installation_method -> winget" in report
    assert "installation_package_id -> tesseract-ocr.tesseract" in report
    assert "tesseract_command_present -> true" in report
    assert "version_check_performed -> true" in report
    assert "language_list_check_performed -> true" in report
    assert "eng_language_available -> true" in report
    assert "local_path_discovery_performed -> true" in report
    assert "local_paths_committed -> false" in report
    assert "tesseract_path_committed -> false" in report
    assert "tessdata_path_committed -> false" in report
    assert "can_claim_ocr_dependency_available -> true" in report
    assert "can_claim_ocr_execution -> false" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "source_policy_no_native_text_ocr_execution_plan_v0" in report
    assert "not OCR execution evidence" in report
    assert "not OCR quality evidence" in report
    assert "not robust PDF extraction evidence" in report


def test_source_policy_no_native_text_ocr_dependency_resolution_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_ocr_dependency_resolution_command",
            "--resolution-packet",
            str(RESOLUTION_PATH),
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
    assert (
        "source_policy_no_native_text_ocr_dependency_resolution_report_current"
        in result.stdout
    )
    assert "dependency_resolution_status=resolved_dependency_available" in result.stdout
    assert "can_claim_ocr_dependency_available=true" in result.stdout
    assert "can_claim_ocr_execution=false" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_no_native_text_ocr_dependency_resolution_artifacts_do_not_commit_paths_or_raw_content():
    artifacts = [
        RESOLUTION_PATH,
        REPORT_PATH,
        REPO_ROOT / "docs/review/source-policy-no-native-text-ocr-dependency-resolution.md",
        REPO_ROOT
        / "docs/specs/2026-06-30-source-policy-no-native-text-ocr-dependency-resolution.md",
    ]
    forbidden = [
        "C:\\",
        "Users\\admin",
        "tessdata_path:",
        "tesseract_path:",
        "raw_text:",
        "raw_ocr_text:",
        "raw_extracted_text:",
        "page_image:",
        "screenshot:",
    ]

    for artifact in artifacts:
        text = artifact.read_text(encoding="utf-8")
        for marker in forbidden:
            assert marker not in text


def test_source_policy_no_native_text_ocr_dependency_resolution_docs_and_surfaces_are_linked():
    review_path = (
        REPO_ROOT
        / "docs/review/source-policy-no-native-text-ocr-dependency-resolution.md"
    )
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-source-policy-no-native-text-ocr-dependency-resolution.md"
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
        assert "source_policy_no_native_text_ocr_dependency_resolution_v0" in surface
        assert "source_policy_no_native_text_ocr_execution_plan_v0" in surface

    for boundary in [
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
