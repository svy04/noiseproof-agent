# Source-policy No-native-text OCR Quality Eval Plan

Phase marker: `source_policy_no_native_text_ocr_quality_eval_plan_v0`.

This review records the bounded plan for evaluating OCR quality after the
accepted source-policy no-native-text OCR execution smoke.

## Evidence Route

```text
docs/specs/2026-06-30-source-policy-no-native-text-ocr-quality-eval-plan.md
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-quality-eval-plan.json
docs/evaluation/source-policy-no-native-text-ocr-quality-eval-plan-report.md
apps/api/app/services/source_policy_no_native_text_ocr_quality_eval_plan_command.py
apps/api/tests/test_source_policy_no_native_text_ocr_quality_eval_plan.py
```

## Current Result

```text
plan_status -> planned_quality_eval_contract
previous_gate -> source_policy_no_native_text_ocr_execution_smoke_v0
execution_smoke_ocr_text_char_count -> 8019
execution_smoke_expected_markers_found_count -> 2
execution_smoke_quality_eval_performed -> false
ground_truth_available -> false
reference_pack_required -> true
quality_eval_performed -> false
marker_hits_are_quality_proxy_only -> true
can_claim_quality_eval_plan -> true
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_no_native_text_ocr_quality_reference_pack_v0
```

## Why This Gate Exists

The previous OCR execution smoke proves that one bounded PyMuPDF/Tesseract path
ran over the preserved NARA no-native-text route and produced sanitized
metadata. It does not prove recognition quality.

This gate prevents marker hits, character counts, or successful execution from
being upgraded into OCR-quality evidence.

## Required Before OCR Quality Evaluation

```text
page_level_reference_transcript_or_accepted_spans
reference_source_policy
normalization_rules
page_mapping
source_sha256_binding
ocr_output_acquisition_boundary
raw_text_redaction_boundary
```

## Candidate Metrics

```text
character_error_rate
word_error_rate
expected_marker_precision_recall_proxy
```

The first two are future metric candidates once reference data exists. The
third is only a proxy and cannot close an OCR-quality claim by itself.

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
