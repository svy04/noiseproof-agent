# External Review Issue Body Download-audit Refresh

Status: live issue body refresh completed.

Phase marker: external review issue body download-audit refresh v0.

## Purpose

This gate records the owner-authored issue #1 body edit that points external reviewers to the raw file download audit runtime smoke and request refresh.

It keeps external reviewer feedback v0 pending.

It does not accept feedback.

It does not close the external feedback gate.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed issue state after edit:

```json
{
  "updatedAt": "2026-06-04T13:57:17Z",
  "state": "OPEN",
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_download_audit_proof": true,
  "has_download_audit_request_refresh": true,
  "has_external_feedback_boundary": true,
  "comment_count": 1,
  "labels": "external-review,feedback"
}
```

## Added Issue Links

```text
docs/review/uploaded-raw-file-download-audit-runtime-smoke.md
docs/review/external-reviewer-download-audit-request-refresh.md
```

The issue body now points reviewers to:

```text
raw file download audit runtime smoke
External reviewer download-audit request refresh
```

## Added Boundary

The issue body now states that the raw file download audit runtime smoke records:

```text
raw_file_download_events
missing-scan download returns `409`
same-file no-scan attempts return `[409, 409, 409, 409, 409]` then `429`
separate clean file downloads with `200`
latest clean scan id linked on the allowed event
not hosted deployment evidence
not external reviewer feedback
not production authorization
not user identity
not malware detection proof
not endpoint malicious-detection runtime proof
not product-complete
```

The request refresh boundary also states:

```text
owner-authored request-surface update only
does not close external reviewer feedback v0
not hosted deployment evidence
not production authorization
not user identity
not malware detection proof
not endpoint malicious-detection runtime proof
not product-complete
```

## Verification Command

```powershell
gh issue view 1 --repo svy04/noiseproof-agent --json body,comments,updatedAt,state,url,labels
```

Text markers:

```text
starts_with_request: true
first_codepoint: 35
comment_count: 1
has_download_audit_proof: true
has_download_audit_request_refresh: true
```

## Boundary

This is an owner-authored issue body edit.

This does not close external reviewer feedback v0.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not production authorization.

This is not user identity.

This is not malware detection proof.

This is not endpoint malicious-detection runtime proof.

It is not customer validation, Braincrew acceptance, production readiness, robust file serving, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
external feedback current-state download-audit issue verification v0
```

Current-state verification artifact:

```text
docs/review/external-feedback-current-state-download-audit-issue-verification.md
```
