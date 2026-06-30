# Source-policy No-native-text OCR Owner Rights Decision Record

Phase marker: source_policy_no_native_text_ocr_owner_rights_decision_record_v0.

This report records a repository-owner hold decision for the preserved NARA no-native-text route.

It is not rights clearance evidence.

It is not request-sent evidence.

It is not source-rights approval evidence.

It is not source-rights owner decision evidence.

It is not transcript collection evidence.

It is not reference transcript availability.

It is not OCR quality evidence.

It is not CER/WER support.

It is not robust PDF extraction evidence.

## Gate Result

previous_gate -> source_policy_no_native_text_ocr_source_rights_review_request_packet_v0
decision_status -> owner_decision_recorded_blocked_pending_source_rights_response
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
target_fixture_id -> nara_911_mfr_00282_no_native_text_candidate
source_sha256 -> 6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba
source_policy_url -> https://www.archives.gov/global-pages/privacy.html
repository_commit_policy -> metadata_only_no_transcript_text_or_hash
transcript_collection_allowed -> false
transcript_collection_performed -> false
reference_text_available -> false
reference_text_commit_allowed -> false
transcript_hash_commit_allowed -> false
transcript_hash_committed -> false
quality_eval_performed -> false
cer_computed -> false
wer_computed -> false
metric_candidates -> cer, wer
metric_candidates_status -> blocked_until_request_sent_rights_response_and_reference_text_exist
raw_reference_text_committed -> false
raw_ocr_text_committed -> false

## Decision Basis

- request_packet_prepared
- request_not_sent
- no_rights_response_received
- no_source_rights_owner_approval_recorded
- nara_policy_does_not_guarantee_item_specific_rights_status
- ocr_quality_metrics_require_reference_text

## Blocked Actions

- collect_reference_transcript
- commit_reference_transcript_text
- commit_reference_transcript_hash
- compute_cer
- compute_wer
- claim_ocr_quality
- claim_robust_pdf_extraction

## Allowed Actions

- keep_metadata_only_request_packet
- prepare_or_send_owner_runtime_rights_request
- record_future_rights_response_metadata
- keep_public_claims_blocked

## Claim Boundary

can_claim_owner_rights_decision_record -> true
can_claim_rights_clearance -> false
can_claim_request_sent -> false
can_claim_source_rights_owner_approval -> false
can_claim_transcript_collection -> false
can_claim_reference_transcript_available -> false
can_claim_ocr_quality -> false
can_claim_robust_pdf_extraction -> false

## Warnings

- This is a repository-owner hold decision record only.
- It does not send a rights request or record a source-rights response.
- It does not record rights clearance or source-rights owner approval.
- It blocks transcript collection, transcript text commits, and transcript hash commits.
- CER/WER remain blocked until request delivery, rights response, and reference text exist.

## Next Gate

source_policy_no_native_text_ocr_rights_request_delivery_record_v0
