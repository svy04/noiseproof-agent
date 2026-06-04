# External Review Issue Body Guarded Download Refresh

Status: owner-authored issue body edit only.

Phase marker: external review issue body guarded download refresh v0.

## Purpose

This gate updates the live public external review issue body so reviewers can reach the guarded raw file download endpoint runtime smoke proof from issue #1.

It is request infrastructure only.

It does not add runtime behavior.

It does not close external reviewer feedback v0.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed after edit:

```json
{
  "updatedAt": "2026-06-04T10:06:04Z",
  "state": "OPEN",
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_guarded_download_proof": true,
  "has_guarded_download_request_refresh": true,
  "has_external_feedback_boundary": true,
  "comment_count": 1,
  "labels": "external-review,feedback"
}
```

Text markers:

```text
starts_with_request: true
first_codepoint: 35
comment_count: 1
has_guarded_download_proof: true
has_guarded_download_request_refresh: true
```

## Added Links

Guarded raw file download endpoint runtime smoke:

```text
docs/review/uploaded-raw-file-download-endpoint-runtime-smoke.md
```

External reviewer guarded download request refresh:

```text
docs/review/external-reviewer-guarded-download-request-refresh.md
```

## Added Boundary

The issue body now states that the guarded raw file download endpoint runtime smoke:

```text
local Docker PostgreSQL plus live FastAPI HTTP for guarded raw download
no-scan download returns 409
latest clean scan metadata returns 200 with raw bytes and nosniff/download headers
later failed scan metadata returns 409
not hosted deployment evidence
not external reviewer feedback
not production malware scanning evidence
not production authorization
not enforced download rate limiting
not product-complete
```

The request refresh boundary also states:

```text
owner-authored request-surface update only
does not close external reviewer feedback v0
not hosted deployment evidence
not production malware scanning evidence
not production authorization
not enforced download rate limiting
```

## Boundary

This is an owner-authored issue body edit.

This does not close external reviewer feedback v0.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not production malware scanning evidence.

This is not production authorization.

This is not enforced download rate limiting.

This is not endpoint malicious-detection runtime proof.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
external feedback current-state guarded download issue verification v0
```
