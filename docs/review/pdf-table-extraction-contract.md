# PDF Table Extraction Contract

Phase marker: PDF table extraction contract v0.

Status: implemented as a fixture and evaluator contract only.

## Purpose

Define the minimum table-heavy PDF quality contract before adding a table extraction engine.

This prevents a future adapter from passing only because it reports a positive row count. A table extraction path must recover expected table cell values before it can improve the PDF quality score.

## Implemented Artifacts

```text
examples/pdf-extraction-quality/fixture-manifest.json
packages/ingestion/pdf_quality/fixture.py
packages/ingestion/pdf_quality/evaluator.py
packages/ingestion/pdf_quality/observation.py
packages/ingestion/pdf_quality/report.py
docs/evaluation/pdf-extraction-quality-report.md
apps/api/tests/test_pdf_extraction_quality.py
```

## Contract Markers

```text
table_contract_fixture_ids
table_heavy_report
expected_table_rows
table_cell_recall
table_row_coverage
```

The `table_heavy_report` fixture now includes:

```text
expected_table_rows:
  - [region, q1 volume]
  - [seoul, 120]
```

The evaluator now scores `table_cell_recall` by normalizing expected and extracted table cells. This makes cell-level recovery visible separately from `table_row_coverage`.

## Current Observed State

The committed observation fixture still records:

```text
table_rows_extracted: 0
table_cell_recall: 0
```

The generated report therefore keeps the table extraction gap visible:

```text
The table contract now records expected table cells separately from row count, so future table extraction must recover expected cell values instead of passing on positive row count alone.
```

## Boundary

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not table extraction implementation.

This is not table extraction evidence.

This is not hosted deployment evidence.

This is not product-complete.

## Next Gate

Next gate: table extraction adapter source-first review or a tiny table extraction adapter behind this contract, still without robust PDF extraction claims.
