# Source-policy PDF Parse Quality Matrix

Phase marker: source_policy_pdf_parse_quality_matrix_v0.

This report turns source-policy PDF parse observations into a quality-claim blocker matrix.

It does not add new runtime evidence.

It is not robust PDF extraction evidence.

## Gate Result

matrix_status -> passed
quality_status -> blocked
previous_gate -> source_policy_pdf_parse_observation_v0
matrix_cell_count -> 6
observed_fixture_cell_count -> 3
native_text_observed_cell_count -> 2
no_native_text_failure_cell_count -> 1
blocked_download_cell_count -> 2
external_route_cell_count -> 1
quality_claim_ready_cell_count -> 0
quality_blocked_cell_count -> 6
runtime_work_performed -> false
pdf_downloads_performed -> false
parser_calls_performed -> false
ocr_calls_performed -> false
table_extraction_calls_performed -> false
llm_calls_performed -> false
binary_files_committed -> false
download_cache_committed -> false
raw_text_committed -> false
can_claim_source_policy_pdf_parse_quality_matrix -> true
can_claim_robust_pdf_extraction -> false
can_claim_rendered_visual_fidelity -> false
can_claim_labeled_layout_ground_truth -> false
can_claim_reading_order -> false
can_claim_image_chart_interpretation -> false
can_claim_ocr_quality -> false
can_claim_external_validation -> false

## Matrix Cells

| Cell | Missing cell | Publisher | Status | Quality ready | Missing quality evidence | Boundary |
|---|---|---|---|---|---|---|
| eia_rendered_visual_fidelity_quality_blocker | multi_publisher_rendered_visual_fidelity | U.S. Energy Information Administration | metadata_observed_quality_unproven | false | Rendered page comparison and visual-fidelity pass criteria are still missing. | metadata observation only; not robust PDF extraction evidence |
| bea_labeled_layout_ground_truth_quality_blocker | multi_publisher_labeled_layout_ground_truth | U.S. Bureau of Economic Analysis | metadata_observed_quality_unproven | false | Labeled layout ground truth and layout/reading-order comparison are still missing. | metadata observation only; not robust PDF extraction evidence |
| nara_no_native_text_quality_blocker | multi_publisher_no_extractable_text_failure | National Archives and Records Administration | no_native_text_failure_candidate | false | OCR route, OCR quality criteria, and image-aware handling evidence are still missing. | no-native-text failure candidate only; not robust PDF extraction evidence |
| bls_reading_order_download_blocker | multi_publisher_reading_order | BLS Monthly Labor Review | blocked_download | false | Source-access route or alternate policy-reviewed fixture plus reading-order ground truth is still missing. | blocked download route only; not robust PDF extraction evidence |
| bls_image_chart_download_blocker | multi_publisher_image_chart_interpretation | U.S. Bureau of Labor Statistics | blocked_download | false | Source-access route or alternate policy-reviewed fixture plus image/chart interpretation evidence is still missing. | blocked download route only; not robust PDF extraction evidence |
| github_issue_external_reviewer_blocker | external_reviewer_validation | NoiseProof GitHub issue tracker | external_review_pending | false | Qualifying outside reviewer comment and screening result are still missing. | external route only; not robust PDF extraction evidence |

## Blocked Reasons

- rendered_visual_fidelity_unproven
- labeled_layout_ground_truth_unproven
- ocr_quality_unproven_for_no_native_text_candidate
- reading_order_candidate_blocked_http_403
- image_chart_candidate_blocked_http_403
- external_reviewer_validation_pending
- robust_pdf_claim_still_blocked

## Minimum Next Evidence

- Review whether the next proof should target OCR failure routing, visual/layout ground truth, BLS access blockers, or external reviewer validation.
- Preserve the no-native-text failure candidate before claiming OCR coverage.
- Keep rendered visual fidelity, reading order, and image/chart interpretation separate from digital-text metadata.

## Warnings

- This matrix is over existing observations and does not re-download or re-parse PDFs.
- A metadata_observed cell does not prove extraction quality.
- No cell is ready for a stronger quality claim.
- External reviewer validation cannot be self-completed by this gate.

## Next Gate

- source_policy_pdf_quality_gap_review_v0

## Boundary Notes

- source-policy PDF parse quality matrix only
- does not add new runtime evidence
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

This is a deterministic quality-claim blocker matrix over the existing source-policy PDF parse observation packet.

It does not download PDFs, parse PDFs, run OCR, extract tables, compare rendered pages, interpret images or charts, call LLMs, chunk, retrieve, generate Evidence Ledger entries, run Noise Gate, or build a dashboard.

It does not commit external PDF binaries, download caches, raw text, page images, or screenshots.

It does not prove robust PDF extraction, arbitrary-market PDF parsing reliability, OCR quality, table extraction benchmark quality, layout fidelity, rendered visual fidelity, image/chart interpretation, or external validation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
