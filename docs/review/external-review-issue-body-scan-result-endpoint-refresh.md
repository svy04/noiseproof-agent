# External Review Issue Body Scan-result Endpoint Refresh

Status: owner-authored issue edit.

Phase marker: external review issue body scan-result endpoint refresh v0.

Public issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

This records a live owner-authored issue body refresh that points reviewers to the uploaded raw file scan result endpoint proof.

## Observed issue body markers

Observed after owner-authored issue edit:

```text
viewer: svy04
repo_owner: svy04
issue_author: svy04
updatedAt: 2026-06-03T02:07:48Z
first_codepoint: 35
startsWith: ## Request
comment_count: 1
owner_comment_count: 1
```

The issue body now includes:

```text
uploaded raw file scan result endpoint proof
docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md
POST /documents/upload-raw-files/{raw_file_id}/scan-results
GET /documents/upload-raw-files/{raw_file_id}/scan-results
path/body mismatch -> 400
scan_verdict -> scan_error
response_has_raw_bytes -> false
not malware scanning
not a download endpoint
```

It also includes the request refresh proof:

```text
docs/review/external-reviewer-scan-result-endpoint-request-refresh.md
```

## Boundary

This is an owner-authored issue edit.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not malware scanning.

This is not a download endpoint.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

This does not close external reviewer feedback v0.
