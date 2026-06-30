# Cross-publisher Real-world PDF Fixture Gate

Phase marker: cross_publisher_real_world_pdf_fixture_gate_v0.

This report adds one EIA Short-Term Energy Outlook owner-runtime observation to the existing BEA real-world PDF matrix.

It is cross-publisher fixture coverage, not robust PDF extraction evidence.

## Gate Result

cross_publisher_gate_status -> passed
base_matrix_phase -> multi_real_world_pdf_parse_observation_matrix_v0
base_observed_fixture_count -> 3
added_observed_fixture_count -> 1
combined_observed_fixture_count -> 4
distinct_publisher_count -> 2
has_cross_publisher_coverage -> true
has_table_extraction_evidence -> false
has_ocr_evidence -> false
has_layout_fidelity_evidence -> false
can_claim_cross_publisher_real_world_pdf_fixture_coverage -> true
can_claim_robust_pdf_extraction -> false

## Added Fixture

- fixture_id: eia_steo_full_2026_06
- title: Short-Term Energy Outlook, June 2026
- publisher: U.S. Energy Information Administration
- source_url: https://www.eia.gov/outlooks/steo/pdf/steo_full.pdf
- license_source_url: https://www.eia.gov/about/copyrights_reuse.php
- page_count: 60
- text_char_count: 249238
- table_candidate_count: 58

## Publishers

- U.S. Bureau of Economic Analysis
- U.S. Energy Information Administration

## Passed Checks

- cross_publisher_coverage_visible
- source_policy_visible
- sha256_visible
- external_binary_not_committed_for_added_fixture
- download_cache_not_committed_for_added_fixture
- raw_extracted_text_not_committed_for_added_fixture

## Remaining Blocked Reasons

- table_extraction_evidence_missing
- ocr_evidence_missing
- layout_fidelity_evidence_missing

## Next Gate

- real_world_table_extraction_evidence_gate_v0

## Boundary Notes

- not robust PDF extraction evidence
- not arbitrary-market PDF parsing evidence
- not OCR evidence
- not table extraction evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a deterministic report over sanitized owner-runtime observations.

It does not commit external PDF binaries, download caches, or raw extracted text.

It does not run OCR, extract tables, prove layout fidelity, or prove arbitrary-market PDF parsing reliability.

It does not prove robust PDF extraction.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
