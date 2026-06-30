# Source-policy No-native-text OCR Rights Request Delivery Record Spec

status: draft_for_tdd

date: 2026-07-01

target_gate: source_policy_no_native_text_ocr_rights_request_delivery_record_v0

previous_gate: source_policy_no_native_text_ocr_owner_rights_decision_record_v0

recommended_next_gate_after_this_spec:

```text
source_policy_no_native_text_ocr_owner_runtime_rights_request_delivery_v0
```

## Current Repo State

- `source_policy_no_native_text_ocr_owner_rights_decision_record_v0` is accepted on main.
- The owner decision record blocks transcript collection and transcript/hash commits until source-rights response evidence exists.
- `request_sent` remains false.
- `source_rights_request_delivery_performed` remains false.
- No owner contact identity, delivery timestamp, delivery receipt, rights response, source-rights owner approval, transcript text, transcript hash, source PDF, raw OCR text, raw reference text, page images, screenshots, local paths, or tessdata paths are committed.

## Sources To Absorb

- NARA Privacy and Use Policies: access/reproduction policy is not item-specific clearance for all holdings; restrictions and copyright uncertainty can remain.
- NARA contact/reference patterns: specific record questions should go through official NARA contact/reference routes, but this repository must not send on behalf of the owner or commit private contact identity.
- OCR-D evaluation: OCR quality scoring needs ground-truth/reference text and OCR output comparison.
- JiWER: WER/CER-style metrics require reference and hypothesis strings after normalization/alignment decisions.
- Existing owner rights decision record: the repository can record delivery route readiness and missing delivery evidence, but cannot record request delivery or rights response without evidence.

## Non-goals

- Do not send a rights request.
- Do not record request delivery as performed.
- Do not record a delivery timestamp, receipt, ticket, message id, or response.
- Do not record source-rights owner approval as completed.
- Do not commit owner private contact identity, email account details, browser session screenshots, or form submission contents.
- Do not collect, write, or commit a transcript.
- Do not permit transcript text or transcript hashes to enter the repository.
- Do not compute CER, WER, precision, recall, accuracy, or benchmark scores.
- Do not run OCR.
- Do not add JiWER as a dependency.
- Do not commit source PDFs, download caches, local paths, tessdata paths, raw native text, raw OCR text, page-level transcripts, page images, screenshots, or table rows.
- Do not implement retrieval, Evidence Ledger, Critic / Noise Gate, final reports, dashboard, DB persistence, hosted deployment, or LLM calls.
- Do not claim rights clearance, request delivery, source-rights approval, transcript collection, reference transcript availability, robust PDF extraction, arbitrary-market OCR reliability, OCR benchmark quality, external reviewer feedback, or product completeness.

## Implementation Scope

- Add a deterministic rights request delivery record module.
- Load the accepted owner rights decision record artifact.
- Produce a sanitized delivery record artifact that records:
  - previous owner rights decision marker
  - target fixture identity and hash
  - delivery status
  - official delivery route candidates
  - required delivery evidence
  - missing owner-runtime inputs
  - blocked repository actions
  - explicit non-claims and next gate
- Add a deterministic report builder and CLI check mode.
- Update reviewer/public proof surfaces and CI staleness checks.

## Data Or API Contract

Committed rights request delivery record:

```text
examples/pdf-extraction-quality/source-policy-no-native-text-ocr-rights-request-delivery-record.json
```

Committed report:

```text
docs/evaluation/source-policy-no-native-text-ocr-rights-request-delivery-record-report.md
```

Required committed summary fields:

