# Default PdfParser Table Adapter Metadata

Status: implemented.

Phase marker: default PdfParser table adapter metadata v0.

## Purpose

Make table-adapter output visible from the default `PdfParser` metadata for
digital PDFs where PyMuPDF reports table candidates.

This closes a narrow inspectability gap: the repository already had a tiny
PyMuPDF table adapter and route-level proof for `quality_table_adapter`, but the
default parser metadata still forced reviewers to inspect a separate smoke
runner to see extracted table rows. This gate keeps the extraction claim
bounded while making the adapter handoff easier to inspect.

## Source-first Basis

Primary PyMuPDF references:

- https://pymupdf.readthedocs.io/en/latest/page.html
- https://pymupdf.readthedocs.io/en/latest/the-basics.html

The implementation follows the existing PyMuPDF `Page.find_tables()` /
`Table.extract()` path already isolated in
`packages/ingestion/pdf_quality/table_adapter.py`.

## Implemented

```text
packages/ingestion/parsers/pdf.py
packages/ingestion/pdf_quality/table_adapter.py
apps/api/tests/test_pdf_extraction_quality.py
apps/api/tests/test_docs.py
```

When `PdfParser` sees one or more table candidates in a digital PDF, it now
adds:

```text
default_pdf_parser_table_adapter_metadata -> true
table_adapter
table_adapter_boundary
table_adapter_extraction_performed
```

Observed deterministic fixture markers:

```text
parser -> pdf-pymupdf
metadata.robust_pdf_extraction -> false
metadata.table_candidate_count -> positive
metadata.table_extraction_performed remains false
table_adapter.table_extraction_engine -> pymupdf-find_tables-extract
table_adapter.table_extraction_performed -> true
table_adapter.robust_pdf_extraction -> false
table_adapter.extracted_table_rows -> [[Segment, Growth], [Enterprise, 12%]]
table_adapter.table_rows_extracted -> 2
table_adapter.table_cell_count -> 4
```

## Boundary

This is metadata visibility for the existing adapter output.

It is not robust PDF extraction evidence.
It is not robust PDF extraction implementation.
It is not OCR implementation.
It is not layout fidelity evidence.
It is not table extraction evidence for arbitrary market PDFs.
It does not make `metadata.table_extraction_performed` true.
It does not prove extraction quality on external PDFs.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not product-complete.

## Next Gate

Next gate: route/runtime proof that uploaded PDF handoff surfaces preserve this
default parser table-adapter metadata, remote verification after push, external
reviewer feedback v0 if qualifying outside feedback exists, or another
source-first product gate selected from the current repository state.
