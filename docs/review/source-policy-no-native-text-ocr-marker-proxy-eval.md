# Source-policy No-native-text OCR Marker Proxy Eval

Phase marker: `source_policy_no_native_text_ocr_marker_proxy_eval_v0`.

## Evidence Route

- Spec: `docs/specs/2026-07-01-source-policy-no-native-text-ocr-marker-proxy-eval.md`
- JSON: `examples/pdf-extraction-quality/source-policy-no-native-text-ocr-marker-proxy-eval.json`
- Report: `docs/evaluation/source-policy-no-native-text-ocr-marker-proxy-eval-report.md`
- CLI: `app.services.source_policy_no_native_text_ocr_marker_proxy_eval_command`
- Test: `apps/api/tests/test_source_policy_no_native_text_ocr_marker_proxy_eval.py`

## Current Result

```text
eval_status -> marker_proxy_eval_completed
previous_gate -> source_policy_no_native_text_ocr_quality_reference_pack_v0
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
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
can_claim_marker_proxy_eval -> true
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_no_native_text_ocr_transcript_reference_plan_v0
```

## What This Enables

This gate records a bounded marker-presence proxy evaluation over the committed
reference anchors and committed OCR execution-smoke marker hits for the preserved
NARA no-native-text route.

It can support the narrow claim that the two accepted marker anchors were
present in the committed smoke metadata.

## What This Does Not Enable

This is not OCR quality evidence.

This is not CER/WER support.

This is not robust PDF extraction evidence.

This is not arbitrary-market PDF parsing evidence.

This is not rendered visual fidelity evidence.

This is not image/chart interpretation evidence.

This is not external reviewer feedback.

This is not product-complete.

## Boundary

The marker proxy eval uses committed booleans only. It does not inspect,
commit, or publish raw OCR text, source PDF binaries, page images, screenshots,
or a full reference transcript.

The next useful gate is
`source_policy_no_native_text_ocr_transcript_reference_plan_v0`, which should
plan the minimum owner-approved transcript/reference boundary needed before any
true OCR quality metric can be considered.
