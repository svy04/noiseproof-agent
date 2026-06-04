# External Review Issue Body ClamAV Malicious-detection Refresh

Status: live issue body refresh completed.

Phase marker: external review issue body clamav malicious-detection refresh v0

## Goal

Update the live public external review issue body so reviewers can reach the ClamAV API endpoint malicious-detection owner-runtime smoke from issue #1.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Linked proof:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke.md
docs/review/external-reviewer-clamav-malicious-detection-request-refresh.md
```

The new issue-body block asks reviewers to inspect:

```text
harness_status: verified_infected
scan_verdict: infected
matched_signature: Eicar-Test-Signature
payload_committed_to_repo: false
raw_payload_logged: false
```

## Observed Issue State

```json
{
  "url": "https://github.com/svy04/noiseproof-agent/issues/1",
  "updatedAt": "2026-06-04T18:22:31Z",
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_clamav_malicious_detection_proof": true,
  "has_clamav_malicious_detection_request_refresh": true,
  "has_external_feedback_boundary": true,
  "comment_count": 1
}
```

## Boundary

```text
owner-authored issue body edit only
does not close external reviewer feedback v0
not external reviewer feedback
not hosted deployment evidence
not production malware scanning evidence
not product-complete
```

This refresh changes reviewer navigation on issue #1 only. It adds no runtime behavior, schema, migration, API endpoint, external reviewer feedback, hosted deployment evidence, production malware scanning evidence, customer validation, Braincrew acceptance, or product-complete claim.

## Follow-up Current-state Verification

The current issue state after this owner-authored edit is recorded here:

```text
docs/review/external-feedback-current-state-clamav-malicious-detection-issue-verification.md
```
