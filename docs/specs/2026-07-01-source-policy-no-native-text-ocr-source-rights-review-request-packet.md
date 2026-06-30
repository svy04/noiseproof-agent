# Source-policy No-native-text OCR Source Rights Review Request Packet Spec

status: draft_for_tdd

date: 2026-07-01

target_gate: source_policy_no_native_text_ocr_source_rights_review_request_packet_v0

previous_gate: source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0

recommended_next_gate_after_this_spec:

```text
source_policy_no_native_text_ocr_owner_rights_decision_record_v0
```

## Current Repo State

- `source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0` is accepted on main.
- The accepted plan defines an owner-runtime transcript collection workflow only.
- `source_rights_owner_approval_recorded` remains false.
- No transcript text, transcript hash, source PDF, raw OCR text, raw reference text, page images, screenshots, local paths, or tessdata paths are committed.

## Sources To Absorb

- OCR-D evaluation: OCR quality scoring needs reference/ground-truth text and OCR output comparison.
- JiWER: WER/CER-style metrics require reference and hypothesis strings after normalization/alignment decisions.
- NARA policy: NARA access and reproduction policies do not guarantee item-specific rights clearance for all records; the requester remains responsible for copyright or other restrictions.
- Existing owner transcript collection plan: the request packet can prepare a rights-review question, but cannot record source-rights approval, transcript availability, or OCR quality evidence.

## Non-goals

- Do not collect, write, or commit a transcript.
- Do not record source-rights owner approval as completed.
- Do not commit a transcript hash.
- Do not contact external rights owners or claim a response was received.
- Do not run OCR.
- Do not evaluate OCR recognition quality.
- Do not compute CER, WER, precision, recall, accuracy, or benchmark scores.
- Do not add JiWER as a dependency.
- Do not commit source PDFs, download caches, local paths, tessdata paths, raw native text, raw OCR text, page-level transcripts, page images, screenshots, or table rows.
- Do not implement retrieval, Evidence Ledger, Critic / Noise Gate, final reports, dashboard, DB persistence, or hosted deployment.
- Do not call LLMs.
- Do not claim rights clearance, transcript collection, reference transcript availability, robust PDF extraction, arbitrary-market OCR reliability, OCR benchmark quality, external reviewer feedback, or product completeness.

## Implementation Scope

- Add a deterministic source-rights review request packet module.
- Load the accepted owner transcript collection plan artifact.
- Produce a sanitized request packet artifact that records:
  - source policy route
  - target fixture identity and hash
  - previous owner transcript collection plan marker
  - rights review questions
  - proposed use scope
  - material requested for review
  - repository non-commit policy
  - explicit non-claims and next gate
- Add a deterministic report builder and CLI check mode.
- Update reviewer/public proof surfaces and CI staleness checks.

## Data Or API Contract

Committed source-rights review request packet:

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-source-rights-review-request-packet.json
```

Committed report:

```text
docs/evaluation/source-policy-no-native-text-ocr-source-rights-review-request-packet-report.md
```

Required committed summary fields:

```text
phase_marker -> source_policy_no_native_text_ocr_source_rights_review_request_packet_v0
previous_gate -> source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0
packet_status -> source_rights_review_request_packet_prepared
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
owner_transcript_collection_plan_phase_marker -> source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0
request_scope -> rights_review_request_only
request_question_count -> 5
proposed_use_scope -> internal_owner_runtime_reference_transcript_for_ocr_quality_eval
material_requested_for_review_count -> 5
repository_commit_policy -> metadata_only_no_transcript_text_or_hash
request_packet_prepared -> true
request_sent -> false
rights_response_received -> false
source_rights_owner_approval_recorded -> false
source_rights_decision_recorded -> false
transcript_collection_performed -> false
reference_text_available -> false
reference_text_commit_allowed -> false
transcript_hash_committed -> false
quality_eval_performed -> false
cer_computed -> false
wer_computed -> false
metric_candidates_status -> blocked_until_rights_decision_and_reference_text_exist
raw_reference_text_committed -> false
raw_ocr_text_committed -> false
can_claim_source_rights_review_request_packet -> true
can_claim_rights_clearance -> false
can_claim_transcript_collection -> false
can_claim_reference_transcript_available -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_no_native_text_ocr_owner_rights_decision_record_v0
```

Required rights review questions:

```text
does_item_have_known_copyright_or_access_restrictions
may_owner_create_manual_reference_transcript_for_internal_ocr_quality_eval
may_reference_transcript_text_be_committed_publicly
may_reference_transcript_hash_or_page_level_metadata_be_committed_publicly
what_attribution_or_restriction_notice_is_required
```

Required material requested for review:

```text
source_url
source_policy_url
source_sha256
target_page_count
proposed_repository_commit_policy
```

## Tests

- `apps/api/tests/test_source_policy_no_native_text_ocr_source_rights_review_request_packet.py`
- RED must fail because the new request-packet module does not exist.
- GREEN must pass committed packet/report checks, command check mode, rejection tests, artifact safety checks, proof-surface links, proof-gap registry updates, and CI staleness checks.

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

- Stop if the implementation is asked to send a rights request or claim a rights response.
- Stop if the implementation records source-rights owner approval as completed without evidence.
- Stop if the implementation collects or commits transcript text.
- Stop if the implementation commits transcript hashes before a rights decision.
- Stop if the implementation tries to compute CER/WER without reference text.
- Stop if any artifact would require committing raw OCR text, raw reference text, source PDFs, page images, screenshots, local paths, or tessdata paths.
- Stop if the implementation drifts into retrieval, Evidence Ledger, Critic / Noise Gate, final report generation, dashboard, DB persistence, or hosted deployment.

## Claim Boundaries

Implemented:

- A deterministic source-rights review request packet for the preserved NARA no-native-text OCR route.

Not implemented:

- Request sending, source-rights approval completion, rights decision recording, transcript collection, transcript hash commitment, reference transcript availability, OCR quality scoring, CER/WER computation, robust PDF extraction, arbitrary-market OCR reliability, retrieval, Evidence Ledger, Critic / Noise Gate, final report generation, dashboard, hosted deployment, external reviewer feedback.

Can claim:

- The source-policy no-native-text OCR route now has a rights-review request packet that defines the questions and metadata needed before transcript text or hashes can enter the repository.

Cannot claim:

- Rights are cleared, a response was received, a reference transcript exists, transcript collection has happened, source-rights owner approval is recorded, OCR output is correct, OCR quality is benchmarked, CER/WER can be computed, robust PDF extraction works, arbitrary-market PDF parsing is reliable, or the product is complete.

## Next Gate If Passed

```text
source_policy_no_native_text_ocr_owner_rights_decision_record_v0
```
