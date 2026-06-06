# PDF Extraction Quality Digital-text Observation Smoke

Phase marker: PDF extraction quality digital-text observation smoke v0.

Status: implemented.

Purpose: prove that actual PyMuPDF digital-text parser output can be converted into a PDF quality observation and evaluated against the manifest without claiming robust PDF extraction.

Implemented code:

```text
packages/ingestion/pdf_quality/observation.py
packages/ingestion/parsers/pdf.py
apps/api/tests/test_pdf_extraction_quality.py
```

Observed smoke markers:

```text
parser -> pdf-pymupdf
digital_pdf_text_extraction -> true
robust_pdf_extraction -> false
observed_fixture_count -> 1
not_evaluated_fixture_count -> 6
manifest_metric_only_not_robust_pdf_extraction
```

The smoke uses a minimal born-digital PDF test payload with embedded text. It does not use OCR, table extraction, external files, or hosted runtime infrastructure.

## Boundary

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not table extraction implementation.

This is not hosted deployment evidence.

This is not product-complete.

Next recommended gate: add a committed local smoke report for digital-text parser observations, or add table-candidate observation smoke while preserving the no-table-extraction claim.
