# Multi-publisher Modality-stratified PDF Eval

Phase marker: multi_publisher_modality_stratified_pdf_eval_v0.

This report turns the robust-PDF generalization gap review into a publisher/modality/failure-class matrix.

It is a stratified evaluation matrix, not robust PDF extraction evidence.

It does not add new runtime evidence.

## Gate Result

matrix_status -> passed
coverage_status -> partial
robust_pdf_eval_status -> blocked
previous_gate -> robust_pdf_extraction_generalization_gap_review_v0
publisher_stratum_count -> 3
modality_stratum_count -> 9
matrix_cell_count -> 12
covered_limited_cell_count -> 6
missing_cell_count -> 6
can_claim_robust_pdf_extraction -> false

## Stratification Axes

- publisher
- modality
- failure_class
- evidence_role
- rights_boundary

## Publishers

- U.S. Bureau of Economic Analysis
- U.S. Energy Information Administration
- National Archives and Records Administration

## Modalities

- digital_text
- table_extraction
- ocr_text
- layout_metadata
- reading_order
- rendered_visual_fidelity
- image_chart_interpretation
- no_extractable_text_failure
- cross_cutting_review

## Source Patterns

- docling_document_conversion_pipeline
- unstructured_partitioning_elements_and_metadata
- doclaynet_labeled_layout_ground_truth
- publaynet_document_layout_benchmark
- pubtables1m_table_structure_ground_truth
- tablebank_table_detection_recognition
- ocrd_eval_text_error_rates

## Matrix Cells

| Cell | Publisher | Modality | Failure class | Role | Status | Route | Missing evidence |
|---|---|---|---|---|---|---|---|
| bea_digital_text_parse | U.S. Bureau of Economic Analysis | digital_text | none_observed | digital_text_parse_observation | covered_limited | docs/evaluation/multi-real-world-pdf-parse-observation-report.md | publisher-diverse expected-span comparison and missed-span records |
| eia_digital_text_parse | U.S. Energy Information Administration | digital_text | none_observed | cross_publisher_digital_text_parse_observation | covered_limited | docs/evaluation/cross-publisher-real-world-pdf-fixture-gate-report.md | additional non-BEA publisher observations and missed-span records |
| bea_table_extraction | U.S. Bureau of Economic Analysis | table_extraction | table_structure_loss_unmeasured | table_extraction_observation | covered_limited | docs/evaluation/real-world-table-extraction-evidence-gate-report.md | table structure ground truth and row/cell quality checks |
| eia_table_extraction | U.S. Energy Information Administration | table_extraction | table_structure_loss_unmeasured | cross_publisher_table_extraction_observation | covered_limited | docs/evaluation/real-world-table-extraction-evidence-gate-report.md | table structure ground truth and row/cell quality checks |
| nara_ocr_text | National Archives and Records Administration | ocr_text | scanned_image_text | ocr_observation | covered_limited | docs/evaluation/real-world-ocr-evidence-gate-report.md | multi-document OCR quality checks and CER/WER-style evaluation |
| bea_layout_metadata | U.S. Bureau of Economic Analysis | layout_metadata | layout_order_unmeasured | layout_metadata_sanity_observation | covered_limited | docs/evaluation/real-world-layout-fidelity-evidence-gate-report.md | labeled layout classes, reading-order checks, and visual comparison |
| multi_publisher_reading_order | multi-publisher | reading_order | bad_reading_order | reading_order_ground_truth | missing | docs/evaluation/robust-pdf-generalization-gap-review-report.md | reading-order ground truth or reviewer-auditable ordering checks |
| multi_publisher_rendered_visual_fidelity | multi-publisher | rendered_visual_fidelity | visual_fidelity_unmeasured | rendered_visual_fidelity_comparison | missing | docs/evaluation/robust-pdf-generalization-gap-review-report.md | sanitized rendered-layout comparison with explicit rights boundary |
| multi_publisher_labeled_layout_ground_truth | multi-publisher | layout_metadata | layout_classification_unmeasured | labeled_layout_ground_truth | missing | docs/evaluation/robust-pdf-generalization-gap-review-report.md | DocLayNet/PubLayNet-style labeled layout evaluation or local equivalent |
| multi_publisher_image_chart_interpretation | multi-publisher | image_chart_interpretation | image_chart_content_unread | image_chart_interpretation_evidence | missing | docs/evaluation/robust-pdf-generalization-gap-review-report.md | image-heavy and chart-heavy fixture observations with failure candidates |
| multi_publisher_no_extractable_text_failure | multi-publisher | no_extractable_text_failure | no_extractable_text | real_world_no_extractable_text_failure | missing | docs/evaluation/robust-pdf-generalization-gap-review-report.md | source-policy-reviewed real-world no-text or encrypted failure candidates |
| external_reviewer_validation | external | cross_cutting_review | not_reviewed_externally | external_reviewer_validation | missing | https://github.com/svy04/noiseproof-agent/issues/1 | qualifying outside reviewer comment or issue review |

