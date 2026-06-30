# Source-policy No-native-text OCR Owner Rights Decision Record Spec

status: draft_for_tdd

date: 2026-07-01

target_gate: source_policy_no_native_text_ocr_owner_rights_decision_record_v0

previous_gate: source_policy_no_native_text_ocr_source_rights_review_request_packet_v0

recommended_next_gate_after_this_spec:

```text
source_policy_no_native_text_ocr_rights_request_delivery_record_v0
```

## Current Repo State

- `source_policy_no_native_text_ocr_source_rights_review_request_packet_v0` is accepted on main.
- The request packet is prepared, but `request_sent` remains false.
- No rights response, source-rights owner approval, source-rights owner decision, transcript text, transcript hash, source PDF, raw OCR text, raw reference text, page images, screenshots, local paths, or tessdata paths are committed.
- NARA's current public policy page says Federal-agency materials are generally public domain, but not all website/holdings materials are public domain; some holdings may have restrictions, NARA cannot confirm copyright status for every item, and use is at the user's risk.
- OCR-D and JiWER keep CER/WER-style scoring dependent on ground-truth/reference and OCR/hypothesis text. Those inputs are still unavailable in the repository.

## Sources To Absorb

- OCR-D evaluation: OCR quality scoring needs ground-truth/reference text and OCR output comparison.
- JiWER: WER/CER-style metrics require reference and hypothesis strings after normalization/alignment decisions.
- NARA Privacy and Use Policies: access/reproduction policy is not item-specific rights clearance for all holdings; restrictions and copyright uncertainty can remain.
- Existing request packet: the repository can record an owner decision to keep transcript collection blocked, but cannot record request delivery, source-rights response, or rights clearance without evidence.

## Non-goals

- Do not send a rights request.
- Do not record a rights response.
- Do not record source-rights owner approval as completed.
- Do not collect, write, or commit a transcript.
- Do not permit transcript text or transcript hashes to enter the repository.
- Do not compute CER, WER, precision, recall, accuracy, or benchmark scores.
- Do not run OCR.
- Do not add JiWER as a dependency.
- Do not commit source PDFs, download caches, local paths, tessdata paths, raw native text, raw OCR text, page-level transcripts, page images, screenshots, or table rows.
- Do not implement retrieval, Evidence Ledger, Critic / Noise Gate, final reports, dashboard, DB persistence, hosted deployment, or LLM calls.
- Do not claim rights clearance, request delivery, source-rights approval, transcript collection, reference transcript availability, robust PDF extraction, arbitrary-market OCR reliability, OCR benchmark quality, external reviewer feedback, or product completeness.

## Implementation Scope

- Add a deterministic owner rights decision record module.
- Load the accepted source-rights review request packet artifact.
- Produce a sanitized owner decision record artifact that records:
  - previous request packet marker
  - target fixture identity and hash
  - owner decision status
  - decision basis
  - blocked repository actions
  - allowed repository actions
  - source-rights request delivery still needed
  - explicit non-claims and next gate
- Add a deterministic report builder and CLI check mode.
- Update reviewer/public proof surfaces and CI staleness checks.

## Data Or API Contract

Committed owner rights decision record:

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-owner-rights-decision-record.json
```

Committed report:

```text
docs/evaluation/source-policy-no-native-text-ocr-owner-rights-decision-record-report.md
```

Required committed summary fields:

```text
phase_marker -> source_policy_no_native_text_ocr_owner_rights_decision_record_v0
previous_gate -> source_policy_no_native_text_ocr_source_rights_review_request_packet_v0
decision_status -> owner_decision_recorded_blocked_pending_source_rights_response
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
source_rights_review_request_packet_phase_marker -> source_policy_no_native_text_ocr_source_rights_review_request_packet_v0
decision_scope -> repository_transcript_and_hash_commit_boundary
owner_decision -> do_not_collect_or_commit_transcript_until_source_rights_response_exists
request_packet_prepared -> true
request_sent -> false
rights_response_received -> false
source_rights_owner_approval_recorded -> false
source_rights_owner_decision_recorded -> false
owner_rights_decision_recorded -> true
source_rights_request_delivery_needed -> true
source_rights_request_delivery_performed -> false
transcript_collection_allowed -> false
transcript_collection_performed -> false
reference_text_available -> false
reference_text_commit_allowed -> false
transcript_hash_commit_allowed -> false
transcript_hash_committed -> false
quality_eval_performed -> false
cer_computed -> false
wer_computed -> false
metric_candidates_status -> blocked_until_request_sent_rights_response_and_reference_text_exist
raw_reference_text_committed -> false
raw_ocr_text_committed -> false
can_claim_owner_rights_decision_record -> true
can_claim_rights_clearance -> false
can_claim_request_sent -> false
can_claim_source_rights_owner_approval -> false
can_claim_transcript_collection -> false
can_claim_reference_transcript_available -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_no_native_text_ocr_rights_request_delivery_record_v0
```

Required decision basis:

```text
request_packet_prepared
request_not_sent
no_rights_response_received
no_source_rights_owner_approval_recorded
nara_policy_does_not_guarantee_item_specific_rights_status
ocr_quality_metrics_require_reference_text
```

Required blocked actions:

```text
collect_reference_transcript
commit_reference_transcript_text
commit_reference_transcript_hash
compute_cer
compute_wer
claim_ocr_quality
claim_robust_pdf_extraction
```

Required allowed actions:

```text
keep_metadata_only_request_packet
prepare_or_send_owner_runtime_rights_request
record_future_rights_response_metadata
keep_public_claims_blocked
```

## Tests

- `apps/api/tests/test_source_policy_no_native_text_ocr_owner_rights_decision_record.py`
- RED must fail because the new owner-rights decision record module does not exist.
- GREEN must pass committed record/report checks, command check mode, rejection tests, artifact safety checks, proof-surface links, proof-gap registry updates, and CI staleness checks.

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

- Stop if the implementation is asked to treat this owner decision as source-rights clearance.
- Stop if the implementation records request delivery or rights response without evidence.
- Stop if the implementation records source-rights owner approval as completed without evidence.
- Stop if the implementation collects or commits transcript text.
- Stop if the implementation permits transcript hashes before a source-rights decision.
- Stop if the implementation tries to compute CER/WER without reference text.
- Stop if any artifact would require committing raw OCR text, raw reference text, source PDFs, page images, screenshots, local paths, or tessdata paths.
- Stop if the implementation drifts into retrieval, Evidence Ledger, Critic / Noise Gate, final report generation, dashboard, DB persistence, hosted deployment, or LLM calls.

## Claim Boundaries

Implemented:

- A deterministic owner decision record that blocks transcript collection and transcript/hash commits until source-rights response evidence exists.

Not implemented:

- Request delivery, source-rights response, source-rights approval completion, source-rights clearance, transcript collection, transcript hash commitment, reference transcript availability, OCR quality scoring, CER/WER computation, robust PDF extraction, arbitrary-market OCR reliability, retrieval, Evidence Ledger, Critic / Noise Gate, final report generation, dashboard, hosted deployment, external reviewer feedback.

Can claim:

- The source-policy no-native-text OCR route now has an owner decision record that keeps transcript text and hashes out of the repository until source-rights response evidence exists.

Cannot claim:

- Rights are cleared, a request was sent, a response was received, source-rights owner approval is recorded, a reference transcript exists, transcript collection has happened, OCR output is correct, OCR quality is benchmarked, CER/WER can be computed, robust PDF extraction works, arbitrary-market PDF parsing is reliable, or the product is complete.

## Next Gate If Passed

```text
source_policy_no_native_text_ocr_rights_request_delivery_record_v0
```
