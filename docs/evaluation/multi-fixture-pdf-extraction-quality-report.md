# Multi-fixture PDF Extraction Quality Eval

Phase marker: multi_fixture_pdf_extraction_quality_eval_v0.

This report maps every PDF extraction quality fixture role to its current observation state.

It is not robust PDF extraction evidence.

## Aggregate

| Metric | Value |
|---|---:|
| fixture_count | 8 |
| observed_fixture_count | 4 |
| gap_fixture_count | 4 |
| robust_pdf_extraction_claimed | false |
| can_claim_robust_pdf_extraction | false |

## Per-fixture Matrix

| Fixture | State | Limitation codes | expected_span_recall | table_cell_recall | warning_correctness | failure_case_candidate_correctness |
|---|---|---|---:|---:|---:|---:|
| born_digital_text | observed_passed | none | 1 | 1 | 1 | 1 |
| table_heavy_report | observed_with_gaps | table_rows_not_extracted | 1 | 0 | 1 | 1 |
| deterministic_table_adapter_pdf | adapter_contract_observed | adapter_contract_not_arbitrary_pdf_evidence | 1 | 1 | 1 | 1 |
| scanned_image_pdf | missing_runtime_observation | ocr_adapter_not_run, no_runtime_scan_fixture_observation | 0 | 0 | 0 | 0 |
| encrypted_pdf | expected_failure_observed | none | 1 | 1 | 1 | 1 |
| image_heavy_pdf | missing_runtime_observation | image_chart_interpretation_not_claimed, no_runtime_image_heavy_observation | 0 | 0 | 0 | 0 |
| multi_column_layout_pdf | missing_runtime_observation | layout_fidelity_not_claimed, reading_order_not_evaluated | 0 | 0 | 0 | 0 |
| no_extractable_text_pdf | missing_runtime_observation | failure_candidate_runtime_observation_missing, no_runtime_empty_text_observation | 0 | 0 | 0 | 0 |

## Missing Runtime Observations

- `scanned_image_pdf`
- `image_heavy_pdf`
- `multi_column_layout_pdf`
- `no_extractable_text_pdf`

## Next Evidence Needed

- runtime observations for missing PDF fixture roles
- OCR adapter evidence before scanned-image text coverage
- layout-order diagnostics before multi-column fidelity claims
- image/chart interpretation boundary before image-heavy claims

## Boundary Notes

- not robust PDF extraction evidence
- not OCR evidence
- not table extraction evidence for arbitrary market PDFs
- not layout fidelity evidence
- not hosted deployment evidence
- not product-complete

## Boundary

This is a multi-fixture observation matrix only.

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not layout fidelity evidence.

This is not hosted deployment evidence.

This is not product-complete.
