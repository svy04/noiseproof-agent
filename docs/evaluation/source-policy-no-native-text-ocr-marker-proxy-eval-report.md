# Source-policy No-native-text OCR Marker Proxy Eval

Phase marker: source_policy_no_native_text_ocr_marker_proxy_eval_v0.

This report records a bounded marker-presence proxy evaluation for the preserved NARA no-native-text OCR route.

It is not OCR quality evidence.

It is not robust PDF extraction evidence.

## Gate Result

eval_status -> marker_proxy_eval_completed
previous_gate -> source_policy_no_native_text_ocr_quality_reference_pack_v0
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
publisher -> National Archives and Records Administration
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
source_policy_url -> https://www.archives.gov/global-pages/privacy.html
reference_pack_phase_marker -> source_policy_no_native_text_ocr_quality_reference_pack_v0
ocr_execution_smoke_phase_marker -> source_policy_no_native_text_ocr_execution_smoke_v0
reference_unit_type -> marker_anchor
expected_marker_anchor_count -> 2
observed_marker_hit_count -> 2
missing_marker_anchor_count -> 0
marker_proxy_hit_rate -> 1.0
marker_proxy_threshold -> 1.0
marker_proxy_passed -> true
quality_eval_performed -> false
cer_computed -> false
wer_computed -> false
raw_reference_text_committed -> false
raw_ocr_text_committed -> false
source_pdf_committed -> false
download_cache_committed -> false
page_images_committed -> false
screenshots_committed -> false
can_claim_marker_proxy_eval -> true
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false

## Observed Marker Hits

| Marker | Hit |
|---|---:|
| commission | true |
| mfr | true |

## Missing Marker Anchors

- none

## Warnings

- This is a marker-presence proxy eval only.
- It uses committed marker-hit booleans, not raw OCR text.
- It does not include a full reference transcript.
- It cannot support CER, WER, or OCR quality claims.

## Next Gate

- source_policy_no_native_text_ocr_transcript_reference_plan_v0

## Boundary Notes

- source-policy no-native-text OCR marker proxy eval
- not OCR quality evidence
- not robust PDF extraction evidence
- not arbitrary-market PDF OCR evidence
- not arbitrary-market PDF parsing evidence
- not rendered visual fidelity evidence
- not image/chart interpretation evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a deterministic marker-presence proxy eval over committed marker-hit booleans.

It does not inspect or commit raw OCR text.

It does not contain a full page-level reference transcript and therefore cannot support CER or WER.

It does not prove OCR quality, arbitrary-market PDF OCR reliability, arbitrary-market PDF parsing reliability, layout fidelity, rendered visual fidelity, image/chart interpretation, or robust PDF extraction.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
