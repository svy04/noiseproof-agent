# Source-policy No-native-text OCR Dependency Check Spec

status: draft_for_tdd

date: 2026-06-30

target_gate: source_policy_no_native_text_ocr_dependency_check_v0

current_repo_state:

- `source_policy_no_native_text_ocr_readiness_review_v0` is accepted on main.
- The readiness review identifies OCR as a Tesseract-backed dependency surface.
- The current local shell check returned `TESSERACT_COMMAND=missing`.
- The dependency check must not print or commit local paths.

sources_to_absorb:

- Tesseract tessdoc command-line usage: `--version` and `--list-langs` are the minimum command-level checks.
- Tesseract tessdoc installation: engine and traineddata/language files are separate installation concerns.
- PyMuPDF OCR docs: PyMuPDF OCR is Tesseract-backed and separate from normal text extraction.
- OCR-D evaluation: dependency availability is not OCR quality.

non_goals:

- Do not install Tesseract in this gate.
- Do not run OCR.
- Do not download PDFs.
- Do not parse PDFs.
- Do not commit local executable paths, tessdata paths, source PDFs, download caches, raw text, raw OCR text, page images, screenshots, or table rows.
- Do not implement retrieval, Evidence Ledger, Critic / Noise Gate, final reports, dashboard, or DB persistence.
- Do not claim OCR execution, OCR quality, robust PDF extraction, arbitrary-market PDF parsing reliability, hosted deployment, external reviewer feedback, or product completeness.

implementation_scope:

- Add a deterministic dependency-check observation packet for the current missing local Tesseract command state.
- Add a probe helper that can safely check `tesseract --version` and `tesseract --list-langs` without returning paths.
- Add a loader, validator, summary builder, and markdown report builder.
- Add a CLI command to regenerate/check the report from the committed observation.
- Update public proof surfaces and CI staleness checks.

data_or_api_contract:

Input:

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-dependency-check.json
```

Output:

```text
docs/evaluation/source-policy-no-native-text-ocr-dependency-check-report.md
```

Required committed summary fields:

```text
phase_marker -> source_policy_no_native_text_ocr_dependency_check_v0
previous_gate -> source_policy_no_native_text_ocr_readiness_review_v0
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
next_gate -> source_policy_no_native_text_ocr_dependency_resolution_v0
```

tests:

- `apps/api/tests/test_source_policy_no_native_text_ocr_dependency_check.py`
- RED must fail because the new module does not exist.
- GREEN must pass missing, present, report, command, and proof-surface tests.

docs_to_update:

- `README.md`
- `docs/MASTER-SPEC.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/review/external-reader-proof-path.md`
- `docs/review/proof-gap-action-surface.md`
- `docs/research/source-assimilation-registry.md`
- `.github/workflows/ci.yml`

stop_conditions:

- Stop if the gate requires installing Tesseract.
- Stop if the gate requires OCR execution.
- Stop if the gate needs to print local paths.
- Stop if tests require source PDFs, raw OCR text, local executable paths, tessdata paths, page images, or screenshots.

claim_boundaries:

Implemented:

- Safe OCR dependency check packet and report over the current missing Tesseract command state.

Not implemented:

- Dependency resolution/install, OCR execution, OCR quality evaluation, robust PDF extraction, retrieval, Evidence Ledger, Critic / Noise Gate, final report generation, dashboard, hosted deployment, external reviewer feedback.

Can claim:

- Source-policy no-native-text OCR dependency check exists and currently records missing local Tesseract command without exposing paths.

Cannot claim:

- OCR dependency is available, OCR ran, OCR output is correct, robust PDF extraction works, arbitrary-market PDF parsing is reliable, OCR quality is benchmarked, or the product is complete.

next_gate_if_passed:

```text
source_policy_no_native_text_ocr_dependency_resolution_v0
```
