# Source-policy No-native-text OCR Owner Transcript Collection Plan Spec

status: draft_for_tdd

date: 2026-07-01

target_gate: source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0

previous_gate: source_policy_no_native_text_ocr_transcript_reference_pack_v0

recommended_next_gate_after_this_spec:

```text
source_policy_no_native_text_ocr_source_rights_review_request_packet_v0
```

## Current Repo State

- `source_policy_no_native_text_ocr_transcript_reference_pack_v0` is accepted on main.
- The accepted pack records a sanitized transcript-reference pack boundary only.
- `source_rights_owner_approval_recorded` is false.
- No reference transcript is available or committed.
- No source PDF, raw OCR text, raw reference text, transcript hash, page images, screenshots, local paths, or tessdata paths are committed.

## Sources To Absorb

- OCR-D evaluation: OCR quality scoring needs reference/ground-truth text and OCR output comparison.
- JiWER: WER/CER-style metrics require reference and hypothesis strings after normalization/alignment decisions.
- NARA policy: public access to a record does not by itself prove the item-specific reuse boundary for derived transcript material.
- Existing transcript reference pack: the pack can justify planning an owner-runtime transcript collection workflow, but cannot become transcript availability or OCR quality evidence.

## Non-goals

- Do not collect, write, or commit a transcript.
- Do not request or record source-rights owner approval as completed.
- Do not commit a transcript hash.
- Do not run OCR.
- Do not evaluate OCR recognition quality.
- Do not compute CER, WER, precision, recall, accuracy, or benchmark scores.
- Do not add JiWER as a dependency.
- Do not commit source PDFs, download caches, local paths, tessdata paths, raw native text, raw OCR text, page-level transcripts, page images, screenshots, or table rows.
- Do not implement retrieval, Evidence Ledger, Critic / Noise Gate, final reports, dashboard, DB persistence, or hosted deployment.
- Do not call LLMs.
- Do not claim transcript collection, reference transcript availability, robust PDF extraction, arbitrary-market OCR reliability, OCR benchmark quality, external reviewer feedback, or product completeness.

## Implementation Scope

- Add a deterministic owner transcript collection plan module.
- Load the accepted transcript-reference-pack artifact.
- Produce a sanitized owner transcript collection plan artifact that records:
  - source policy route
  - target fixture identity and hash
  - previous transcript reference pack marker
  - owner-runtime-only transcript collection steps
  - source-rights review requirement before committing transcript text or hashes
  - repository commit policy
  - explicit non-claims and next gate
- Add a deterministic report builder and CLI check mode.
- Update reviewer/public proof surfaces and CI staleness checks.

## Data Or API Contract

Committed owner transcript collection plan artifact:

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-owner-transcript-collection-plan.json
```

Committed report:

```text
docs/evaluation/source-policy-no-native-text-ocr-owner-transcript-collection-plan-report.md
```

Required committed summary fields:

```text
phase_marker -> source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0
previous_gate -> source_policy_no_native_text_ocr_transcript_reference_pack_v0
plan_status -> owner_transcript_collection_planned
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
transcript_reference_pack_phase_marker -> source_policy_no_native_text_ocr_transcript_reference_pack_v0
collection_scope -> owner_runtime_manual_transcript_collection_plan_only
target_page_count -> 4
planned_reference_page_count -> 4
planned_collection_step_count -> 7
source_policy_review_status -> metadata_review_only
source_rights_review_required -> true
source_rights_owner_approval_recorded -> false
source_rights_request_packet_required -> true
owner_runtime_storage_required -> true
repository_commit_policy -> metadata_only_no_transcript_text_or_hash
transcript_collection_performed -> false
reference_text_available -> false
full_reference_transcript_available -> false
reference_text_commit_allowed -> false
transcript_hash_committed -> false
reference_text_hash_committed -> false
quality_eval_performed -> false
cer_computed -> false
wer_computed -> false
metric_candidates_status -> blocked_until_reference_text_and_rights_review_exist
raw_reference_text_committed -> false
raw_ocr_text_committed -> false
can_claim_owner_transcript_collection_plan -> true
can_claim_transcript_collection -> false
can_claim_reference_transcript_available -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_no_native_text_ocr_source_rights_review_request_packet_v0
```

Planned collection steps:

```text
confirm_item_specific_rights_status
prepare_owner_runtime_workspace
create_page_level_manual_reference_transcript_outside_repo
apply_normalization_rules
record_alignment_policy
review_metric_eligibility
decide_commit_or_hash_policy_after_rights_review
```

## Tests

- `apps/api/tests/test_source_policy_no_native_text_ocr_owner_transcript_collection_plan.py`
- RED must fail because the new owner-transcript-collection-plan module does not exist.
- GREEN must pass committed plan/report checks, command check mode, rejection tests, artifact safety checks, proof-surface links, proof-gap registry updates, and CI staleness checks.

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

- Stop if the implementation is asked to collect or commit transcript text.
- Stop if the implementation records source-rights owner approval as completed without evidence.
- Stop if the implementation commits transcript hashes before rights review.
- Stop if the implementation tries to compute CER/WER without reference text.
- Stop if any artifact would require committing raw OCR text, raw reference text, source PDFs, page images, screenshots, local paths, or tessdata paths.
- Stop if the implementation drifts into retrieval, Evidence Ledger, Critic / Noise Gate, final report generation, dashboard, DB persistence, or hosted deployment.

## Claim Boundaries

Implemented:

- A deterministic owner-runtime transcript collection plan for the preserved NARA no-native-text OCR route.

Not implemented:

- Transcript collection, source-rights approval completion, transcript hash commitment, reference transcript availability, OCR quality scoring, CER/WER computation, robust PDF extraction, arbitrary-market OCR reliability, retrieval, Evidence Ledger, Critic / Noise Gate, final report generation, dashboard, hosted deployment, external reviewer feedback.

Can claim:

- The source-policy no-native-text OCR route now has an owner-runtime transcript collection plan that keeps transcript text and hashes out of the repo until item-specific rights review exists.

Cannot claim:

- A reference transcript exists, transcript collection has happened, source-rights owner approval is recorded, OCR output is correct, OCR quality is benchmarked, CER/WER can be computed, robust PDF extraction works, arbitrary-market PDF parsing is reliable, or the product is complete.

## Next Gate If Passed

```text
source_policy_no_native_text_ocr_source_rights_review_request_packet_v0
```
