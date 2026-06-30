import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
PLAN_PATH = (
    REPO_ROOT
    / "examples/pdf-extraction-quality/source-policy-no-native-text-ocr-execution-plan.json"
)
REPORT_PATH = (
    REPO_ROOT
    / "docs/evaluation/source-policy-no-native-text-ocr-execution-plan-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_execution_plan import (  # noqa: E402
    NEXT_GATE,
    PHASE_MARKER,
    build_source_policy_no_native_text_ocr_execution_plan_report,
    build_source_policy_no_native_text_ocr_execution_plan_summary,
    load_source_policy_no_native_text_ocr_execution_plan,
)


def test_source_policy_no_native_text_ocr_execution_plan_commits_bounded_contract():
    plan = load_source_policy_no_native_text_ocr_execution_plan(PLAN_PATH)
    summary = build_source_policy_no_native_text_ocr_execution_plan_summary(plan)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["previous_gate"] == (
        "source_policy_no_native_text_ocr_dependency_resolution_v0"
    )
    assert summary["plan_status"] == "planned_execution_contract"
    assert summary["execution_adapter"] == "pymupdf_page_get_textpage_ocr"
    assert summary["target_fixture_id"] == "nara_911_mfr_00282_no_native_text_candidate"
    assert summary["target_page_count"] == 4
    assert summary["target_empty_page_count"] == 4
    assert summary["dependency_available"] is True
    assert summary["path_refresh_required"] is True
    assert summary["opt_in_required"] is True
    assert summary["planned_ocr_language"] == "eng"
    assert summary["planned_dpi"] == 300
    assert summary["planned_full_page_ocr"] is True
    assert summary["ocr_execution_performed"] is False
    assert summary["ocr_quality_eval_performed"] is False
    assert summary["raw_ocr_text_committed"] is False
    assert summary["page_images_committed"] is False
    assert summary["screenshots_committed"] is False
    assert summary["can_claim_ocr_execution_plan"] is True
    assert summary["can_claim_ocr_execution"] is False
    assert summary["can_claim_ocr_quality"] is False
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE


def test_source_policy_no_native_text_ocr_execution_plan_report_is_current_and_bounded():
    plan = load_source_policy_no_native_text_ocr_execution_plan(PLAN_PATH)
    summary = build_source_policy_no_native_text_ocr_execution_plan_summary(plan)
    report = build_source_policy_no_native_text_ocr_execution_plan_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Source-policy No-native-text OCR Execution Plan" in report
    assert "source_policy_no_native_text_ocr_execution_plan_v0" in report
    assert "plan_status -> planned_execution_contract" in report
    assert "execution_adapter -> pymupdf_page_get_textpage_ocr" in report
    assert "dependency_available -> true" in report
    assert "opt_in_required -> true" in report
    assert "planned_ocr_language -> eng" in report
    assert "planned_dpi -> 300" in report
    assert "planned_full_page_ocr -> true" in report
    assert "ocr_execution_performed -> false" in report
    assert "ocr_quality_eval_performed -> false" in report
    assert "raw_ocr_text_committed -> false" in report
    assert "can_claim_ocr_execution_plan -> true" in report
    assert "can_claim_ocr_execution -> false" in report
    assert "can_claim_ocr_quality -> false" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "source_policy_no_native_text_ocr_execution_smoke_v0" in report
    assert "not OCR execution evidence" in report
    assert "not OCR quality evidence" in report
    assert "not robust PDF extraction evidence" in report


def test_source_policy_no_native_text_ocr_execution_plan_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.source_policy_no_native_text_ocr_execution_plan_command",
            "--plan",
            str(PLAN_PATH),
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
    assert "source_policy_no_native_text_ocr_execution_plan_report_current" in result.stdout
    assert "plan_status=planned_execution_contract" in result.stdout
    assert "can_claim_ocr_execution_plan=true" in result.stdout
    assert "can_claim_ocr_execution=false" in result.stdout
    assert "can_claim_ocr_quality=false" in result.stdout
    assert "can_claim_robust_pdf_extraction=false" in result.stdout


def test_source_policy_no_native_text_ocr_execution_plan_rejects_execution_or_raw_artifacts(tmp_path):
    plan = load_source_policy_no_native_text_ocr_execution_plan(PLAN_PATH)
    bad_plan = dict(plan)
    bad_plan["ocr_execution_performed"] = True
    bad_path = tmp_path / "bad-plan.json"
    bad_path.write_text(__import__("json").dumps(bad_plan), encoding="utf-8")

    with pytest.raises(ValueError, match="ocr_execution_performed"):
        load_source_policy_no_native_text_ocr_execution_plan(bad_path)

    raw_plan = dict(plan)
    raw_plan["raw_ocr_text"] = "forbidden"
    raw_path = tmp_path / "raw-plan.json"
    raw_path.write_text(__import__("json").dumps(raw_plan), encoding="utf-8")

    with pytest.raises(ValueError, match="raw_ocr_text"):
        load_source_policy_no_native_text_ocr_execution_plan(raw_path)


def test_source_policy_no_native_text_ocr_execution_plan_artifacts_do_not_commit_paths_or_raw_content():
    artifacts = [
        PLAN_PATH,
        REPORT_PATH,
        REPO_ROOT / "docs/review/source-policy-no-native-text-ocr-execution-plan.md",
        REPO_ROOT
        / "docs/specs/2026-06-30-source-policy-no-native-text-ocr-execution-plan.md",
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


def test_source_policy_no_native_text_ocr_execution_plan_docs_and_surfaces_are_linked():
    review_path = (
        REPO_ROOT / "docs/review/source-policy-no-native-text-ocr-execution-plan.md"
    )
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-source-policy-no-native-text-ocr-execution-plan.md"
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
        assert "source_policy_no_native_text_ocr_execution_plan_v0" in surface
        assert "source_policy_no_native_text_ocr_execution_smoke_v0" in surface

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
