# PDF Binary Fixture Parser Adapter Smoke

Status: implemented.

Phase marker: PDF binary fixture parser adapter smoke v0.

## Purpose

Run the synthetic binary PDF fixtures from the Phase 778 provenance packet through the existing `PdfParser` and the tiny PyMuPDF table adapter.

This moves the binary fixture packet from file provenance into parser/adapter behavior evidence, while preserving that robust PDF extraction is still not claimed.

## Implemented Artifacts

```text
packages/ingestion/pdf_quality/binary_smoke.py
examples/pdf-extraction-quality/binary-fixtures/provenance.json
examples/pdf-extraction-quality/binary-fixtures/born-digital-text.pdf
examples/pdf-extraction-quality/binary-fixtures/deterministic-table-adapter.pdf
apps/api/tests/test_pdf_extraction_quality.py
apps/api/tests/test_docs.py
```

## Smoke Result

```text
claim_boundary -> binary_fixture_smoke_only_not_robust_pdf_extraction
fixture_count -> 2
passed_count -> 2
failed_count -> 0
```

## Binary Born-Digital Text

```text
fixture_id -> binary_born_digital_text
parser -> pdf-pymupdf
digital_pdf_text_extraction -> true
robust_pdf_extraction -> false
expected_spans_found -> true
failure_case_candidate -> None
```

## Binary Deterministic Table Adapter

```text
fixture_id -> binary_deterministic_table_adapter
parser -> pdf-pymupdf
digital_pdf_text_extraction -> true
robust_pdf_extraction -> false
table_candidate_count -> 1
table_extraction_performed -> false
table_adapter.table_extraction_engine -> pymupdf-find_tables-extract
table_adapter.table_extraction_performed -> true
table_adapter.robust_pdf_extraction -> false
table_adapter.extracted_table_rows -> [[Segment, Growth], [Enterprise, 12%]]
table_adapter.expected_table_rows_found -> true
```

## Boundary

This is local parser/adapter smoke evidence over synthetic binary fixtures only.

It is not robust PDF extraction evidence.
It is not robust PDF extraction implementation.
It is not OCR implementation.
It is not default PdfParser table extraction.
It is not table extraction evidence for arbitrary market PDFs.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not product-complete.

## Next Gate

Next gate: remote verification after push, external-reader route refresh if this smoke should become reviewer-facing, or a future runtime/API smoke that exposes binary fixture behavior without storing arbitrary uploaded files.
