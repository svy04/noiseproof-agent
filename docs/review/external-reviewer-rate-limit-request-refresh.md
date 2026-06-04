# External Reviewer Rate-limit Request Refresh

Status: request-surface refresh.

Phase marker: external reviewer rate-limit request refresh v0.

## Purpose

Make the guarded raw file download rate-limit runtime smoke discoverable from reviewer-facing repository paths.

This refresh points reviewers to:

```text
docs/review/uploaded-raw-file-download-rate-limit-runtime-smoke.md
```

## Updated Surfaces

```text
docs/review/external-reader-proof-path.md
docs/review/external-review-request.md
docs/review/external-reviewer-brief.md
docs/review/external-reviewer-link-map.md
docs/application/portfolio-index.md
docs/application/braincrew-role-map.md
docs/review/application-ready-review.md
README.md
docs/GOAL.md
docs/runbook.md
```

## Reviewer Message

The new proof to inspect is:

```text
guarded raw file download rate-limit runtime smoke
```

It shows local Docker PostgreSQL plus live FastAPI HTTP evidence for:

```text
same raw_file_id no-scan attempts -> 409, 409, 409, 409, 409, then 429
429 response has no raw bytes
429 response includes local_v0_in_memory_fixed_window_not_production
429 response includes local_v0_no_auth_not_production
separate clean raw file download -> 200
clean download includes local_v0_in_memory_fixed_window_not_production
clean download includes local_v0_no_auth_not_production
clean download includes nosniff
```

## Boundary

This is a request-surface refresh.

This is not live issue body edit.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not distributed rate limiting.

This is not production authorization.

This is not production malware scanning evidence.

This is not endpoint malicious-detection runtime proof.

It is not customer validation, Braincrew acceptance, production readiness, file signature validation, automatic failure-case creation, autonomous workflow execution, and not product-complete.

## Next Gate

```text
external review issue body rate-limit refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
