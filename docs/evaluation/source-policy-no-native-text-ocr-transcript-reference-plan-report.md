# Source-policy No-native-text OCR Transcript Reference Plan

Phase marker: source_policy_no_native_text_ocr_transcript_reference_plan_v0.

This report records the bounded reference boundary needed before true OCR quality metrics can be considered for the preserved NARA no-native-text route.

It is not OCR quality evidence.

It is not CER/WER support.

It is not robust PDF extraction evidence.

## Gate Result

plan_status -> planned_transcript_reference_contract
previous_gate -> source_policy_no_native_text_ocr_marker_proxy_eval_v0
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
publisher -> National Archives and Records Administration
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
source_policy_url -> https://www.archives.gov/global-pages/privacy.html
marker_proxy_eval_phase_marker -> source_policy_no_native_text_ocr_marker_proxy_eval_v0
reference_unit_type -> page_level_transcript_plan
target_page_count -> 4
minimum_reference_pages -> 4
required_reference_unit_count -> 6
owner_approval_required -> true
source_policy_review_required -> true
full_reference_transcript_required -> true
full_reference_transcript_available -> false
transcript_collection_performed -> false
reference_pack_created -> false
quality_eval_performed -> false
cer_computed -> false
wer_computed -> false
metric_candidates_status -> blocked_until_reference_transcript_exists
raw_reference_text_committed -> false
raw_ocr_text_committed -> false
source_pdf_committed -> false
download_cache_committed -> false
page_images_committed -> false
screenshots_committed -> false
can_claim_transcript_reference_plan -> true
can_claim_transcript_reference_pack -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false

## Required Future Reference Units

- source_policy_review
- owner_approval
- page_level_reference_transcript
- normalization_rules
- alignment_policy
- metric_eligibility_review

## Metric Candidates

- cer
- wer

Status: blocked_until_reference_transcript_exists.

## Warnings

- This is a transcript/reference planning contract only.
- It does not collect or commit a reference transcript.
- It does not inspect or commit raw OCR text.
- CER/WER remain blocked until transcript-level reference data exists.

## Next Gate

- source_policy_no_native_text_ocr_transcript_reference_pack_v0

## Boundary Notes

- source-policy no-native-text OCR transcript reference plan
- not OCR quality evidence
- not CER/WER support
- not robust PDF extraction evidence
- not arbitrary-market PDF OCR evidence
- not arbitrary-market PDF parsing evidence
- not rendered visual fidelity evidence
- not image/chart interpretation evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a deterministic transcript/reference planning contract only.

It does not collect, inspect, or commit a reference transcript.

It does not inspect or commit raw OCR text.

It keeps CER and WER blocked until owner-approved transcript-level reference data exists.

It does not prove OCR quality, arbitrary-market PDF OCR reliability, arbitrary-market PDF parsing reliability, layout fidelity, rendered visual fidelity, image/chart interpretation, or robust PDF extraction.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
