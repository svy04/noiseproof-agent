# Upload PDF Quality Preview API

Phase marker: upload PDF quality preview API v0.

Status: implemented.

Purpose: expose the existing PDF parser observation path through a preview-only API so reviewers can inspect PDF quality metadata without reading tests or creating persisted records.

Endpoint:

```text
POST /documents/upload-pdf-quality-preview
```

Implemented code:

```text
apps/api/app/routes/documents.py
apps/api/app/services/upload_pdf_quality_preview.py
apps/api/app/schemas.py
apps/api/tests/test_routes.py
packages/ingestion/pdf_quality/observation.py
```

Request shape:

```text
multipart/form-data
file: PDF upload
source_type: optional, defaults to pdf for this preview surface
```

Response markers:

```text
persistence_boundary -> preview_only_not_persisted
quality_boundary -> pdf_quality_observation_preview_only_no_robust_extraction_claim
quality_observation
quality_summary
quality_table_adapter
parser -> pdf-pymupdf
robust_pdf_extraction -> false
```

Observed behavior:

- born-digital PDF input returns `digital_pdf_text_extraction -> true` and extracted text inside `quality_observation`.
- encrypted PDF input preserves `failure_case_candidate -> pdf_encrypted_requires_password`, `encrypted -> true`, and `password_required -> true`.
- `quality_summary` exposes compact reviewer-facing fields such as `page_count`, `extracted_page_count`, `password_required`, `robust_pdf_extraction`, `table_extraction_performed`, and `reviewer_boundary -> summary_only_not_robust_pdf_extraction_evidence`.
- `quality_table_adapter` exposes preview-only PyMuPDF `Page.find_tables()` / `Table.extract()` output such as `table_extraction_engine -> pymupdf-find_tables-extract`, `extracted_table_rows`, `table_rows_extracted`, and `table_cell_count`, while `quality_observation.table_extraction_performed` and `quality_summary.table_extraction_performed` remain `false`.
- the preview endpoint records an agent-run trace like the other preview endpoints, but it does not create a `Document` row.

## Boundary

This is preview-only API behavior.

This is not document persistence.

This is not new retrieval behavior.

This is not Evidence Ledger generation.

This is not decryption evidence.

This is not robust PDF extraction evidence.

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not table extraction implementation.

This is not default PdfParser table extraction.

This is not hosted deployment evidence.

This is not product-complete.

Next recommended gate: local Docker/FastAPI runtime smoke for this preview API if runtime proof is needed, or another source-first product gate selected from current repository state.
