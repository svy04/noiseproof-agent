# External Reviewer Download-audit Request Refresh

Status: request-surface refresh.

Phase marker: external reviewer download-audit request refresh v0.

## Purpose

Make the uploaded raw file download audit runtime smoke discoverable from reviewer-facing repository paths.

This refresh points reviewers to:

```text
docs/review/uploaded-raw-file-download-audit-runtime-smoke.md
```

## Updated Surfaces

```text
docs/review/external-reader-proof-path.md
docs/review/external-review-request.md
docs/review/external-reviewer-brief.md
docs/review/external-reviewer-link-map.md
docs/application/braincrew-role-map.md
docs/application/portfolio-index.md
README.md
docs/GOAL.md
docs/runbook.md
```

## Reviewer Message

The new proof to inspect is:

```text
raw file download audit runtime smoke
```

It shows local Docker FastAPI plus PostgreSQL evidence for:

```text
missing-scan 409
rate-limited [409, 409, 409, 409, 409, 429]
allowed 200
raw_file_download_events persistence and listing
latest clean scan id linked on the allowed event
safe filename metadata preserved as audit-allowed.csv
```

## Boundary

This is a request-surface refresh.

This is not live issue body edit.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not production authorization.

This is not user identity.

This is not malware detection proof.

This is not endpoint malicious-detection runtime proof.

It is not customer validation, Braincrew acceptance, production readiness, automatic failure-case creation, autonomous workflow execution, and not product-complete.

## Next Gate

```text
external review issue body download-audit refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
