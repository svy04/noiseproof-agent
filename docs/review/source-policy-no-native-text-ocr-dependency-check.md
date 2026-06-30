# Source-policy No-native-text OCR Dependency Check

Phase marker: `source_policy_no_native_text_ocr_dependency_check_v0`.

Previous gate: `source_policy_no_native_text_ocr_readiness_review_v0`.

Next gate: `source_policy_no_native_text_ocr_dependency_resolution_v0`.

## Purpose

This gate records the current OCR dependency state for the preserved NARA
no-native-text route without printing or committing local executable or
tessdata paths.

It does not install Tesseract. It does not run OCR. It does not evaluate OCR
quality.

## Result

```text
dependency_check_status -> checked_missing_tesseract_command
tesseract_command_present -> false
version_check_performed -> false
language_list_check_performed -> false
eng_language_available -> false
local_paths_printed -> false
local_paths_committed -> false
tesseract_path_committed -> false
tessdata_path_committed -> false
ocr_execution_performed -> false
ocr_quality_eval_performed -> false
can_claim_ocr_dependency_check -> true
can_claim_ocr_dependency_available -> false
can_claim_ocr_execution -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
```

## Artifacts

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-dependency-check.json
docs/evaluation/source-policy-no-native-text-ocr-dependency-check-report.md
packages/ingestion/pdf_quality/source_policy_no_native_text_ocr_dependency_check.py
apps/api/app/services/source_policy_no_native_text_ocr_dependency_check_command.py
apps/api/tests/test_source_policy_no_native_text_ocr_dependency_check.py
```

## Boundary

This is a deterministic dependency-check packet over the current OCR dependency
state.

It is not OCR dependency availability evidence.

It is not OCR execution evidence.

It is not OCR quality evidence.

It is not robust PDF extraction evidence.

It is not arbitrary-market PDF parsing evidence.

It is not table extraction benchmark evidence.

It is not layout fidelity evidence.

It is not rendered visual fidelity evidence.

It is not image/chart interpretation evidence.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.
