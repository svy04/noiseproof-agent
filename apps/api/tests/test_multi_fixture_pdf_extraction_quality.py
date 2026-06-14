import json
from pathlib import Path
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "examples/pdf-extraction-quality"

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.fixture import load_pdf_extraction_quality_fixture
from packages.ingestion.pdf_quality.multi_fixture import (
    build_multi_fixture_pdf_extraction_quality_matrix,
    build_multi_fixture_pdf_extraction_quality_report,
)


def _load_observations() -> dict:
    return json.loads((FIXTURE_ROOT / "observations.json").read_text(encoding="utf-8"))


def test_multi_fixture_pdf_quality_matrix_keeps_all_fixture_roles_visible():
    fixture = load_pdf_extraction_quality_fixture(FIXTURE_ROOT)
    matrix = build_multi_fixture_pdf_extraction_quality_matrix(
        fixture,
        _load_observations(),
    )

    assert matrix["phase_marker"] == "multi_fixture_pdf_extraction_quality_eval_v0"
    assert matrix["fixture_count"] == 8
    assert matrix["observed_fixture_count"] == 4
    assert matrix["gap_fixture_count"] == 4
    assert matrix["robust_pdf_extraction_claimed"] is False
    assert matrix["quality_gate_status"] == "blocked"
    assert matrix["can_claim_robust_pdf_extraction"] is False
    assert matrix["missing_runtime_observation_fixture_ids"] == [
        "scanned_image_pdf",
        "image_heavy_pdf",
        "multi_column_layout_pdf",
        "no_extractable_text_pdf",
    ]

    rows = matrix["per_fixture"]
    assert rows["born_digital_text"]["fixture_eval_state"] == "observed_passed"
    assert rows["encrypted_pdf"]["fixture_eval_state"] == "expected_failure_observed"
    assert rows["deterministic_table_adapter_pdf"]["fixture_eval_state"] == (
        "adapter_contract_observed"
    )
    assert rows["table_heavy_report"]["fixture_eval_state"] == "observed_with_gaps"
    assert "table_rows_not_extracted" in rows["table_heavy_report"]["limitation_codes"]
    assert rows["scanned_image_pdf"]["fixture_eval_state"] == "missing_runtime_observation"
    assert "ocr_adapter_not_run" in rows["scanned_image_pdf"]["limitation_codes"]
    assert rows["image_heavy_pdf"]["fixture_eval_state"] == "missing_runtime_observation"
    assert "image_chart_interpretation_not_claimed" in rows["image_heavy_pdf"][
        "limitation_codes"
    ]
    assert rows["multi_column_layout_pdf"]["fixture_eval_state"] == (
        "missing_runtime_observation"
    )
    assert "layout_fidelity_not_claimed" in rows["multi_column_layout_pdf"][
        "limitation_codes"
    ]
    assert rows["no_extractable_text_pdf"]["fixture_eval_state"] == (
        "missing_runtime_observation"
    )
    assert "failure_candidate_runtime_observation_missing" in rows[
        "no_extractable_text_pdf"
    ]["limitation_codes"]
    assert "not robust PDF extraction evidence" in matrix["boundary_notes"]


def test_multi_fixture_pdf_quality_report_matches_committed_artifact():
    fixture = load_pdf_extraction_quality_fixture(FIXTURE_ROOT)
    matrix = build_multi_fixture_pdf_extraction_quality_matrix(
        fixture,
        _load_observations(),
    )
    report = build_multi_fixture_pdf_extraction_quality_report(matrix)
    committed = (
        REPO_ROOT
        / "docs/evaluation/multi-fixture-pdf-extraction-quality-report.md"
    ).read_text(encoding="utf-8")

    assert report == committed
    assert "Multi-fixture PDF Extraction Quality Eval" in report
    assert "multi_fixture_pdf_extraction_quality_eval_v0" in report
    assert "| fixture_count | 8 |" in report
    assert "| observed_fixture_count | 4 |" in report
    assert "| gap_fixture_count | 4 |" in report
    assert "scanned_image_pdf" in report
    assert "missing_runtime_observation" in report
    assert "table_rows_not_extracted" in report
    assert "not robust PDF extraction evidence" in report
    assert "not OCR evidence" in report
    assert "not layout fidelity evidence" in report


def test_multi_fixture_pdf_quality_command_check_mode_accepts_committed_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.multi_fixture_pdf_extraction_quality_command",
            "--fixture",
            str(FIXTURE_ROOT),
            "--observations",
            str(FIXTURE_ROOT / "observations.json"),
            "--output",
            str(
                REPO_ROOT
                / "docs/evaluation/multi-fixture-pdf-extraction-quality-report.md"
            ),
            "--check",
        ],
        cwd=REPO_ROOT / "apps/api",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "multi_fixture_pdf_extraction_quality_report_current" in result.stdout
    assert "byte-for-byte regeneration" in result.stdout
    assert "not robust PDF extraction evidence" in result.stdout
