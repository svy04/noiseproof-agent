# Source-policy No-native-text OCR Quality Reference Pack

Phase marker: source_policy_no_native_text_ocr_quality_reference_pack_v0.

This report records a sanitized marker-anchor reference pack for the preserved NARA no-native-text OCR route.

It is not OCR quality evidence.

It is not robust PDF extraction evidence.

## Gate Result

reference_pack_status -> marker_anchor_reference_pack
previous_gate -> source_policy_no_native_text_ocr_quality_eval_plan_v0
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
publisher -> National Archives and Records Administration
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
source_policy_url -> https://www.archives.gov/global-pages/privacy.html
quality_eval_plan_phase_marker -> source_policy_no_native_text_ocr_quality_eval_plan_v0
page_count -> 4
page_mapping_available -> true
reference_unit_type -> marker_anchor
accepted_marker_anchor_count -> 2
full_reference_transcript_available -> false
supports_marker_proxy_eval -> true
supports_cer -> false
supports_wer -> false
quality_eval_performed -> false
raw_reference_text_committed -> false
raw_ocr_text_committed -> false
source_pdf_committed -> false
download_cache_committed -> false
page_images_committed -> false
screenshots_committed -> false
can_claim_reference_pack -> true
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false

## Accepted Marker Anchors

- commission
- mfr

## Normalization Rules

- casefold -> true
- collapse_internal_whitespace -> true
- punctuation_policy -> preserve_for_future_transcript_metrics
- strip_outer_whitespace -> true
- unicode_normalization -> NFC

## Supported Metric Classes

- expected_marker_presence_proxy

## Blocked Metric Classes

- character_error_rate
- word_error_rate

## Warnings

- This is a marker-anchor reference pack only.
- It does not include a full reference transcript.
- It can support a future marker proxy check only.
- It cannot support CER or WER without full reference text.

## Next Gate

- source_policy_no_native_text_ocr_marker_proxy_eval_v0

## Boundary Notes

- source-policy no-native-text OCR marker-anchor reference pack
- not OCR quality evidence
- not robust PDF extraction evidence
- not arbitrary-market PDF OCR evidence
- not arbitrary-market PDF parsing evidence
- not rendered visual fidelity evidence
- not image/chart interpretation evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a deterministic marker-anchor reference pack over the previous quality-eval plan.

It supports only a future marker-presence proxy check.

It does not contain a full page-level reference transcript and therefore cannot support CER or WER.

It does not commit external PDF binaries, download caches, local paths, tessdata paths, raw reference text, raw OCR text, page images, screenshots, or table rows.

It does not prove OCR quality, arbitrary-market PDF OCR reliability, arbitrary-market PDF parsing reliability, layout fidelity, rendered visual fidelity, image/chart interpretation, or robust PDF extraction.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
