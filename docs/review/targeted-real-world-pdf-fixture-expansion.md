# Targeted Real-world PDF Fixture Expansion

Phase marker: `targeted_real_world_pdf_fixture_expansion_v0`.

This review records a source-policy-reviewed fixture expansion plan for the
missing cells from `multi_publisher_modality_stratified_pdf_eval_v0`.

It is a planning gate only.

It does not add new runtime evidence.

## Inputs

```text
plan_packet -> examples/pdf-extraction-quality/targeted-real-world-pdf-fixture-expansion-plan.json
generated_report -> docs/evaluation/targeted-real-world-pdf-fixture-expansion-report.md
previous_gate -> multi_publisher_modality_stratified_pdf_eval_v0
```

## Result

```text
plan_status -> passed
coverage_status -> planned
candidate_count -> 6
missing_cell_count -> 6
covered_missing_cell_count -> 6
downloaded_candidate_count -> 0
runtime_work_performed -> false
pdf_downloads_performed -> false
parser_calls_performed -> false
ocr_calls_performed -> false
table_extraction_calls_performed -> false
llm_calls_performed -> false
binary_files_committed -> false
raw_text_committed -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> real_world_pdf_fixture_source_policy_download_hash_v0
```

## Missing Cells Covered By Plan

```text
multi_publisher_reading_order
multi_publisher_rendered_visual_fidelity
multi_publisher_labeled_layout_ground_truth
multi_publisher_image_chart_interpretation
multi_publisher_no_extractable_text_failure
external_reviewer_validation
```

## Candidate Routes

```text
bls_mlr_2011_06_reading_order_candidate
eia_steo_full_rendered_visual_fidelity_candidate
bea_wp2022_10_labeled_layout_candidate
bls_beyond_numbers_figures_candidate
nara_911_mfr_00282_no_native_text_candidate
github_issue_1_external_reviewer_route
```

## Boundary

This is source-policy-reviewed metadata only.

It does not download PDFs, hash PDFs, parse PDFs, run OCR, extract tables, call
LLMs, commit external binaries, commit raw extracted text, commit screenshots,
or add new runtime evidence.

It is not robust PDF extraction evidence.

It is not arbitrary-market PDF parsing evidence.

It is not OCR quality evidence.

It is not table extraction benchmark evidence.

It is not layout fidelity evidence.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.
