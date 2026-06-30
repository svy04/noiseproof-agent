# Source-policy PDF Download and Hash

Phase marker: `real_world_pdf_fixture_source_policy_download_hash_v0`.

This review records temporary owner-runtime download/hash metadata for selected
source-policy-reviewed real-world PDF candidates from
`targeted_real_world_pdf_fixture_expansion_v0`.

It is download/hash metadata only.

It does not parse PDFs.

## Inputs

```text
source_plan -> examples/pdf-extraction-quality/targeted-real-world-pdf-fixture-expansion-plan.json
manifest -> examples/pdf-extraction-quality/source-policy-download-hash-observations.json
generated_report -> docs/evaluation/source-policy-download-hash-report.md
previous_gate -> targeted_real_world_pdf_fixture_expansion_v0
```

## Result

```text
download_hash_status -> passed_with_blocked_candidates
candidate_count -> 6
downloaded_fixture_count -> 3
blocked_fixture_count -> 2
external_route_count -> 1
runtime_work_performed -> true
pdf_downloads_performed -> true
parser_calls_performed -> false
ocr_calls_performed -> false
table_extraction_calls_performed -> false
llm_calls_performed -> false
binary_files_committed -> false
download_cache_committed -> false
raw_text_committed -> false
can_claim_download_hash_metadata -> true
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_pdf_parse_observation_v0
```

## Downloaded and Hashed

```text
eia_steo_full_rendered_visual_fidelity_candidate
bea_wp2022_10_labeled_layout_candidate
nara_911_mfr_00282_no_native_text_candidate
```

## Blocked

```text
bls_mlr_2011_06_reading_order_candidate -> HTTP 403
bls_beyond_numbers_figures_candidate -> HTTP 403
```

## External Route

```text
github_issue_1_external_reviewer_route
```

## Boundary

This is download/hash metadata only.

No external PDF binaries are committed.

No download cache is committed.

No raw text is committed.

No screenshots or page images are committed.

It is not robust PDF extraction evidence.

It is not arbitrary-market PDF parsing evidence.

It is not OCR quality evidence.

It is not table extraction benchmark evidence.

It is not layout fidelity evidence.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.
