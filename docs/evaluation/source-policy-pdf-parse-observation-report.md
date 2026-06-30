# Source-policy PDF Parse Observation

Phase marker: source_policy_pdf_parse_observation_v0.

This report records temporary owner-runtime PyMuPDF text/block metadata observations for source-policy-reviewed PDF candidates.

No external PDF binaries, download caches, raw text, page images, or screenshots are committed.

It is not robust PDF extraction evidence.

## Gate Result

parse_observation_status -> passed_with_no_native_text_candidate
previous_gate -> real_world_pdf_fixture_source_policy_download_hash_v0
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

## Observed Fixtures

| Fixture | Missing cell | Publisher | Status | Pages | Extracted pages | Empty pages | Text chars | Text blocks | Image blocks | Failure candidate |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| eia_steo_full_rendered_visual_fidelity_candidate | multi_publisher_rendered_visual_fidelity | U.S. Energy Information Administration | metadata_observed | 60 | 60 | 0 | 249238 | 2313 | 0 |  |
| bea_wp2022_10_labeled_layout_candidate | multi_publisher_labeled_layout_ground_truth | U.S. Bureau of Economic Analysis | metadata_observed | 30 | 30 | 0 | 60269 | 819 | 0 |  |
| nara_911_mfr_00282_no_native_text_candidate | multi_publisher_no_extractable_text_failure | National Archives and Records Administration | no_native_text_observed | 4 | 0 | 4 | 0 | 0 | 0 | no_native_text_observed |

## Blocked Download Candidates Preserved

| Fixture | Missing cell | Publisher | HTTP | Status | Boundary |
|---|---|---|---:|---|---|
| bls_mlr_2011_06_reading_order_candidate | multi_publisher_reading_order | BLS Monthly Labor Review | 403 | blocked_http_403 | HTTP 403 preserved from the download/hash gate; no binary committed |
| bls_beyond_numbers_figures_candidate | multi_publisher_image_chart_interpretation | U.S. Bureau of Labor Statistics | 403 | blocked_http_403 | HTTP 403 preserved from the download/hash gate; no binary committed |

## External Routes Preserved

- github_issue_1_external_reviewer_route -> https://github.com/svy04/noiseproof-agent/issues/1

## Blocked Reasons

- bls_mlr_candidate_blocked_http_403
- bls_beyond_numbers_candidate_blocked_http_403
- nara_candidate_has_no_native_text_without_ocr
- external_reviewer_validation_still_pending
- robust_pdf_claim_still_blocked

## Warnings

- Downloaded PDFs were temporary owner-runtime observations and are not committed.
- PyMuPDF text/block metadata was observed, but raw text was not committed.
- NARA returned no native text through PyMuPDF digital-text extraction; OCR was not attempted.
- BLS candidates remain blocked HTTP 403 observations from the prior gate.
- External reviewer validation cannot be self-completed by this gate.

## Next Gate

- source_policy_pdf_parse_quality_matrix_v0

## Boundary Notes

- source-policy PDF parse observation metadata only
- source-policy reviewed candidates only
- no external PDF binaries committed
- no download cache committed
- no raw text committed
- not robust PDF extraction evidence
- not arbitrary-market PDF parsing evidence
- not OCR quality evidence
- not table extraction benchmark evidence
- not layout fidelity evidence
- not rendered visual fidelity evidence
- not image/chart interpretation evidence
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is source-policy PDF parse observation metadata only.

It records source URLs, policy URLs, SHA-256 provenance, PyMuPDF text/block metadata, no-native-text failure candidacy, and binary non-commitment.

It does not commit raw text, run OCR, extract tables, compare rendered pages, interpret images or charts, call LLMs, chunk, retrieve, generate Evidence Ledger entries, run Noise Gate, or produce final reports from these PDFs.

It does not prove robust PDF extraction, arbitrary-market PDF parsing reliability, OCR quality, table extraction benchmark quality, layout fidelity, rendered visual fidelity, image/chart interpretation, or external validation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
