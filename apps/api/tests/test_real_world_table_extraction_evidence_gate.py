import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EVIDENCE_PATH = (
    REPO_ROOT / "examples/pdf-extraction-quality/real-world-table-extraction-evidence.json"
)
REPORT_PATH = (
    REPO_ROOT / "docs/evaluation/real-world-table-extraction-evidence-gate-report.md"
)

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.real_world_table_extraction_evidence import (
    NEXT_GATE,
    PHASE_MARKER,
    build_real_world_table_extraction_evidence_report,
    build_real_world_table_extraction_evidence_summary,
    load_real_world_table_extraction_evidence,
)


def test_real_world_table_extraction_evidence_gate_passes_without_robust_claim():
    evidence = load_real_world_table_extraction_evidence(EVIDENCE_PATH)
    summary = build_real_world_table_extraction_evidence_summary(evidence)

    assert summary["phase_marker"] == PHASE_MARKER
    assert summary["table_extraction_gate_status"] == "passed"
    assert summary["observed_fixture_count"] == 3
    assert summary["table_extraction_observed_fixture_count"] == 3
    assert summary["distinct_publisher_count"] == 2
    assert summary["publishers"] == [
        "U.S. Bureau of Economic Analysis",
        "U.S. Energy Information Administration",
    ]
    assert summary["total_table_count"] == 124
    assert summary["total_table_rows_extracted"] == 847
    assert summary["total_table_cell_count"] == 7902
    assert summary["has_cross_publisher_coverage"] is True
    assert summary["has_table_extraction_evidence"] is True
    assert summary["has_ocr_evidence"] is False
    assert summary["has_layout_fidelity_evidence"] is False
    assert summary["can_claim_real_world_table_extraction_evidence"] is True
    assert summary["can_claim_robust_pdf_extraction"] is False
    assert summary["next_gate"] == NEXT_GATE
    assert "real_world_table_extraction_observed" in summary["passed_checks"]
    assert "cross_publisher_coverage_visible" in summary["passed_checks"]
    assert "ocr_evidence_missing" in summary["blocked_reasons"]
    assert "layout_fidelity_evidence_missing" in summary["blocked_reasons"]
    assert "table_extraction_evidence_missing" not in summary["blocked_reasons"]


def test_real_world_table_extraction_evidence_report_is_current_and_bounded():
    evidence = load_real_world_table_extraction_evidence(EVIDENCE_PATH)
    summary = build_real_world_table_extraction_evidence_summary(evidence)
    report = build_real_world_table_extraction_evidence_report(summary)

    assert report == REPORT_PATH.read_text(encoding="utf-8")
    assert "Real-world Table Extraction Evidence Gate" in report
    assert "real_world_table_extraction_evidence_gate_v0" in report
    assert "table_extraction_gate_status -> passed" in report
    assert "has_table_extraction_evidence -> true" in report
    assert "can_claim_real_world_table_extraction_evidence -> true" in report
    assert "can_claim_robust_pdf_extraction -> false" in report
    assert "real_world_ocr_evidence_gate_v0" in report
    assert "not robust PDF extraction evidence" in report
    assert "not OCR evidence" in report
    assert "not layout fidelity evidence" in report


def test_real_world_table_extraction_evidence_command_check_mode_accepts_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.real_world_table_extraction_evidence_gate_command",
            "--evidence",
            str(EVIDENCE_PATH),
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
    assert "real_world_table_extraction_evidence_gate_report_current" in result.stdout
    assert "table_extraction_gate_status=passed" in result.stdout
    assert "not robust PDF extraction evidence" in result.stdout


def test_real_world_table_extraction_evidence_docs_and_proof_surface_are_linked():
    review_path = REPO_ROOT / "docs/review/real-world-table-extraction-evidence-gate.md"
    spec_path = (
        REPO_ROOT
        / "docs/specs/2026-06-30-real-world-table-extraction-evidence-gate.md"
    )
    assert review_path.is_file()
    assert spec_path.is_file()
    assert REPORT_PATH.is_file()

    review = review_path.read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    master_spec = (REPO_ROOT / "docs/MASTER-SPEC.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    registry = (REPO_ROOT / "apps/api/app/services/proof_gap_registry.py").read_text(
        encoding="utf-8"
    )

    for surface in [review, readme, goal, master_spec, runbook, portfolio, registry]:
        assert "real_world_table_extraction_evidence_gate_v0" in surface
        assert "real_world_ocr_evidence_gate_v0" in surface

    for boundary in [
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF parsing evidence",
        "not OCR evidence",
        "not layout fidelity evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in review
