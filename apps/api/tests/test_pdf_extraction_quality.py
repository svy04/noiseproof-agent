import json
from pathlib import Path
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.pdf_quality.evaluator import evaluate_pdf_extraction_quality
from packages.ingestion.pdf_quality.fixture import (
    load_pdf_extraction_quality_fixture,
    summarize_pdf_extraction_quality_fixture,
)
from packages.ingestion.pdf_quality.observation import (
    pdf_parse_result_to_quality_observation,
)
from packages.ingestion.pdf_quality.report import build_pdf_extraction_quality_report
from packages.ingestion.parsers.pdf import PdfParser
from packages.ingestion.types import ParseInput


def test_pdf_extraction_quality_fixture_loader_keeps_boundaries_visible():
    fixture = load_pdf_extraction_quality_fixture(
        REPO_ROOT / "examples/pdf-extraction-quality"
    )

    assert fixture.packet == "pdf_extraction_quality_fixture_packet_v0"
    assert fixture.binary_pdf_fixtures_included is False
    assert fixture.robust_pdf_extraction_claimed is False
    assert fixture.quality_gate_required_before_robust_claim is True
    assert len(fixture.fixtures) == 7
    assert fixture.fixtures[0].fixture_id == "born_digital_text"

    summary = summarize_pdf_extraction_quality_fixture(fixture)

    assert summary["fixture_count"] == 7
    assert summary["binary_pdf_fixtures_included"] is False
    assert summary["robust_pdf_extraction_claimed"] is False
    assert summary["quality_gate_required_before_robust_claim"] is True
    assert "table_heavy_report" in summary["fixture_ids"]
    assert "scanned_image_pdf" in summary["fixture_ids"]
    assert "page_coverage" in summary["quality_metrics"]
    assert summary["claim_boundary"] == (
        "manifest_only_not_robust_pdf_extraction_evidence"
    )


def test_pdf_extraction_quality_evaluator_scores_observations_without_robust_claim():
    fixture = load_pdf_extraction_quality_fixture(
        REPO_ROOT / "examples/pdf-extraction-quality"
    )
    observations = {
        "born_digital_text": {
            "extracted_text": "company revenue increased and source date visible",
            "warnings": ["robust PDF extraction is not claimed"],
            "page_count": 2,
            "extracted_page_count": 2,
            "empty_page_count": 0,
            "failure_case_candidate": None,
        },
        "table_heavy_report": {
            "extracted_text": "quarterly volume table with region row label",
            "warnings": ["table candidate detection is not table extraction"],
            "page_count": 1,
            "extracted_page_count": 1,
            "table_rows_extracted": 0,
            "failure_case_candidate": None,
        },
        "encrypted_pdf": {
            "extracted_text": "",
            "warnings": ["password required"],
            "page_count": 1,
            "extracted_page_count": 0,
            "failure_case_candidate": "pdf_encrypted_requires_password",
        },
    }

    result = evaluate_pdf_extraction_quality(fixture, observations)

    assert result["claim_boundary"] == (
        "manifest_metric_only_not_robust_pdf_extraction"
    )
    assert result["robust_pdf_extraction_claimed"] is False
    assert result["aggregate"]["observed_fixture_count"] == 3
    assert result["aggregate"]["not_evaluated_fixture_count"] == 4
    assert result["per_fixture"]["born_digital_text"]["status"] == "evaluated"
    assert result["per_fixture"]["born_digital_text"]["expected_span_recall"] == 1.0
    assert result["per_fixture"]["born_digital_text"]["warning_correctness"] == 1.0
    assert result["per_fixture"]["encrypted_pdf"][
        "failure_case_candidate_correctness"
    ] == 1.0
    assert result["per_fixture"]["scanned_image_pdf"]["status"] == "not_evaluated"
    assert "not robust PDF extraction evidence" in result["boundary_notes"]
    assert "not OCR evidence" in result["boundary_notes"]
    assert "not table extraction evidence" in result["boundary_notes"]


