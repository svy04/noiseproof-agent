# Source-policy No-native-text OCR Execution Plan Spec

status: draft_for_tdd

date: 2026-06-30

target_gate: source_policy_no_native_text_ocr_execution_plan_v0

current_repo_state:

- `source_policy_no_native_text_ocr_dependency_resolution_v0` is accepted on main.
- The dependency resolution records Tesseract command availability and English language data availability after owner-runtime PATH refresh.
- The preserved NARA route remains the no-native-text candidate:
  `nara_911_mfr_00282_no_native_text_candidate`.
- OCR has not been executed in the source-policy route.
- OCR quality has not been evaluated.
- Robust PDF extraction remains unproven.

sources_to_absorb:

- PyMuPDF OCR docs: OCR is an explicit Tesseract-backed path through `Page.get_textpage_ocr()`, not an implicit fallback from normal text extraction.
- Tesseract command-line usage: command and language availability are prerequisites, not OCR execution evidence.
- OCR-D evaluation: OCR quality requires a separate evaluation criterion such as CER/WER-like checks or expected-span evaluation.
- Existing NoiseProof dependency resolution packet: dependency availability can feed an execution plan but cannot replace execution evidence.

non_goals:

- Do not run OCR in this gate.
- Do not evaluate OCR quality.
- Do not download PDFs.
- Do not parse PDFs.
- Do not commit local executable paths, tessdata paths, source PDFs, download caches, raw text, raw OCR text, page images, screenshots, or table rows.
- Do not implement retrieval, Evidence Ledger, Critic / Noise Gate, final reports, dashboard, or DB persistence.
- Do not claim OCR execution, OCR quality, robust PDF extraction, arbitrary-market PDF parsing reliability, hosted deployment, external reviewer feedback, or product completeness.

implementation_scope:

- Add a deterministic OCR execution-plan packet for the preserved source-policy NARA no-native-text route.
- Add a loader, validator, summary builder, and markdown report builder for the execution plan.
- Add a CLI command to regenerate/check the report from the committed plan.
- Update public proof surfaces and CI staleness checks.

data_or_api_contract:

Input:

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-execution-plan.json
```

Output:

```text
docs/evaluation/source-policy-no-native-text-ocr-execution-plan-report.md
```

Required committed summary fields:

```text
phase_marker -> source_policy_no_native_text_ocr_execution_plan_v0
previous_gate -> source_policy_no_native_text_ocr_dependency_resolution_v0
plan_status -> planned_execution_contract
execution_adapter -> pymupdf_page_get_textpage_ocr
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
target_page_count -> 4
target_empty_page_count -> 4
dependency_available -> true
path_refresh_required -> true
opt_in_required -> true
planned_ocr_language -> eng
planned_dpi -> 300
planned_full_page_ocr -> true
ocr_execution_performed -> false
ocr_quality_eval_performed -> false
raw_ocr_text_committed -> false
page_images_committed -> false
screenshots_committed -> false
can_claim_ocr_execution_plan -> true
can_claim_ocr_execution -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
next_gate -> source_policy_no_native_text_ocr_execution_smoke_v0
```

tests:

- `apps/api/tests/test_source_policy_no_native_text_ocr_execution_plan.py`
- RED must fail because the new execution-plan module does not exist.
- GREEN must pass plan summary/report, command check mode, path/raw-content safety, proof-surface, and rejection tests.

docs_to_update:

- `README.md`
- `docs/MASTER-SPEC.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/review/external-reader-proof-path.md`
- `docs/review/proof-gap-action-surface.md`
- `docs/research/source-assimilation-registry.md`
- `apps/api/app/services/proof_gap_registry.py`
- `.github/workflows/ci.yml`

stop_conditions:

- Stop if the plan requires OCR execution in this gate.
- Stop if the plan would commit local paths, source PDFs, raw OCR text, page images, or screenshots.
- Stop if the plan cannot preserve dependency availability, opt-in requirement, and raw-content boundary.
- Stop if tests require retrieval, Evidence Ledger, Critic / Noise Gate, final reports, dashboard, or DB persistence.

claim_boundaries:

Implemented:

- A bounded OCR execution plan exists for the preserved source-policy NARA no-native-text route.

Not implemented:

- OCR execution, OCR quality evaluation, robust PDF extraction, retrieval, Evidence Ledger, Critic / Noise Gate, final report generation, dashboard, hosted deployment, external reviewer feedback.

Can claim:

- The source-policy no-native-text OCR execution plan is inspectable and bounded.

Cannot claim:

- OCR ran, OCR output is correct, robust PDF extraction works, arbitrary-market PDF parsing is reliable, OCR quality is benchmarked, or the product is complete.

next_gate_if_passed:

```text
source_policy_no_native_text_ocr_execution_smoke_v0
```
