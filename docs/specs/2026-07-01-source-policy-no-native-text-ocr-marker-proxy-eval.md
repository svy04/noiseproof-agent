# Source-policy No-native-text OCR Marker Proxy Eval Spec

status: draft_for_tdd

date: 2026-07-01

target_gate: source_policy_no_native_text_ocr_marker_proxy_eval_v0

previous_gate: source_policy_no_native_text_ocr_quality_reference_pack_v0

recommended_next_gate_after_this_spec:

```text
source_policy_no_native_text_ocr_transcript_reference_plan_v0
```

## Current Repo State

- `source_policy_no_native_text_ocr_quality_reference_pack_v0` is accepted on main.
- The accepted reference pack contains two marker anchors: `commission` and `mfr`.
- The previous OCR execution smoke contains matching expected-marker hit booleans.
- No full reference transcript is committed.
- No OCR quality evaluation, CER, WER, robust PDF extraction, or arbitrary-market
  PDF parsing reliability has been proven.

## Sources To Absorb

- OCR-D evaluation: OCR quality requires ground truth/manual transcription and
  OCR output comparison. Marker presence is not a CER/WER substitute.
- JiWER: WER/CER-style metrics are future candidates only after reference text
  exists.
- Existing source-policy reference pack: marker anchors can support a bounded
  proxy check while CER/WER remain blocked.
- Existing source-policy OCR execution smoke: committed marker-hit booleans can
  be used without committing raw OCR text.

## Non-goals

- Do not run OCR.
- Do not evaluate OCR recognition quality.
- Do not compute CER, WER, precision, recall, accuracy, or benchmark scores.
- Do not add JiWER as a dependency.
- Do not commit source PDFs, download caches, local paths, tessdata paths,
  raw native text, raw OCR text, page-level transcripts, page images,
  screenshots, or table rows.
- Do not implement retrieval, Evidence Ledger, Critic / Noise Gate, final
  reports, dashboard, DB persistence, or hosted deployment.
- Do not call LLMs.
- Do not claim robust PDF extraction, arbitrary-market OCR reliability,
  OCR benchmark quality, external reviewer feedback, or product completeness.

## Implementation Scope

- Add a deterministic marker-proxy evaluation module.
- Load the accepted marker-anchor reference pack and OCR execution-smoke
  observation.
- Produce a sanitized marker-proxy eval artifact that records:
  - reference marker anchors
  - committed observed marker-hit booleans from the smoke packet
  - expected marker count
  - observed hit count
  - missing marker anchors
  - marker proxy hit rate
  - pass/fail against a narrow marker-presence threshold
  - claim boundaries and next gate
- Add a deterministic report builder and CLI check mode.
- Update reviewer/public proof surfaces and CI staleness checks.

## Data Or API Contract

Committed marker proxy eval artifact:

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-marker-proxy-eval.json
```

Committed report:

```text
docs/evaluation/source-policy-no-native-text-ocr-marker-proxy-eval-report.md
```

Required committed summary fields:

```text
phase_marker -> source_policy_no_native_text_ocr_marker_proxy_eval_v0
previous_gate -> source_policy_no_native_text_ocr_quality_reference_pack_v0
eval_status -> marker_proxy_eval_completed
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
reference_unit_type -> marker_anchor
expected_marker_anchor_count -> 2
observed_marker_hit_count -> 2
missing_marker_anchor_count -> 0
marker_proxy_hit_rate -> 1.0
marker_proxy_threshold -> 1.0
marker_proxy_passed -> true
ocr_execution_smoke_phase_marker -> source_policy_no_native_text_ocr_execution_smoke_v0
reference_pack_phase_marker -> source_policy_no_native_text_ocr_quality_reference_pack_v0
quality_eval_performed -> false
cer_computed -> false
wer_computed -> false
raw_reference_text_committed -> false
raw_ocr_text_committed -> false
can_claim_marker_proxy_eval -> true
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_no_native_text_ocr_transcript_reference_plan_v0
```

Required observed marker hits:

```text
commission -> true
mfr -> true
```

## Tests

- `apps/api/tests/test_source_policy_no_native_text_ocr_marker_proxy_eval.py`
- RED must fail because the new marker-proxy eval module does not exist.
- GREEN must pass committed eval/report checks, command check mode, rejection
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

- Stop if a marker proxy result is requested to close OCR quality.
- Stop if the implementation tries to compute CER/WER without a transcript.
- Stop if marker anchors are treated as full ground truth.
- Stop if any artifact would require committing raw OCR text, raw reference
  text, source PDFs, page images, screenshots, local paths, or tessdata paths.
- Stop if the implementation drifts into retrieval, Evidence Ledger, Critic /
  Noise Gate, final report generation, dashboard, DB persistence, or hosted
  deployment.

## Claim Boundaries

Implemented:

- A deterministic marker-presence proxy eval over the preserved NARA
  no-native-text OCR route.

Not implemented:

- OCR quality scoring, CER/WER computation, full ground-truth transcript,
  robust PDF extraction, arbitrary-market OCR reliability, retrieval, Evidence
  Ledger, Critic / Noise Gate, final report generation, dashboard, hosted
  deployment, external reviewer feedback.

Can claim:

- The source-policy no-native-text OCR route has a bounded marker-presence proxy
  evaluation over two accepted anchors.

Cannot claim:

- OCR output is correct, OCR quality is benchmarked, marker proxy proves
  recognition quality, CER/WER can be computed, robust PDF extraction works,
  arbitrary-market PDF parsing is reliable, or the product is complete.

## Next Gate If Passed

```text
source_policy_no_native_text_ocr_transcript_reference_plan_v0
```
