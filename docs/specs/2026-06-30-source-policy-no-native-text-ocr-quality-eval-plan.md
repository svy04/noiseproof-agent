# Source-policy No-native-text OCR Quality Eval Plan Spec

status: draft_for_tdd

date: 2026-06-30

target_gate: source_policy_no_native_text_ocr_quality_eval_plan_v0

previous_gate: source_policy_no_native_text_ocr_execution_smoke_v0

recommended_next_gate_after_this_spec:

```text
source_policy_no_native_text_ocr_quality_reference_pack_v0
```

## Current Repo State

- `source_policy_no_native_text_ocr_execution_smoke_v0` is accepted on main.
- The accepted smoke records one owner-runtime PyMuPDF/Tesseract OCR execution
  over the preserved NARA no-native-text route.
- The accepted smoke records `ocr_text_char_count -> 8019` and two expected
  marker hits.
- The accepted smoke explicitly keeps `ocr_quality_eval_performed -> false`.
- No ground-truth transcript, page-level reference text, or accepted reference
  spans are committed.
- OCR quality, robust PDF extraction, arbitrary-market PDF OCR reliability, and
  arbitrary-market PDF parsing reliability remain unproven.

## Sources To Absorb

- OCR-D evaluation: OCR quality needs OCR output and ground-truth/reference
  text, with edit-distance style metrics such as character error rate and word
  error rate.
- JiWER: CER/WER-style metrics should be treated as a reusable metric surface
  candidate, not introduced before reference data exists.
- Model Cards and Datasheets: public claims must keep intended use, data
  boundary, metric boundary, caveats, and next evidence visible.
- Existing source-policy OCR smoke: marker hits and character counts are smoke
  checks only; they are not quality scores.

## Non-goals

- Do not run OCR.
- Do not evaluate OCR quality.
- Do not compute CER, WER, precision, recall, or accuracy.
- Do not commit source PDFs, download caches, local paths, tessdata paths,
  raw native text, raw OCR text, reference transcripts, page images,
  screenshots, or table rows.
- Do not implement retrieval, Evidence Ledger, Critic / Noise Gate, final
  reports, dashboard, DB persistence, or hosted deployment.
- Do not call LLMs.
- Do not claim robust PDF extraction, arbitrary-market OCR reliability,
  OCR benchmark quality, external reviewer feedback, or product completeness.

## Implementation Scope

- Add a deterministic quality-evaluation plan module.
- Load the accepted execution-smoke observation.
- Produce a sanitized plan artifact that records:
  - why the previous smoke is insufficient for quality claims
  - which reference inputs are required before quality scoring
  - candidate metrics to use only after a reference pack exists
  - stop conditions that block quality scoring
  - public claim boundaries and next gate
- Add a deterministic report builder and CLI check mode.
- Update reviewer/public proof surfaces and CI staleness checks.

## Data Or API Contract

Committed plan artifact:

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-quality-eval-plan.json
```

Committed report:

```text
docs/evaluation/source-policy-no-native-text-ocr-quality-eval-plan-report.md
```

Required committed summary fields:

```text
phase_marker -> source_policy_no_native_text_ocr_quality_eval_plan_v0
previous_gate -> source_policy_no_native_text_ocr_execution_smoke_v0
plan_status -> planned_quality_eval_contract
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
execution_smoke_ocr_text_char_count -> 8019
execution_smoke_expected_markers_found_count -> 2
execution_smoke_quality_eval_performed -> false
ground_truth_available -> false
reference_pack_required -> true
quality_eval_performed -> false
raw_reference_text_committed -> false
raw_ocr_text_committed -> false
marker_hits_are_quality_proxy_only -> true
can_claim_quality_eval_plan -> true
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_no_native_text_ocr_quality_reference_pack_v0
```

Required metric candidates:

```text
character_error_rate
word_error_rate
expected_marker_precision_recall_proxy
```

Required reference inputs before any quality evaluation:

```text
page_level_reference_transcript_or_accepted_spans
reference_source_policy
normalization_rules
page_mapping
source_sha256_binding
ocr_output_acquisition_boundary
raw_text_redaction_boundary
```

## Tests

- `apps/api/tests/test_source_policy_no_native_text_ocr_quality_eval_plan.py`
- RED must fail because the new plan module does not exist.
- GREEN must pass committed plan/report checks, command check mode, rejection
  tests, artifact safety checks, proof-surface links, proof-gap registry
  updates, and CI staleness checks.

## Docs To Update

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

## Stop Conditions

- Stop if a quality score is requested without a reference transcript, accepted
  spans, or equivalent reference pack.
- Stop if any plan or report would require committing raw OCR text, raw
  reference text, source PDFs, page images, screenshots, local paths, or
  tessdata paths.
- Stop if marker hits, text counts, or successful OCR execution are treated as
  recognition-quality evidence.
- Stop if the implementation drifts into retrieval, Evidence Ledger, Critic /
  Noise Gate, final report generation, dashboard, DB persistence, or hosted
  deployment.

## Claim Boundaries

Implemented:

- A source-policy no-native-text OCR quality-evaluation plan.

Not implemented:

- Ground-truth/reference pack, OCR quality scoring, CER/WER computation, robust
  PDF extraction, arbitrary-market OCR reliability, retrieval, Evidence Ledger,
  Critic / Noise Gate, final report generation, dashboard, hosted deployment,
  external reviewer feedback.

Can claim:

- The source-policy no-native-text OCR route now has a bounded plan for what
  must exist before OCR quality can be evaluated.

Cannot claim:

- OCR output is correct, OCR quality is benchmarked, marker hits prove
  recognition quality, robust PDF extraction works, arbitrary-market PDF parsing
  is reliable, or the product is complete.

## Next Gate If Passed

```text
source_policy_no_native_text_ocr_quality_reference_pack_v0
```
