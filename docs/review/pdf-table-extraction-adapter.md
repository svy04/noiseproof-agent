# PDF Table Extraction Adapter

Phase marker: PDF table extraction adapter v0.

Status: source-first adapter decision implemented as a tiny local adapter.

## Purpose

Add the smallest table extraction adapter behind the Phase 771 table contract.

The goal is not robust PDF extraction. The goal is to prove that table rows can be extracted into the evaluator's `extracted_table_rows` contract without changing the default `PdfParser` proof boundary.

## Source-First Decision

Primary upstream sources checked:

- PyMuPDF `Page.find_tables()` and `Table.extract()` API reference: https://pymupdf.readthedocs.io/en/latest/page.html#Page.find_tables
- PyMuPDF table extraction recipe: https://pymupdf.readthedocs.io/en/latest/the-basics.html#extracting-tables-from-a-page
- pdfplumber table extraction methods and settings: https://github.com/jsvine/pdfplumber#extracting-tables
- Camelot documentation: https://camelot-py.readthedocs.io/en/stable/

Decision:

Use PyMuPDF first because it is already installed, already used by `PdfParser`, and exposes `Table.extract()` as rows and cells. This adds no new dependency.

Do not add pdfplumber in this gate. pdfplumber has richer table settings and visual-debugging surfaces, but adding it now would expand dependency and tuning scope before the tiny PyMuPDF adapter is inspected.

Do not add Camelot in this gate. Camelot is table-focused and exposes useful extraction metrics, but it only works for text-based PDFs and has a broader dependency/installation surface than this gate needs.

## Implemented Artifacts

```text
packages/ingestion/pdf_quality/table_adapter.py
apps/api/tests/test_pdf_extraction_quality.py
```

## Adapter Contract

The adapter exposes:

```text
table_extraction_engine: pymupdf-find_tables-extract
table_extraction_performed
tables
extracted_table_rows
table_rows_extracted
table_cell_count
table_shapes
warnings
failure_case_candidate
boundary
robust_pdf_extraction: false
```

For the local deterministic table fixture, the adapter extracts:

```text
tables:
  - [[Segment, Growth], [Enterprise, 12%]]
table_rows_extracted: 2
table_cell_count: 4
```

The adapter can feed `extracted_table_rows` into the Phase 771 evaluator contract. It does not make the existing table-heavy manifest fixture pass, because that manifest currently expects `[region, q1 volume]` and `[seoul, 120]`; this keeps fixture mismatch visible instead of treating any extracted table as a correct table.

## Boundary

This is adapter output only.

It is not wired into the default PdfParser output.

It is not table extraction evidence for arbitrary market PDFs.

It is not robust PDF extraction evidence.

It is not OCR implementation.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.

## Next Gate

Next gate: either integrate the adapter into a preview-only PDF quality route behind an explicit boundary, or add a fixture whose expected table rows match the deterministic local table fixture and regenerate the quality report.