```text
phase_marker -> source_policy_no_native_text_ocr_rights_request_delivery_record_v0
previous_gate -> source_policy_no_native_text_ocr_owner_rights_decision_record_v0
delivery_status -> delivery_record_prepared_request_not_sent
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
owner_rights_decision_record_phase_marker -> source_policy_no_native_text_ocr_owner_rights_decision_record_v0
delivery_scope -> owner_runtime_external_rights_request_delivery
request_packet_prepared -> true
owner_rights_decision_recorded -> true
request_sent -> false
source_rights_request_delivery_performed -> false
delivery_channel_selected -> false
delivery_destination_recorded -> false
delivery_timestamp_recorded -> false
delivery_receipt_recorded -> false
owner_contact_identity_available -> false
owner_contact_identity_committed -> false
rights_response_received -> false
source_rights_owner_approval_recorded -> false
source_rights_owner_decision_recorded -> false
transcript_collection_allowed -> false
transcript_collection_performed -> false
reference_text_available -> false
reference_text_commit_allowed -> false
transcript_hash_commit_allowed -> false
transcript_hash_committed -> false
quality_eval_performed -> false
cer_computed -> false
wer_computed -> false
metric_candidates_status -> blocked_until_owner_runtime_delivery_response_and_reference_text_exist
raw_reference_text_committed -> false
raw_ocr_text_committed -> false
can_claim_rights_request_delivery_record -> true
can_claim_request_sent -> false
can_claim_delivery_performed -> false
can_claim_rights_clearance -> false
can_claim_source_rights_owner_approval -> false
can_claim_transcript_collection -> false
can_claim_reference_transcript_available -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> source_policy_no_native_text_ocr_owner_runtime_rights_request_delivery_v0
```

Required delivery route candidates:

```text
nara_contact_form
nara_reference_staff_consultation
nara_general_inquiry_channel
```

Required delivery evidence if future delivery happens:

```text
owner_runtime_contact_identity_available
delivery_channel
delivery_destination
delivery_timestamp
delivery_receipt_or_ticket_id
sent_request_summary
non_commit_private_contact_boundary
```

Required missing owner-runtime inputs:

```text
owner_contact_identity
delivery_channel_selection
delivery_destination_confirmation
owner_runtime_submission
delivery_receipt_or_ticket_id
```

## Tests

- `apps/api/tests/test_source_policy_no_native_text_ocr_rights_request_delivery_record.py`
- RED must fail because the new delivery record module does not exist.
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

- Stop if the implementation is asked to record request delivery without evidence.
- Stop if the implementation is asked to send the request from a non-owner account.
- Stop if the implementation would commit owner private contact identity, browser screenshots, form payloads, or message contents.
- Stop if the implementation records rights response or source-rights owner approval without evidence.
- Stop if the implementation collects or commits transcript text.
- Stop if the implementation permits transcript hashes before a source-rights response.
- Stop if the implementation tries to compute CER/WER without reference text.
- Stop if any artifact would require committing raw OCR text, raw reference text, source PDFs, page images, screenshots, local paths, or tessdata paths.
- Stop if the implementation drifts into retrieval, Evidence Ledger, Critic / Noise Gate, final report generation, dashboard, DB persistence, hosted deployment, or LLM calls.

## Claim Boundaries

Implemented:

- A deterministic rights request delivery record that identifies official delivery route candidates and the missing owner-runtime evidence required before `request_sent` can become true.

Not implemented:

- Request delivery, source-rights response, source-rights approval completion, source-rights clearance, transcript collection, transcript hash commitment, reference transcript availability, OCR quality scoring, CER/WER computation, robust PDF extraction, arbitrary-market OCR reliability, retrieval, Evidence Ledger, Critic / Noise Gate, final report generation, dashboard, hosted deployment, external reviewer feedback.

Can claim:

- The source-policy no-native-text OCR route now has a delivery record showing the required owner-runtime delivery evidence and why request delivery remains unproven.

Cannot claim:

- A request was sent, rights are cleared, a response was received, source-rights owner approval is recorded, a reference transcript exists, transcript collection has happened, OCR output is correct, OCR quality is benchmarked, CER/WER can be computed, robust PDF extraction works, arbitrary-market PDF parsing is reliable, or the product is complete.

## Next Gate If Passed

```text
source_policy_no_native_text_ocr_owner_runtime_rights_request_delivery_v0
```
