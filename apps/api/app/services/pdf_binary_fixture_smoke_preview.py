from pathlib import Path

from app.schemas import PdfBinaryFixtureSmokePreviewOut
from packages.ingestion.pdf_quality.binary_smoke import run_pdf_binary_fixture_smoke


ROOT_DIR = Path(__file__).resolve().parents[4]
PDF_BINARY_FIXTURE_DIR = ROOT_DIR / "examples/pdf-extraction-quality/binary-fixtures"
PDF_BINARY_FIXTURE_PREVIEW_SOURCE_BOUNDARY = (
    "repo_synthetic_binary_fixtures_only_no_arbitrary_upload"
)


def preview_pdf_binary_fixture_smoke() -> PdfBinaryFixtureSmokePreviewOut:
    result = run_pdf_binary_fixture_smoke(PDF_BINARY_FIXTURE_DIR)
    table_fixture = result["per_fixture"].get("binary_deterministic_table_adapter", {})
    table_adapter = table_fixture.get("table_adapter", {})
    return PdfBinaryFixtureSmokePreviewOut(
        **result,
        warnings=[
            "PDF binary fixture smoke preview is preview-only and does not create documents, chunks, retrieval runs, Evidence Ledger entries, Noise Gate records, reports, workflow runs, or failure cases.",
            "PDF binary fixture smoke preview uses only repo synthetic binary fixtures and does not accept arbitrary uploads.",
            "PDF binary fixture smoke preview does not claim robust PDF extraction.",
        ],
        persistence_boundary="preview_only_not_persisted",
        fixture_source_boundary=PDF_BINARY_FIXTURE_PREVIEW_SOURCE_BOUNDARY,
        reviewer_summary={
            "api_surface": "GET /documents/pdf-binary-fixture-smoke-preview",
            "fixture_source_boundary": PDF_BINARY_FIXTURE_PREVIEW_SOURCE_BOUNDARY,
            "persistence_boundary": "preview_only_not_persisted",
            "claim_boundary": result["claim_boundary"],
            "fixture_count": result["fixture_count"],
            "passed_count": result["passed_count"],
            "failed_count": result["failed_count"],
            "document_count_delta": 0,
            "table_adapter_rows": table_adapter.get("extracted_table_rows", []),
        },
        response_contract={
            "contract": "pdf_binary_fixture_smoke_preview_response_contract_v0",
            "truth_scope": "repo_synthetic_binary_fixture_smoke_only",
            "not_claimed": [
                "arbitrary_uploaded_file_behavior",
                "document_persistence",
                "robust_pdf_extraction",
                "default_pdf_parser_table_extraction",
                "hosted_deployment",
                "external_reviewer_feedback",
                "product_complete",
            ],
        },
    )
