# Source-policy No-native-text Failure Route

Phase marker: `source_policy_no_native_text_failure_route_v0`.

Previous gate: `source_policy_pdf_quality_gap_review_v0`.

Next gate: `source_policy_no_native_text_ocr_readiness_review_v0`.

## Purpose

This gate preserves the NARA no-native-text observation as an explicit
source-policy failure route before any OCR work starts.

It does not run OCR. It does not improve parsing. It does not add runtime
evidence.

## Result

```text
route_status -> passed_failure_route_preserved
failure_route_count -> 1
selected_failure_route -> multi_publisher_no_extractable_text_failure
fixture_id -> nara_911_mfr_00282_no_native_text_candidate
publisher -> National Archives and Records Administration
failure_type -> no_native_text_observed
root_cause -> image_or_scanned_pdf_without_native_text_layer
page_count -> 4
empty_page_count -> 4
text_char_count -> 0
ocr_calls_performed -> false
can_claim_source_policy_no_native_text_failure_route -> true
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
```

## Artifacts

```text
examples/pdf-extraction-quality/source-policy-no-native-text-failure-route.json
docs/evaluation/source-policy-no-native-text-failure-route-report.md
packages/ingestion/pdf_quality/source_policy_no_native_text_failure_route.py
apps/api/app/services/source_policy_no_native_text_failure_route_command.py
apps/api/tests/test_source_policy_no_native_text_failure_route.py
```

## Boundary

This is a deterministic failure-route packet over existing source-policy PDF
observations.

It is not robust PDF extraction evidence.

It is not arbitrary-market PDF parsing evidence.

It is not OCR quality evidence.

It is not table extraction benchmark evidence.

It is not layout fidelity evidence.

It is not rendered visual fidelity evidence.

It is not image/chart interpretation evidence.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.
