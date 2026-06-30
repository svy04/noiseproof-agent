# Source-policy No-native-text OCR Readiness Review Spec

status: draft_for_tdd

date: 2026-06-30

target_gate: source_policy_no_native_text_ocr_readiness_review_v0

current_repo_state:

- `source_policy_no_native_text_failure_route_v0` is accepted on main.
- The preserved NARA route records `page_count -> 4`, `empty_page_count -> 4`, `text_char_count -> 0`, and `ocr_calls_performed -> false`.
- `docs/MASTER-SPEC.md`, `docs/GOAL.md`, `README.md`, `docs/runbook.md`, and `apps/api/app/services/proof_gap_registry.py` point to `source_policy_no_native_text_ocr_readiness_review_v0`.

sources_to_absorb:

- PyMuPDF OCR recipes: OCR is an explicit Tesseract-backed path, not normal text extraction.
- PyMuPDF `Page.get_textpage_ocr()`: OCR textpage creation is a distinct API surface.
- OCR-D evaluation: OCR quality needs explicit evaluation, not a character-count proxy.
- Model Cards and Datasheets patterns: document intended use, caveats, factors, and dataset/source boundaries before stronger claims.

non_goals:

- Do not run OCR.
- Do not install or check Tesseract/tessdata in this gate.
- Do not download PDFs.
- Do not parse PDFs.
- Do not commit external PDF binaries, download caches, raw text, raw OCR text, page images, screenshots, local paths, or tessdata paths.
- Do not implement retrieval, Evidence Ledger, Critic / Noise Gate, final reports, dashboard, or DB persistence.
- Do not claim OCR quality, OCR dependency availability, OCR execution, robust PDF extraction, arbitrary-market PDF parsing reliability, rendered visual fidelity, image/chart interpretation, external reviewer feedback, hosted deployment, or product completeness.

implementation_scope:

- Add a deterministic OCR readiness review packet for the preserved no-native-text route.
- Add a loader, validator, summary builder, and markdown report builder.
- Add a CLI command to regenerate/check the report.
- Add tests that prove the gate stays readiness-only and does not perform runtime work.
- Update public proof surfaces and CI staleness checks.

data_or_api_contract:

Input:

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-readiness-review.json
```

Output:

```text
docs/evaluation/source-policy-no-native-text-ocr-readiness-review-report.md
```

Required summary fields:

```text
phase_marker -> source_policy_no_native_text_ocr_readiness_review_v0
previous_gate -> source_policy_no_native_text_failure_route_v0
readiness_status -> passed_with_conditions
fixture_id -> nara_911_mfr_00282_no_native_text_candidate
failure_type -> no_native_text_observed
ocr_dependency_identified -> true
ocr_dependency_runtime_check_performed -> false
ocr_execution_performed -> false
ocr_quality_eval_performed -> false
can_claim_ocr_readiness_review -> true
can_claim_ocr_dependency_available -> false
can_claim_ocr_execution -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
next_gate -> source_policy_no_native_text_ocr_dependency_check_v0
```

tests:

- `apps/api/tests/test_source_policy_no_native_text_ocr_readiness_review.py`
- RED must fail because the new module does not exist.
- GREEN must pass loader/summary/report/command/surface tests.

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

- Stop if the gate needs actual OCR execution.
- Stop if the gate needs local Tesseract/tessdata paths.
- Stop if the source-policy route is missing or has changed in a way that invalidates the preserved NARA fixture.
- Stop if tests require raw OCR text, source PDFs, page images, or screenshots.

claim_boundaries:

Implemented:

- OCR readiness review packet and report over the preserved no-native-text route.

Not implemented:

- OCR dependency runtime check, OCR execution, OCR quality evaluation, robust PDF extraction, retrieval, Evidence Ledger, Critic / Noise Gate, final report generation, dashboard, hosted deployment, external reviewer feedback.

Can claim:

- Source-policy no-native-text OCR readiness review exists as a deterministic packet.

Cannot claim:

- OCR dependency is available, OCR ran, OCR output is correct, robust PDF extraction works, arbitrary-market PDF parsing is reliable, OCR quality is benchmarked, or the product is complete.

next_gate_if_passed:

```text
source_policy_no_native_text_ocr_dependency_check_v0
```
