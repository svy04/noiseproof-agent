# Source-policy No-native-text OCR Execution Smoke Spec

status: draft_for_tdd

date: 2026-06-30

target_gate: source_policy_no_native_text_ocr_execution_smoke_v0

current_repo_state:

- `source_policy_no_native_text_ocr_execution_plan_v0` is accepted on main.
- The previous plan selected the preserved NARA no-native-text candidate:
  `nara_911_mfr_00282_no_native_text_candidate`.
- The owner runtime has PyMuPDF available through the API environment.
- Tesseract is installed locally but may require a PATH refresh in a new
  PowerShell process.
- The owner-runtime source PDF cache is not committed and may be absent in a
  fresh worktree.
- OCR execution for the source-policy no-native-text route has not yet been
  recorded as a bounded smoke artifact.
- OCR quality evaluation remains unproven.
- Robust PDF extraction remains unproven.

sources_to_absorb:

- PyMuPDF OCR docs: OCR is explicit through `Page.get_textpage_ocr()` and
  depends on Tesseract.
- Tesseract command-line usage: command and language availability are runtime
  prerequisites, not recognition-quality evidence.
- Existing synthetic OCR smoke harness: owner-runtime opt-in, missing-input
  safety, and no-path/no-raw-text reporting should be reused.
- Existing real-world OCR evidence gate: commit only sanitized counts,
  expected-marker hit booleans, source hash, and non-claims.
- OCR-D evaluation: recognition quality requires a later evaluation criterion
  and must not be collapsed into this smoke.

non_goals:

- Do not evaluate OCR quality.
- Do not commit source PDFs, download caches, local paths, tessdata paths,
  raw native text, raw OCR text, page images, screenshots, or table rows.
- Do not implement retrieval, Evidence Ledger, Critic / Noise Gate, final
  reports, dashboard, or DB persistence.
- Do not call LLMs.
- Do not claim robust PDF extraction, arbitrary-market OCR reliability,
  OCR benchmark quality, hosted deployment, external reviewer feedback, or
  product completeness.

implementation_scope:

- Add a source-policy no-native-text OCR smoke module.
- Add owner-runtime input discovery that keeps local paths out of returned
  payloads.
- Add a runner that requires explicit opt-in and rejects repository output
  paths.
- Allow the runner to download the selected source PDF transiently, verify the
  expected SHA-256, run PyMuPDF OCR over the planned pages, and write only a
  sanitized observation packet outside the repository.
- Commit a sanitized observation packet generated from the owner runtime.
- Add a deterministic report builder and CLI check mode for the committed
  sanitized observation.
- Update public proof surfaces and CI staleness checks.

data_or_api_contract:

Committed sanitized observation:

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-execution-smoke.json
```

Committed report:

```text
docs/evaluation/source-policy-no-native-text-ocr-execution-smoke-report.md
```

Required committed summary fields:

```text
phase_marker -> source_policy_no_native_text_ocr_execution_smoke_v0
previous_gate -> source_policy_no_native_text_ocr_execution_plan_v0
run_source -> owner_runtime_pymupdf_ocr_source_policy_smoke
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
publisher -> National Archives and Records Administration
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
page_count -> 4
ocr_pages_attempted -> 4
native_text_char_count -> 0
ocr_text_char_count -> positive integer
expected_markers_checked -> commission; mfr
expected_markers_found_count -> positive integer
ocr_execution_performed -> true
ocr_calls_attempted -> true
ocr_quality_eval_performed -> false
raw_ocr_text_committed -> false
page_images_committed -> false
screenshots_committed -> false
can_claim_source_policy_no_native_text_ocr_execution_smoke -> true
can_claim_ocr_execution -> true
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
next_gate -> source_policy_no_native_text_ocr_quality_eval_plan_v0
```

tests:

- `apps/api/tests/test_source_policy_no_native_text_ocr_execution_smoke.py`
- RED must fail because the new smoke module does not exist.
- GREEN must pass committed sanitized observation/report checks, command check
  mode, owner-runtime missing-input safety, fake-adapter runner behavior,
  path/raw-content safety, proof-surface links, and rejection tests.

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

- Stop if Tesseract or English language data cannot be resolved after a local
  PATH refresh.
- Stop if the selected source PDF cannot be downloaded and hash-verified in
  owner runtime.
- Stop if OCR would require committing raw OCR text, source PDFs, page images,
  screenshots, local paths, or tessdata paths.
- Stop if OCR smoke output is requested to be treated as OCR quality evidence.
- Stop if tests require retrieval, Evidence Ledger, Critic / Noise Gate, final
  reports, dashboard, or DB persistence.

claim_boundaries:

Implemented:

- A bounded source-policy no-native-text OCR smoke over the selected NARA route.

Not implemented:

- OCR quality evaluation, robust PDF extraction, arbitrary-market OCR
  reliability, retrieval, Evidence Ledger, Critic / Noise Gate, final report
  generation, dashboard, hosted deployment, external reviewer feedback.

Can claim:

- The source-policy no-native-text route has one sanitized owner-runtime OCR
  execution smoke.

Cannot claim:

- OCR output is correct, OCR quality is benchmarked, robust PDF extraction
  works, arbitrary-market PDF parsing is reliable, or the product is complete.

next_gate_if_passed:

```text
source_policy_no_native_text_ocr_quality_eval_plan_v0
```
