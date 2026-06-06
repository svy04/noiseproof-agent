# PDF Quality Deterministic Table Adapter Fixture

Status: implemented.

Phase marker: PDF quality deterministic table adapter fixture v0.

## Purpose

Add a manifest/observation fixture that lets the PDF extraction quality report score the deterministic PyMuPDF table adapter output without changing the default `PdfParser` boundary.

The existing `table_heavy_report` fixture remains a default-parser weakness marker with zero extracted table rows. This new fixture only proves that the evaluator/report surface can score adapter-provided `extracted_table_rows` when the expected cells match the deterministic local table fixture.

## Implemented Artifacts

```text
examples/pdf-extraction-quality/fixture-manifest.json
examples/pdf-extraction-quality/observations.json
examples/pdf-extraction-quality/README.md
docs/evaluation/pdf-extraction-quality-report.md
packages/ingestion/pdf_quality/report.py
apps/api/tests/test_pdf_extraction_quality.py
apps/api/tests/test_docs.py
```

## Fixture Contract

```text
fixture_id -> deterministic_table_adapter_pdf
expected_table_rows -> [[Segment, Growth], [Enterprise, 12%]]
observed_extracted_table_rows -> [[Segment, Growth], [Enterprise, 12%]]
observed_table_rows_extracted -> 2
expected_span_recall -> 1
table_cell_recall -> 1
```

## Report Markers

```text
fixture count: 8
observed_fixture_count | 4
not_evaluated_fixture_count | 4
deterministic_table_adapter_pdf | evaluated | 1 | 1 | 1 | 1
table_heavy_report | evaluated | 1 | 0 | 1 | 1
```

## Boundary

This is manifest/observation evaluator evidence only.

It is not binary PDF fixture evidence.
It is not default PdfParser table extraction.
It is not table extraction evidence for arbitrary market PDFs.
It is not robust PDF extraction evidence.
It is not robust PDF extraction implementation.
It is not OCR implementation.
It is not layout fidelity evidence.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not product-complete.

## Next Gate

Next gate: run the full local verification and remote workflows for this fixture/report update, external-reader route refresh if this proof should become reviewer-facing, or a future binary fixture gate with explicit provenance and redistribution boundaries.
