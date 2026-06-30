# Source-policy No-native-text OCR Quality Reference Pack

Phase marker: `source_policy_no_native_text_ocr_quality_reference_pack_v0`.

This review records a sanitized marker-anchor reference pack for the preserved
NARA no-native-text OCR route.

## Evidence Route

```text
docs/specs/2026-06-30-source-policy-no-native-text-ocr-quality-reference-pack.md
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-quality-reference-pack.json
docs/evaluation/source-policy-no-native-text-ocr-quality-reference-pack-report.md
apps/api/app/services/source_policy_no_native_text_ocr_quality_reference_pack_command.py
apps/api/tests/test_source_policy_no_native_text_ocr_quality_reference_pack.py
```

## Current Result

```text
reference_pack_status -> marker_anchor_reference_pack
previous_gate -> source_policy_no_native_text_ocr_quality_eval_plan_v0
source_policy_url -> https://www.archives.gov/global-pages/privacy.html
page_count -> 4
page_mapping_available -> true
reference_unit_type -> marker_anchor
accepted_marker_anchor_count -> 2
full_reference_transcript_available -> false
supports_marker_proxy_eval -> true
supports_cer -> false
supports_wer -> false
quality_eval_performed -> false
can_claim_reference_pack -> true
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_no_native_text_ocr_marker_proxy_eval_v0
```

## What This Enables

This pack can support a future marker-presence proxy evaluation over the two
accepted anchors:

```text
commission
mfr
```

## What This Does Not Enable

This pack cannot support CER or WER because it does not include a full
page-level reference transcript.

## Boundary

This is not OCR quality evidence.

This is not robust PDF extraction evidence.

This is not arbitrary-market PDF parsing evidence.

This is not table extraction benchmark evidence.

This is not layout fidelity evidence.

This is not rendered visual fidelity evidence.

This is not image/chart interpretation evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
