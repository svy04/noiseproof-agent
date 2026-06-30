# Source-policy PDF Parse Observation

Phase marker: `source_policy_pdf_parse_observation_v0`.

This review records temporary owner-runtime PyMuPDF text/block metadata for the
3 source-policy-reviewed PDF candidates that passed the previous download/hash
gate.

It is parse observation metadata only.

It does not commit raw text.

It does not prove robust PDF extraction.

## Inputs

```text
download_hash_manifest -> examples/pdf-extraction-quality/source-policy-download-hash-observations.json
observation_manifest -> examples/pdf-extraction-quality/source-policy-pdf-parse-observations.json
generated_report -> docs/evaluation/source-policy-pdf-parse-observation-report.md
previous_gate -> real_world_pdf_fixture_source_policy_download_hash_v0
```

## Result

```text
parse_observation_status -> passed_with_no_native_text_candidate
candidate_count -> 6
observed_fixture_count -> 3
native_text_fixture_count -> 2
no_native_text_fixture_count -> 1
blocked_fixture_count -> 2
external_route_count -> 1
failure_case_candidate_count -> 1
total_page_count -> 94
total_extracted_page_count -> 90
total_empty_page_count -> 4
total_text_char_count -> 309507
total_text_block_count -> 3132
total_image_block_count -> 0
runtime_work_performed -> true
pdf_downloads_performed -> true
parser_calls_performed -> true
ocr_calls_performed -> false
table_extraction_calls_performed -> false
llm_calls_performed -> false
binary_files_committed -> false
download_cache_committed -> false
raw_text_committed -> false
can_claim_source_policy_pdf_parse_observation -> true
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_pdf_parse_quality_matrix_v0
```

## Observed

```text
eia_steo_full_rendered_visual_fidelity_candidate -> metadata_observed
bea_wp2022_10_labeled_layout_candidate -> metadata_observed
nara_911_mfr_00282_no_native_text_candidate -> no_native_text_observed
```

## Preserved Blocked Routes

```text
bls_mlr_2011_06_reading_order_candidate -> HTTP 403
bls_beyond_numbers_figures_candidate -> HTTP 403
github_issue_1_external_reviewer_route -> external route only
```

## Failure Candidate

```text
nara_911_mfr_00282_no_native_text_candidate
failure_type -> no_native_text_observed
root_cause -> image_or_scanned_pdf_without_native_text_layer
fix_status -> planned_not_implemented
```

## Boundary

This is source-policy PDF parse observation metadata only.

No external PDF binaries are committed.

No download cache is committed.

No raw text is committed.

No OCR is performed.

No table extraction is performed.

No rendered page comparison is performed.

No image/chart interpretation is performed.

It is not robust PDF extraction evidence.

It is not arbitrary-market PDF parsing evidence.

It is not OCR quality evidence.

It is not table extraction benchmark evidence.

It is not layout fidelity evidence.

It is not rendered visual fidelity evidence.

It is not image/chart interpretation evidence.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.
