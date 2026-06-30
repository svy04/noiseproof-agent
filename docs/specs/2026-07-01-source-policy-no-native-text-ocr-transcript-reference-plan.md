# Source-policy No-native-text OCR Transcript Reference Plan Spec

status: draft_for_tdd

date: 2026-07-01

target_gate: source_policy_no_native_text_ocr_transcript_reference_plan_v0

previous_gate: source_policy_no_native_text_ocr_marker_proxy_eval_v0

recommended_next_gate_after_this_spec:

```text
source_policy_no_native_text_ocr_transcript_reference_pack_v0
```

## Current Repo State

- `source_policy_no_native_text_ocr_marker_proxy_eval_v0` is accepted on main.
- The accepted marker proxy eval records two observed marker hits and no
  missing marker anchors.
- The marker proxy eval explicitly does not prove OCR quality and does not
  compute CER/WER.
- No full reference transcript is committed.
- No source PDF, raw OCR text, raw reference text, page images, screenshots,
  local paths, or tessdata paths are committed.

## Sources To Absorb

- OCR-D evaluation: OCR quality scoring requires reference/ground-truth text
  and OCR output comparison, not marker-anchor presence alone.
- JiWER: WER/CER-style metrics are future metric candidates only after
  reference text exists and normalization/alignment rules are fixed.
- NARA source policy: the source route must keep publisher policy and reuse
  boundaries visible before creating or committing derived reference material.
- Existing marker-proxy eval: marker hit rate can justify planning a stronger
  reference boundary, but it cannot become OCR quality evidence.

## Non-goals

- Do not collect, write, or commit a transcript.
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

- Add a deterministic transcript-reference-plan module.
- Load the accepted marker proxy eval artifact.
- Produce a sanitized transcript-reference-plan artifact that records:
  - source policy route
  - target fixture identity and hash
  - previous marker proxy eval marker
  - required future reference units
  - metric candidates blocked until transcript reference exists
  - non-claims and next gate
- Add a deterministic report builder and CLI check mode.
- Update reviewer/public proof surfaces and CI staleness checks.

## Data Or API Contract

Committed transcript reference plan artifact:

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-transcript-reference-plan.json
```

Committed report:

```text
docs/evaluation/source-policy-no-native-text-ocr-transcript-reference-plan-report.md
```

Required committed summary fields:

```text
phase_marker -> source_policy_no_native_text_ocr_transcript_reference_plan_v0
previous_gate -> source_policy_no_native_text_ocr_marker_proxy_eval_v0
plan_status -> planned_transcript_reference_contract
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
marker_proxy_eval_phase_marker -> source_policy_no_native_text_ocr_marker_proxy_eval_v0
reference_unit_type -> page_level_transcript_plan
target_page_count -> 4
minimum_reference_pages -> 4
required_reference_unit_count -> 6
owner_approval_required -> true
source_policy_review_required -> true
full_reference_transcript_required -> true
full_reference_transcript_available -> false
transcript_collection_performed -> false
reference_pack_created -> false
quality_eval_performed -> false
cer_computed -> false
wer_computed -> false
metric_candidates_status -> blocked_until_reference_transcript_exists
raw_reference_text_committed -> false
raw_ocr_text_committed -> false
can_claim_transcript_reference_plan -> true
can_claim_transcript_reference_pack -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_no_native_text_ocr_transcript_reference_pack_v0
```

Required future reference units:

```text
source_policy_review
owner_approval
page_level_reference_transcript
normalization_rules
alignment_policy
metric_eligibility_review
```

## Tests

- `apps/api/tests/test_source_policy_no_native_text_ocr_transcript_reference_plan.py`
- RED must fail because the new transcript-reference-plan module does not
  exist.
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

- Stop if a transcript plan is requested to close OCR quality.
- Stop if the implementation tries to compute CER/WER without a transcript.
- Stop if marker anchors are treated as full ground truth.
- Stop if any artifact would require committing raw OCR text, raw reference
  text, source PDFs, page images, screenshots, local paths, or tessdata paths.
- Stop if the implementation drifts into retrieval, Evidence Ledger, Critic /
  Noise Gate, final report generation, dashboard, DB persistence, or hosted
  deployment.

## Claim Boundaries

Implemented:

- A deterministic transcript-reference planning contract for the preserved NARA
  no-native-text OCR route.

Not implemented:

- Transcript collection, reference pack creation, OCR quality scoring, CER/WER
  computation, robust PDF extraction, arbitrary-market OCR reliability,
  retrieval, Evidence Ledger, Critic / Noise Gate, final report generation,
  dashboard, hosted deployment, external reviewer feedback.

Can claim:

- The source-policy no-native-text OCR route has a bounded plan for the minimum
  transcript/reference boundary needed before true OCR quality metrics can be
  considered.

Cannot claim:

- A reference transcript exists, OCR output is correct, OCR quality is
  benchmarked, CER/WER can be computed, robust PDF extraction works,
  arbitrary-market PDF parsing is reliable, or the product is complete.

## Next Gate If Passed

```text
source_policy_no_native_text_ocr_transcript_reference_pack_v0
```
