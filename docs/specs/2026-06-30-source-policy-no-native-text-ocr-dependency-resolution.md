# Source-policy No-native-text OCR Dependency Resolution Spec

status: draft_for_tdd

date: 2026-06-30

target_gate: source_policy_no_native_text_ocr_dependency_resolution_v0

current_repo_state:

- `source_policy_no_native_text_ocr_dependency_check_v0` is accepted on main.
- The dependency check recorded `checked_missing_tesseract_command`.
- Local runtime evidence now shows `winget` can install `tesseract-ocr.tesseract`.
- `winget list --id tesseract-ocr.tesseract --source winget` reports version `5.5.0.20241111`.
- The Codex parent process does not automatically inherit the refreshed user PATH, so the owner-runtime probe must refresh machine/user PATH in-process before checking command availability.
- A refreshed owner-runtime probe reports `tesseract_command_present -> true`, `version_check_performed -> true`, `language_list_check_performed -> true`, `eng_language_available -> true`, and no OCR execution.

sources_to_absorb:

- Tesseract tessdoc command-line usage: `--version` and `--list-langs` are command-level dependency checks only.
- Tesseract tessdoc installation: engine installation and language traineddata availability remain separate setup surfaces.
- PyMuPDF OCR docs: OCR remains a Tesseract-backed path and must not run until a separate OCR execution gate.
- OCR-D evaluation: dependency availability is not recognition quality.

non_goals:

- Do not run OCR.
- Do not download PDFs.
- Do not parse PDFs.
- Do not evaluate OCR quality.
- Do not commit local executable paths, tessdata paths, source PDFs, download caches, raw text, raw OCR text, page images, screenshots, or table rows.
- Do not implement retrieval, Evidence Ledger, Critic / Noise Gate, final reports, dashboard, or DB persistence.
- Do not claim OCR execution, OCR quality, robust PDF extraction, arbitrary-market PDF parsing reliability, hosted deployment, external reviewer feedback, or product completeness.

implementation_scope:

- Add a deterministic dependency-resolution observation packet for the source-policy NARA no-native-text route.
- Fix the dependency probe so Tesseract version can be parsed from stdout or stderr.
- Add a loader, validator, summary builder, and markdown report builder for the resolution packet.
- Add a CLI command to regenerate/check the report from the committed observation.
- Update public proof surfaces and CI staleness checks.

data_or_api_contract:

Input:

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-dependency-resolution.json
```

Output:

```text
docs/evaluation/source-policy-no-native-text-ocr-dependency-resolution-report.md
```

Required committed summary fields:

```text
phase_marker -> source_policy_no_native_text_ocr_dependency_resolution_v0
previous_gate -> source_policy_no_native_text_ocr_dependency_check_v0
dependency_resolution_status -> resolved_dependency_available
installation_method -> winget
installation_package_id -> tesseract-ocr.tesseract
installed_package_version -> 5.5.0.20241111
codex_parent_path_inheritance_mismatch -> true
owner_runtime_path_refresh_performed -> true
tesseract_command_present -> true
version_check_performed -> true
language_list_check_performed -> true
tesseract_version_reported -> true
detected_language_count -> 2
eng_language_available -> true
local_path_discovery_performed -> true
local_paths_committed -> false
tesseract_path_committed -> false
tessdata_path_committed -> false
ocr_execution_performed -> false
ocr_quality_eval_performed -> false
can_claim_ocr_dependency_available -> true
can_claim_ocr_execution -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
next_gate -> source_policy_no_native_text_ocr_execution_plan_v0
```

tests:

- `apps/api/tests/test_source_policy_no_native_text_ocr_dependency_resolution.py`
- RED must fail because the new resolution module does not exist.
- GREEN must pass stderr-version parsing, resolution summary/report, command check mode, path-safety, and proof-surface tests.

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

- Stop if the dependency cannot be made available without committing local paths.
- Stop if resolution requires OCR execution.
- Stop if the report would need source PDFs, raw OCR text, local executable paths, tessdata paths, page images, or screenshots.
- Stop if tests require retrieval, Evidence Ledger, Critic / Noise Gate, final reports, dashboard, or DB persistence.

claim_boundaries:

Implemented:

- Tesseract command and English language data are available to an owner-runtime probe after PATH refresh.

Not implemented:

- OCR execution, OCR quality evaluation, robust PDF extraction, retrieval, Evidence Ledger, Critic / Noise Gate, final report generation, dashboard, hosted deployment, external reviewer feedback.

Can claim:

- Source-policy no-native-text OCR dependency is available in the owner runtime after installation/configuration and sanitized PATH refresh.

Cannot claim:

- OCR ran, OCR output is correct, robust PDF extraction works, arbitrary-market PDF parsing is reliable, OCR quality is benchmarked, or the product is complete.

next_gate_if_passed:

```text
source_policy_no_native_text_ocr_execution_plan_v0
```
