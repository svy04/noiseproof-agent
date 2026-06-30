# Source-policy No-native-text OCR Transcript Reference Plan

Phase marker: `source_policy_no_native_text_ocr_transcript_reference_plan_v0`.

## Evidence Route

- Spec: `docs/specs/2026-07-01-source-policy-no-native-text-ocr-transcript-reference-plan.md`
- JSON: `examples/pdf-extraction-quality/source-policy-no-native-text-ocr-transcript-reference-plan.json`
- Report: `docs/evaluation/source-policy-no-native-text-ocr-transcript-reference-plan-report.md`
- CLI: `app.services.source_policy_no_native_text_ocr_transcript_reference_plan_command`
- Test: `apps/api/tests/test_source_policy_no_native_text_ocr_transcript_reference_plan.py`

## Current Result

```text
plan_status -> planned_transcript_reference_contract
previous_gate -> source_policy_no_native_text_ocr_marker_proxy_eval_v0
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
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
can_claim_transcript_reference_plan -> true
can_claim_transcript_reference_pack -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_no_native_text_ocr_transcript_reference_pack_v0
```

## What This Enables

This gate records the minimum reference boundary that must exist before true
OCR quality metrics can be considered for the preserved NARA no-native-text
route.

It can support the narrow claim that the route now has a source-policy-reviewed
plan for an owner-approved page-level transcript reference pack.

## What This Does Not Enable

This is not OCR quality evidence.

This is not CER/WER support.

This is not a reference transcript.

This is not robust PDF extraction evidence.

This is not arbitrary-market PDF parsing evidence.

This is not rendered visual fidelity evidence.

This is not image/chart interpretation evidence.

This is not external reviewer feedback.

This is not product-complete.

## Boundary

The transcript reference plan does not collect, inspect, commit, or publish raw
OCR text, raw reference text, source PDF binaries, page images, screenshots, or
a full reference transcript.

The next useful gate is
`source_policy_no_native_text_ocr_transcript_reference_pack_v0`, which should
create only a source-policy-reviewed and owner-approved reference pack if the
rights and review boundary remain safe.
