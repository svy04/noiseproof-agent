# Source-policy No-native-text OCR Transcript Reference Pack Spec

status: draft_for_tdd

date: 2026-07-01

target_gate: source_policy_no_native_text_ocr_transcript_reference_pack_v0

previous_gate: source_policy_no_native_text_ocr_transcript_reference_plan_v0

recommended_next_gate_after_this_spec:

```text
source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0
```

## Current Repo State

- `source_policy_no_native_text_ocr_transcript_reference_plan_v0` is accepted on main.
- The accepted plan defines six required future reference units before true OCR quality metrics can be considered.
- No reference transcript is committed.
- No source PDF, raw OCR text, raw reference text, page images, screenshots, local paths, or tessdata paths are committed.

## Sources To Absorb

- OCR-D evaluation: OCR quality scoring requires reference/ground-truth text and OCR output comparison, not a marker proxy or metadata pack alone.
- JiWER: CER/WER remain future metric candidates only after reference text, normalization, and alignment rules exist.
- NARA source policy: public access and federal-record routes do not automatically permit committing derived transcript material without preserving source-policy and reuse boundaries.
- Existing transcript reference plan: the pack can record the minimum source-policy-reviewed boundary, but cannot become reference text or OCR quality evidence.

## Non-goals

- Do not collect, write, or commit a transcript.
- Do not run OCR.
- Do not evaluate OCR recognition quality.
- Do not compute CER, WER, precision, recall, accuracy, or benchmark scores.
- Do not add JiWER as a dependency.
- Do not commit source PDFs, download caches, local paths, tessdata paths, raw native text, raw OCR text, page-level transcripts, page images, screenshots, or table rows.
- Do not implement retrieval, Evidence Ledger, Critic / Noise Gate, final reports, dashboard, DB persistence, or hosted deployment.
- Do not call LLMs.
- Do not claim reference transcript availability, robust PDF extraction, arbitrary-market OCR reliability, OCR benchmark quality, external reviewer feedback, or product completeness.

## Implementation Scope

- Add a deterministic transcript-reference-pack module.
- Load the accepted transcript reference plan artifact.
- Produce a sanitized transcript-reference-pack boundary artifact that records:
  - source policy route
  - target fixture identity and hash
  - previous transcript reference plan marker
  - planned page-level reference units
  - normalization and alignment contract
  - metric candidates blocked until transcript text exists
  - explicit non-claims and next gate
- Add a deterministic report builder and CLI check mode.
- Update reviewer/public proof surfaces and CI staleness checks.

## Data Or API Contract

Committed transcript reference pack artifact:

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-transcript-reference-pack.json
```

Committed report:

```text
docs/evaluation/source-policy-no-native-text-ocr-transcript-reference-pack-report.md
```

Required committed summary fields:

```text
phase_marker -> source_policy_no_native_text_ocr_transcript_reference_pack_v0
previous_gate -> source_policy_no_native_text_ocr_transcript_reference_plan_v0
reference_pack_status -> sanitized_transcript_reference_pack_boundary
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
transcript_reference_plan_phase_marker -> source_policy_no_native_text_ocr_transcript_reference_plan_v0
reference_unit_type -> page_level_transcript_reference_pack_boundary
target_page_count -> 4
planned_reference_page_count -> 4
required_reference_unit_count -> 6
reference_pack_created -> true
reference_pack_claim_scope -> sanitized_boundary_only
source_policy_review_status -> reviewed_for_metadata_only
project_owner_approval_recorded -> true
source_rights_owner_approval_recorded -> false
source_rights_owner_approval_required_before_transcript -> true
reference_text_available -> false
full_reference_transcript_available -> false
transcript_collection_performed -> false
transcript_hash_committed -> false
reference_text_hash_committed -> false
quality_eval_performed -> false
cer_computed -> false
wer_computed -> false
metric_candidates_status -> blocked_until_reference_text_exists
raw_reference_text_committed -> false
raw_ocr_text_committed -> false
can_claim_transcript_reference_pack -> true
can_claim_reference_transcript_available -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0
```

Required reference pack units:

```text
source_policy_review
owner_approval
page_level_reference_transcript
normalization_rules
alignment_policy
metric_eligibility_review
```

## Tests

- `apps/api/tests/test_source_policy_no_native_text_ocr_transcript_reference_pack.py`
- RED must fail because the new transcript-reference-pack module does not exist.
- GREEN must pass committed pack/report checks, command check mode, rejection tests, artifact safety checks, proof-surface links, proof-gap registry updates, and CI staleness checks.

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

- Stop if the pack is requested to include transcript text.
- Stop if the implementation tries to compute CER/WER without a reference transcript.
- Stop if a sanitized pack boundary is treated as OCR quality.
- Stop if any artifact would require committing raw OCR text, raw reference text, source PDFs, page images, screenshots, local paths, or tessdata paths.
- Stop if the implementation drifts into retrieval, Evidence Ledger, Critic / Noise Gate, final report generation, dashboard, DB persistence, or hosted deployment.

## Claim Boundaries

Implemented:

- A deterministic sanitized transcript-reference pack boundary for the preserved NARA no-native-text OCR route.

Not implemented:

- Transcript collection, reference transcript availability, OCR quality scoring, CER/WER computation, robust PDF extraction, arbitrary-market OCR reliability, retrieval, Evidence Ledger, Critic / Noise Gate, final report generation, dashboard, hosted deployment, external reviewer feedback.

Can claim:

- The source-policy no-native-text OCR route now has a sanitized transcript-reference pack boundary that records the minimum future reference units and keeps raw transcript material out of the repo.

Cannot claim:

- A reference transcript exists, OCR output is correct, OCR quality is benchmarked, CER/WER can be computed, robust PDF extraction works, arbitrary-market PDF parsing is reliable, or the product is complete.

## Next Gate If Passed

```text
source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0
```
