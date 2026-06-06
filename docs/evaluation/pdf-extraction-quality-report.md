# PDF Extraction Quality Report

Phase marker: PDF extraction quality report v0.

This report records manifest fixture metric output for PDF extraction quality evaluation plumbing.

It is not robust PDF extraction evidence.

## Fixture

- fixture: `pdf_extraction_quality_fixture_packet_v0`
- fixture count: 7
- binary PDF fixtures included: False
- robust PDF extraction claimed: False
- claim boundary: `manifest_metric_only_not_robust_pdf_extraction`

## Aggregate Metrics

| Metric | Value |
|---|---:|
| observed_fixture_count | 3 |
| not_evaluated_fixture_count | 4 |
| page_coverage | 0.6667 |
| character_coverage | 0.6667 |
| expected_span_recall | 1 |
| table_row_coverage | 0.6667 |
| table_cell_recall | 0.6667 |
| ocr_page_coverage | 1 |
| warning_correctness | 1 |
| failure_case_candidate_correctness | 1 |

## Per-fixture Metrics

| Fixture | Status | expected_span_recall | table_cell_recall | warning_correctness | failure_case_candidate_correctness |
|---|---|---:|---:|---:|---:|
| born_digital_text | evaluated | 1 | 1 | 1 | 1 |
| table_heavy_report | evaluated | 1 | 0 | 1 | 1 |
| scanned_image_pdf | not_evaluated | 0 | 0 | 0 | 0 |
| encrypted_pdf | evaluated | 1 | 1 | 1 | 1 |
| image_heavy_pdf | not_evaluated | 0 | 0 | 0 | 0 |
| multi_column_layout_pdf | not_evaluated | 0 | 0 | 0 | 0 |
| no_extractable_text_pdf | not_evaluated | 0 | 0 | 0 | 0 |

## Boundary Notes

- not robust PDF extraction evidence
- not OCR evidence
- not table extraction evidence
- not hosted deployment evidence

## Interpretation

This report intentionally evaluates only a partial observation fixture. Four fixture roles remain `not_evaluated`, so this artifact is useful as evaluator plumbing and gap visibility, not as extraction quality evidence.

The table-heavy observation currently records zero extracted table rows. That keeps table extraction weakness visible instead of turning table candidate diagnostics into a table extraction claim.

The table contract now records expected table cells separately from row count, so future table extraction must recover expected cell values instead of passing on positive row count alone.

The scanned-image fixture is not evaluated here. OCR remains outside this gate.

## Boundary

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not table extraction implementation.

This is not hosted deployment evidence.

This is not product-complete.
