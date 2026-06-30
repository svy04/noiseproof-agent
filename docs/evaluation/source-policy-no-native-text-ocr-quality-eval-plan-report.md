# Source-policy No-native-text OCR Quality Eval Plan

Phase marker: source_policy_no_native_text_ocr_quality_eval_plan_v0.

This report records the evaluation contract required before the preserved NARA no-native-text OCR route can make any OCR-quality claim.

It is not OCR quality evidence.

It is not robust PDF extraction evidence.

## Gate Result

plan_status -> planned_quality_eval_contract
previous_gate -> source_policy_no_native_text_ocr_execution_smoke_v0
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
publisher -> National Archives and Records Administration
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
execution_smoke_phase_marker -> source_policy_no_native_text_ocr_execution_smoke_v0
execution_smoke_run_source -> owner_runtime_pymupdf_ocr_source_policy_smoke
execution_smoke_ocr_execution_performed -> true
execution_smoke_ocr_text_char_count -> 8019
execution_smoke_expected_markers_found_count -> 2
execution_smoke_quality_eval_performed -> false
ground_truth_available -> false
reference_pack_required -> true
quality_eval_performed -> false
raw_reference_text_committed -> false
raw_ocr_text_committed -> false
source_pdf_committed -> false
download_cache_committed -> false
page_images_committed -> false
screenshots_committed -> false
marker_hits_are_quality_proxy_only -> true
can_claim_quality_eval_plan -> true
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false

## Candidate Metrics

- character_error_rate
- word_error_rate
- expected_marker_precision_recall_proxy

## Required Reference Inputs

- page_level_reference_transcript_or_accepted_spans
- reference_source_policy
- normalization_rules
- page_mapping
- source_sha256_binding
- ocr_output_acquisition_boundary
- raw_text_redaction_boundary

## Stop Conditions

- no_page_level_reference_transcript_or_accepted_spans
- no_reference_source_policy
- no_normalization_rules
- source_sha256_not_bound_to_reference_pack
- quality_score_requested_from_marker_hits_only
- quality_score_requires_committing_raw_ocr_or_reference_text

## Warnings

- This is an OCR quality-evaluation plan only.
- The previous OCR execution smoke is not OCR quality evidence.
- Expected-marker hits and OCR text counts are proxy checks only.
- A reference pack is required before any quality score can be computed.

## Next Gate

- source_policy_no_native_text_ocr_quality_reference_pack_v0

## Boundary Notes

- source-policy no-native-text OCR quality-evaluation plan
- not OCR quality evidence
- not robust PDF extraction evidence
- not arbitrary-market PDF OCR evidence
- not arbitrary-market PDF parsing evidence
- not rendered visual fidelity evidence
- not image/chart interpretation evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a deterministic plan over the previous sanitized OCR execution smoke.

The previous smoke proves only that one bounded OCR execution path ran and produced sanitized metadata.

Expected-marker hits and character counts are not recognition-quality scores.

No OCR quality evaluation is performed until a reference pack exists with source policy, page mapping, normalization rules, and raw-text redaction boundaries.

It does not commit external PDF binaries, download caches, local paths, tessdata paths, raw reference text, raw OCR text, page images, screenshots, or table rows.

It does not prove OCR quality, arbitrary-market PDF OCR reliability, arbitrary-market PDF parsing reliability, layout fidelity, rendered visual fidelity, image/chart interpretation, or robust PDF extraction.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