def test_pdf_extraction_quality_report_matches_committed_artifact():
    fixture_root = REPO_ROOT / "examples/pdf-extraction-quality"
    fixture = load_pdf_extraction_quality_fixture(fixture_root)
    observations = json.loads(
        (fixture_root / "observations.json").read_text(encoding="utf-8")
    )
    evaluation = evaluate_pdf_extraction_quality(fixture, observations)

    report = build_pdf_extraction_quality_report(fixture, evaluation)
    committed_report = (
        REPO_ROOT / "docs/evaluation/pdf-extraction-quality-report.md"
    ).read_text(encoding="utf-8")

    assert report == committed_report
    assert "PDF Extraction Quality Report" in report
    assert "PDF extraction quality report v0" in report
    assert "manifest_metric_only_not_robust_pdf_extraction" in report
    assert "observed_fixture_count" in report
    assert "not_evaluated_fixture_count" in report
    assert "born_digital_text" in report
    assert "scanned_image_pdf" in report
    assert "not_evaluated" in report
    assert "not robust PDF extraction evidence" in report
    assert "not OCR evidence" in report
    assert "not table extraction evidence" in report
    assert "not hosted deployment evidence" in report


def test_pdf_extraction_quality_report_command_regenerates_committed_report(tmp_path):
    output_path = tmp_path / "pdf-extraction-quality-report.md"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.pdf_extraction_quality_report_command",
            "--fixture",
            str(REPO_ROOT / "examples/pdf-extraction-quality"),
            "--observations",
            str(REPO_ROOT / "examples/pdf-extraction-quality/observations.json"),
            "--output",
            str(output_path),
        ],
        cwd=REPO_ROOT / "apps/api",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    report = output_path.read_text(encoding="utf-8")
    committed_report = (
        REPO_ROOT / "docs/evaluation/pdf-extraction-quality-report.md"
    ).read_text(encoding="utf-8")

    assert report == committed_report
    assert "PDF extraction quality report v0" in result.stdout
    assert "manifest_metric_only_not_robust_pdf_extraction" in result.stdout
    assert "not robust PDF extraction evidence" in result.stdout


def test_pdf_extraction_quality_report_command_check_mode_accepts_current_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.pdf_extraction_quality_report_command",
            "--fixture",
            str(REPO_ROOT / "examples/pdf-extraction-quality"),
            "--observations",
            str(REPO_ROOT / "examples/pdf-extraction-quality/observations.json"),
            "--output",
            str(REPO_ROOT / "docs/evaluation/pdf-extraction-quality-report.md"),
            "--check",
        ],
        cwd=REPO_ROOT / "apps/api",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "pdf_extraction_quality_report_current" in result.stdout
    assert "byte-for-byte regeneration" in result.stdout
    assert "not robust PDF extraction evidence" in result.stdout


def test_pdf_extraction_quality_report_command_check_mode_rejects_stale_report(tmp_path):
    stale_report = tmp_path / "pdf-extraction-quality-report.md"
    stale_report.write_text("# stale\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.pdf_extraction_quality_report_command",
            "--fixture",
            str(REPO_ROOT / "examples/pdf-extraction-quality"),
            "--observations",
            str(REPO_ROOT / "examples/pdf-extraction-quality/observations.json"),
            "--output",
            str(stale_report),
            "--check",
        ],
        cwd=REPO_ROOT / "apps/api",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 3
    assert "pdf_extraction_quality_report_stale" in result.stderr
    assert "byte-for-byte regeneration mismatch" in result.stderr
    assert "not robust PDF extraction evidence" in result.stderr
    assert stale_report.read_text(encoding="utf-8") == "# stale\n"


def test_pdf_extraction_quality_report_command_fails_with_boundary_for_bad_observations(tmp_path):
    bad_observations = tmp_path / "bad-observations.json"
    bad_observations.write_text("[]", encoding="utf-8")
    output_path = tmp_path / "pdf-extraction-quality-report.md"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.pdf_extraction_quality_report_command",
            "--fixture",
            str(REPO_ROOT / "examples/pdf-extraction-quality"),
            "--observations",
            str(bad_observations),
            "--output",
            str(output_path),
        ],
        cwd=REPO_ROOT / "apps/api",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 2
    assert "pdf_extraction_quality_report_regeneration_failed" in result.stderr
    assert "observations fixture must be a JSON object" in result.stderr
    assert "not robust PDF extraction evidence" in result.stderr
    assert "Traceback" not in result.stderr
    assert not output_path.exists()