## Missing Cells

- multi_publisher_reading_order -> reading-order ground truth or reviewer-auditable ordering checks
- multi_publisher_rendered_visual_fidelity -> sanitized rendered-layout comparison with explicit rights boundary
- multi_publisher_labeled_layout_ground_truth -> DocLayNet/PubLayNet-style labeled layout evaluation or local equivalent
- multi_publisher_image_chart_interpretation -> image-heavy and chart-heavy fixture observations with failure candidates
- multi_publisher_no_extractable_text_failure -> source-policy-reviewed real-world no-text or encrypted failure candidates
- external_reviewer_validation -> qualifying outside reviewer comment or issue review

## Blocked Reasons

- reading_order_ground_truth_missing
- rendered_visual_fidelity_missing
- labeled_layout_ground_truth_missing
- image_chart_interpretation_missing
- real_world_no_extractable_text_failure_missing
- external_reviewer_validation_missing

## Minimum Next Evidence

- source-policy-reviewed real-world fixture expansion for missing cells
- per-cell pass/fail thresholds for digital text, tables, OCR, layout, reading order, visual fidelity, image/chart interpretation, and no-text failures
- failure case records for missed spans, bad table structure, OCR uncertainty, bad reading order, image/chart unreadability, and no-extractable-text PDFs
- no external PDF binaries, raw extracted text, screenshots, or page images committed without explicit rights review

## Passed Checks

- publisher_strata_visible
- modality_strata_visible
- matrix_cells_visible
- covered_and_missing_cells_separated
- robust_claim_blocked
- runtime_work_not_performed
- external_binaries_not_committed
- raw_text_not_committed

## Warnings

- This matrix evaluates current proof coverage only and does not add new runtime evidence.
- Covered cells are covered_limited, not proof of arbitrary-market reliability.
- Table count metrics are not table structure benchmark evidence.
- OCR expected-term hits are not OCR quality benchmark evidence.
- Synthetic failure fixtures do not close real-world failure-class coverage.

## Next Gate

- targeted_real_world_pdf_fixture_expansion_v0

## Boundary Notes

- stratified PDF evaluation matrix only
- does not add new runtime evidence
- no external PDF binaries committed
- no download cache committed
- no raw extracted text committed
- not robust PDF extraction evidence
- not arbitrary-market PDF parsing evidence
- not table extraction benchmark evidence
- not OCR quality benchmark evidence
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a deterministic matrix over existing sanitized PDF proof packets.

It does not download PDFs, parse PDFs, run OCR, extract tables, call LLMs, commit external binaries, commit raw extracted text, commit screenshots, or add new runtime evidence.

It does not prove robust PDF extraction, arbitrary-market PDF parsing reliability, table extraction benchmark quality, OCR quality benchmark performance, natural reading order correctness, rendered visual fidelity, image/chart interpretation, or external validation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
