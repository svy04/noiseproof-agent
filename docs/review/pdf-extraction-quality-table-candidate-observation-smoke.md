# PDF Extraction Quality Table-candidate Observation Smoke

Phase marker: PDF extraction quality table-candidate observation smoke v0.

Status: implemented.

Purpose: prove that PyMuPDF table-candidate diagnostics can flow into the PDF quality observation surface without being misrepresented as table extraction.

Implemented code:

```text
packages/ingestion/pdf_quality/observation.py
packages/ingestion/parsers/pdf.py
apps/api/tests/test_pdf_extraction_quality.py
```

Observed smoke markers:

```text
parser -> pdf-pymupdf
table_candidate_count -> positive
table_extraction_performed -> false
table_rows_extracted -> 0
table_row_coverage -> 0
not table extraction evidence
```

The smoke uses a minimal local PDF with drawn grid lines and text. `PdfParser` surfaces candidate table diagnostics through PyMuPDF, while the observation adapter keeps extracted table rows at zero because table extraction is not performed.

## Boundary

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not table extraction implementation.

This is not hosted deployment evidence.

This is not product-complete.

Next recommended gate: a committed table-candidate observation report, or a no-text PDF observation smoke that keeps failure candidates visible.
