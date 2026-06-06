# Upload PDF Quality Preview Table Adapter

Phase marker: upload PDF quality preview table adapter v0.

Status: implemented as preview-only API response shape.

## Purpose

Expose the Phase 772 PyMuPDF table adapter through `POST /documents/upload-pdf-quality-preview` without changing the default PDF parser evidence boundary.

This gives reviewers one place to inspect digital-text coverage, parser observation metadata, and table adapter output while keeping the claims separate.

## Endpoint

```text
POST /documents/upload-pdf-quality-preview
```

## Implemented Code

```text
apps/api/app/services/upload_pdf_quality_preview.py
apps/api/app/schemas.py
apps/api/tests/test_routes.py
packages/ingestion/pdf_quality/table_adapter.py
```

## Response Marker

The response now includes:

```text
quality_table_adapter
```

Expected table adapter fields:

```text
table_extraction_engine -> pymupdf-find_tables-extract
table_extraction_performed
tables
extracted_table_rows
table_rows_extracted
table_cell_count
boundary
robust_pdf_extraction -> false
```

For the deterministic local table PDF test, `quality_table_adapter` returns:

```text
tables -> [[[Segment, Growth], [Enterprise, 12%]]]
extracted_table_rows -> [[Segment, Growth], [Enterprise, 12%]]
table_rows_extracted -> 2
table_cell_count -> 4
```

The same response keeps the default parser observation boundary visible:

```text
quality_observation.table_extraction_performed -> false
quality_summary.table_extraction_performed -> false
quality_summary.robust_pdf_extraction -> false
```

## Boundary

This is adapter output only.

This is not default PdfParser table extraction.

This is not default parser table extraction evidence.

This is not table extraction evidence for arbitrary market PDFs.

This is not robust PDF extraction evidence.

This is not OCR implementation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.

## Next Gate

Next gate: local Docker/FastAPI runtime smoke for `quality_table_adapter`, or a quality fixture/report update that evaluates a matching deterministic table fixture.