def test_pdf_quality_observation_smoke_uses_pymupdf_digital_text_without_robust_claim():
    parse_result = PdfParser().parse(
        ParseInput(
            source_type="pdf",
            content_bytes=_minimal_pdf_bytes(
                "company revenue increased and source date visible"
            ),
            filename="born-digital-smoke.pdf",
        )
    )

    observation = pdf_parse_result_to_quality_observation(parse_result)

    assert observation["parser"] == "pdf-pymupdf"
    assert observation["digital_pdf_text_extraction"] is True
    assert observation["robust_pdf_extraction"] is False
    assert observation["failure_case_candidate"] is None
    assert observation["extracted_page_count"] == 1
    assert observation["page_count"] == 1

    fixture = load_pdf_extraction_quality_fixture(
        REPO_ROOT / "examples/pdf-extraction-quality"
    )
    result = evaluate_pdf_extraction_quality(
        fixture,
        {"born_digital_text": observation},
    )

    assert result["claim_boundary"] == (
        "manifest_metric_only_not_robust_pdf_extraction"
    )
    assert result["aggregate"]["observed_fixture_count"] == 1
    assert result["aggregate"]["not_evaluated_fixture_count"] == 6
    assert result["per_fixture"]["born_digital_text"]["expected_span_recall"] == 1.0
    assert "not robust PDF extraction evidence" in result["boundary_notes"]


def test_pdf_quality_observation_smoke_keeps_table_candidates_out_of_table_extraction():
    parse_result = PdfParser().parse(
        ParseInput(
            source_type="pdf",
            content_bytes=_table_pdf_bytes(),
            filename="table-candidate-smoke.pdf",
        )
    )

    observation = pdf_parse_result_to_quality_observation(parse_result)

    assert observation["parser"] == "pdf-pymupdf"
    assert observation["digital_pdf_text_extraction"] is True
    assert observation["robust_pdf_extraction"] is False
    assert observation["table_candidate_count"] > 0
    assert observation["table_extraction_performed"] is False
    assert observation["table_rows_extracted"] == 0
    assert any(
        "does not extract table contents" in warning
        for warning in observation["warnings"]
    )

    fixture = load_pdf_extraction_quality_fixture(
        REPO_ROOT / "examples/pdf-extraction-quality"
    )
    result = evaluate_pdf_extraction_quality(
        fixture,
        {"table_heavy_report": observation},
    )

    assert result["aggregate"]["observed_fixture_count"] == 1
    assert result["aggregate"]["not_evaluated_fixture_count"] == 6
    assert result["per_fixture"]["table_heavy_report"]["table_row_coverage"] == 0.0
    assert result["per_fixture"]["table_heavy_report"]["warning_correctness"] == 1.0
    assert "not table extraction evidence" in result["boundary_notes"]


def _minimal_pdf_bytes(text: str) -> bytes:
    escaped_text = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    content_stream = f"BT /F1 12 Tf 72 720 Td ({escaped_text}) Tj ET\n".encode("ascii")
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        (
            b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            b"/Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>"
        ),
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        b"<< /Length %d >>\nstream\n" % len(content_stream)
        + content_stream
        + b"endstream",
    ]
    output = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for index, body in enumerate(objects, start=1):
        offsets.append(len(output))
        output.extend(f"{index} 0 obj\n".encode("ascii"))
        output.extend(body)
        output.extend(b"\nendobj\n")
    xref_offset = len(output)
    output.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    output.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.extend(
        (
            f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
            f"startxref\n{xref_offset}\n%%EOF\n"
        ).encode("ascii")
    )
    return bytes(output)


def _table_pdf_bytes() -> bytes:
    import pymupdf

    document = pymupdf.open()
    page = document.new_page(width=300, height=200)
    x0, y0, x1, y1 = 40, 40, 260, 120
    for x in [x0, (x0 + x1) / 2, x1]:
        page.draw_line((x, y0), (x, y1), color=(0, 0, 0), width=1)
    for y in [y0, (y0 + y1) / 2, y1]:
        page.draw_line((x0, y), (x1, y), color=(0, 0, 0), width=1)
    page.insert_text((50, 65), "Segment")
    page.insert_text((160, 65), "Growth")
    page.insert_text((50, 105), "Enterprise")
    page.insert_text((160, 105), "12%")
    content = document.tobytes()
    document.close()
    return content
