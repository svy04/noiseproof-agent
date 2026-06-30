# Real-world Layout Fidelity Evidence Gate

Phase marker: real_world_layout_fidelity_evidence_gate_v0.

This report records sanitized PyMuPDF block and bbox metadata for one temporary owner-runtime BEA PDF download.

It is real-world layout metadata sanity evidence, not robust PDF extraction evidence.

raw text is not committed.

## Gate Result

layout_gate_status -> passed
previous_gate -> real_world_ocr_evidence_gate_v0
observed_fixture_count -> 1
layout_observed_fixture_count -> 1
total_page_count -> 30
observed_page_count -> 1
total_block_count -> 20
total_text_block_count -> 16
total_image_block_count -> 0
total_text_blocks_with_bbox_in_page_bounds -> 16
expected_markers_found_count -> 7
expected_marker_order_observed -> true
has_real_world_layout_fidelity_evidence -> true
can_claim_real_world_layout_fidelity_evidence -> true
can_claim_robust_pdf_extraction -> false

## Publishers

- U.S. Bureau of Economic Analysis

## Fixtures

| Fixture | Publisher | Pages | Observed pages | Blocks | Text blocks | BBox-in-bounds | Marker hits | SHA-256 |
|---|---|---:|---:|---:|---:|---:|---:|---|
| bea_open_source_software_innovation_wp_2022_10 | U.S. Bureau of Economic Analysis | 30 | 1 | 20 | 16 | 16 | 7 | c95fe4445f42271d90b233944078fcbba76c75dab93ed678e8c08f721797ad83 |

## Passed Checks

- real_world_layout_metadata_observed
- bbox_page_bounds_sanity_observed
- expected_marker_order_sanity_observed
- source_policy_visible
- sha256_visible
- raw_block_text_not_committed
- page_images_not_committed

## Remaining Blocked Reasons

- robust_pdf_generalization_missing
- arbitrary_market_pdf_coverage_missing

## Warnings

- PyMuPDF get_text('blocks'), get_text('dict'), and sorted text extraction produced layout metadata for one temporary owner-runtime BEA PDF download.
- The PDF binary, download cache, local path, raw extracted text, raw block text, screenshots, and rendered page images are not committed.
- This gate records one real-world layout metadata sanity observation only; robust PDF extraction remains unproven.
- Expected marker ordering is a bounded sanity check, not a general reading-order or visual-fidelity benchmark.

## Next Gate

- robust_pdf_extraction_generalization_gap_review_v0

## Boundary Notes

- real-world layout fidelity evidence
- single BEA fixture observation
- sanitized layout metadata only
- no external PDF binaries committed
- no download cache committed
- no raw extracted text committed
- no raw block text committed
- no page images committed
- not robust PDF extraction evidence
- not arbitrary-market PDF parsing evidence
- not arbitrary-market layout fidelity evidence
- not natural reading order correctness evidence
- not rendered visual fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a deterministic report over one sanitized owner-runtime layout metadata observation.

It does not commit external PDF binaries, download caches, local paths, raw extracted text, raw block text, screenshots, or rendered page images.

It does not prove robust PDF extraction, arbitrary-market PDF parsing reliability, arbitrary-market layout fidelity, natural reading order correctness, or rendered visual fidelity.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
