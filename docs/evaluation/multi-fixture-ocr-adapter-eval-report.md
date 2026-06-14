# Multi-fixture OCR Adapter Eval

Phase marker: multi_fixture_ocr_adapter_eval_v0.

This report combines the existing 8-role PDF fixture matrix with one sanitized owner-runtime OCR smoke observation.

It is not robust PDF extraction evidence.

## Aggregate

| Metric | Value |
|---|---:|
| base_fixture_count | 8 |
| base_observed_fixture_count | 8 |
| owner_runtime_ocr_smoke_count | 1 |
| combined_fixture_signal_count | 9 |
| owner_runtime_ocr_expected_spans_found | true |
| robust_pdf_extraction_claimed | false |
| can_claim_robust_pdf_extraction | false |

## Signal Matrix

| Signal | Status | Evidence scope | Limitation codes |
|---|---|---|---|
| born_digital_text | digital_text_observed | base_pdf_quality_fixture | digital_text_only, robust_pdf_extraction_not_explicitly_false |
| table_heavy_report | table_candidate_gap_visible | base_pdf_quality_fixture | table_rows_not_extracted, robust_pdf_extraction_not_explicitly_false |
| deterministic_table_adapter_pdf | deterministic_table_adapter_contract | base_pdf_quality_fixture | deterministic_adapter_contract_not_arbitrary_pdf_evidence, robust_pdf_extraction_not_explicitly_false |
| scanned_image_pdf | base_scanned_role_still_boundary_only | base_pdf_quality_fixture | ocr_smoke_is_adjacent_not_same_fixture, base_fixture_text_still_not_extracted |
| encrypted_pdf | expected_failure_observed | base_pdf_quality_fixture | expected_failure_boundary, robust_pdf_extraction_not_explicitly_false |
| image_heavy_pdf | image_diagnostics_only | base_pdf_quality_fixture | image_chart_interpretation_not_claimed |
| multi_column_layout_pdf | layout_diagnostics_only | base_pdf_quality_fixture | layout_fidelity_not_claimed |
| no_extractable_text_pdf | empty_text_failure_boundary_only | base_pdf_quality_fixture | empty_text_failure_boundary_only |
| ocr_smoke_text_image_pdf | owner_runtime_ocr_smoke_passed | single_synthetic_owner_runtime_fixture | single_synthetic_fixture_only, not_arbitrary_market_pdf_ocr, not_robust_pdf_extraction |

## Next Evidence Needed

- licensed real-world PDF fixture pack before arbitrary-market-PDF claims
- OCR text-span fixture expansion before scanned-image coverage claims
- image/chart interpretation adapter evidence before image-heavy truth claims
- reading-order diagnostics before layout fidelity claims
- table extraction evaluation beyond deterministic adapter contracts

## Boundary Notes

- one owner-runtime OCR smoke over one synthetic fixture only
- not robust PDF extraction evidence
- not arbitrary market PDF OCR evidence
- not image/chart interpretation evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a multi-fixture OCR adapter evaluation surface only.

The OCR evidence is limited to one synthetic owner-runtime fixture.

This is not robust PDF extraction implementation.

This is not arbitrary market PDF OCR evidence.

This is not image/chart interpretation evidence.

This is not layout fidelity evidence.

This is not hosted deployment evidence.

This is not product-complete.
