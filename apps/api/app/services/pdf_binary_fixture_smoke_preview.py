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
    return PdfBinaryFixtureSmokePreviewOut(
        **result,
        warnings=[
            "PDF binary fixture smoke preview is preview-only and does not create documents, chunks, retrieval runs, Evidence Ledger entries, Noise Gate records, reports, workflow runs, or failure cases.",
            "PDF binary fixture smoke preview uses only repo synthetic binary fixtures and does not accept arbitrary uploads.",
            "PDF binary fixture smoke preview does not claim robust PDF extraction.",
        ],
        persistence_boundary="preview_only_not_persisted",
        fixture_source_boundary=PDF_BINARY_FIXTURE_PREVIEW_SOURCE_BOUNDARY,
    )
