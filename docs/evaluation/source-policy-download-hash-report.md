# Source-policy PDF Download and Hash

Phase marker: real_world_pdf_fixture_source_policy_download_hash_v0.

This report records temporary owner-runtime download/hash metadata for source-policy-reviewed PDF candidates.

No external PDF binaries, download caches, raw text, page images, or screenshots are committed.

It is not robust PDF extraction evidence.

## Gate Result

download_hash_status -> passed_with_blocked_candidates
previous_gate -> targeted_real_world_pdf_fixture_expansion_v0
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

## Downloaded and Hashed Fixtures

| Fixture | Missing cell | Publisher | HTTP | Content type | Bytes | SHA-256 |
|---|---|---|---:|---|---:|---|
| eia_steo_full_rendered_visual_fidelity_candidate | multi_publisher_rendered_visual_fidelity | U.S. Energy Information Administration | 200 | application/pdf | 4697437 | 21555ad32b90f7f0c8d49f87799b4956234c5505403a14102661cb247d32387f |
| bea_wp2022_10_labeled_layout_candidate | multi_publisher_labeled_layout_ground_truth | U.S. Bureau of Economic Analysis | 200 | application/pdf | 1303789 | c95fe4445f42271d90b233944078fcbba76c75dab93ed678e8c08f721797ad83 |
| nara_911_mfr_00282_no_native_text_candidate | multi_publisher_no_extractable_text_failure | National Archives and Records Administration | 200 | unknown | 2985436 | 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba |

## Blocked Download Candidates

| Fixture | Missing cell | Publisher | HTTP | Status | Boundary |
|---|---|---|---:|---|---|
| bls_mlr_2011_06_reading_order_candidate | multi_publisher_reading_order | BLS Monthly Labor Review | 403 | blocked_http_403 | HTTP 403 recorded in owner runtime; no binary committed |
| bls_beyond_numbers_figures_candidate | multi_publisher_image_chart_interpretation | U.S. Bureau of Labor Statistics | 403 | blocked_http_403 | HTTP 403 recorded in owner runtime; no binary committed |

## External Routes

- github_issue_1_external_reviewer_route -> https://github.com/svy04/noiseproof-agent/issues/1

## Blocked Reasons

- bls_mlr_candidate_blocked_http_403
- bls_beyond_numbers_candidate_blocked_http_403
- external_reviewer_validation_still_pending
- robust_pdf_claim_still_blocked

## Warnings

- Downloaded PDFs were temporary owner-runtime observations and are not committed.
- BLS candidates returned HTTP 403 in this owner runtime and remain planned or blocked, not observed.
- The NARA content type header was not application/pdf, but the downloaded bytes had a PDF magic header.
- External reviewer validation cannot be self-completed by this gate.

## Next Gate

- source_policy_pdf_parse_observation_v0

## Boundary Notes

- download/hash metadata only
- source-policy reviewed candidates only
- no external PDF binaries committed
- no download cache committed
- no raw text committed
- not robust PDF extraction evidence
- not arbitrary-market PDF parsing evidence
- not OCR quality evidence
- not table extraction benchmark evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is download/hash metadata only.

It records source URLs, policy URLs, runtime HTTP status, byte size, SHA-256, PDF magic-header status, and binary non-commitment.

It does not parse PDFs, run OCR, extract tables, call LLMs, chunk, retrieve, generate Evidence Ledger entries, run Noise Gate, or produce final reports from these PDFs.

It does not prove robust PDF extraction, arbitrary-market PDF parsing reliability, OCR quality, table extraction benchmark quality, layout fidelity, rendered visual fidelity, image/chart interpretation, or external validation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
