# External Reviewer Guarded Download Request Refresh

Status: request-surface refresh.

Phase marker: external reviewer guarded download request refresh v0.

## Purpose

Make the guarded raw file download endpoint runtime smoke discoverable from reviewer-facing repository paths.

This refresh points reviewers to:

```text
docs/review/uploaded-raw-file-download-endpoint-runtime-smoke.md
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
guarded raw file download endpoint runtime smoke
```

It shows local Docker PostgreSQL plus live FastAPI HTTP evidence for:

```text
upload raw bytes
download before scan -> 409
caller-provided clean scan metadata
download after latest clean scan -> 200
later failed scan metadata
download after latest failed scan -> 409
```

## Boundary

This is a request-surface refresh.

This is not live issue body edit.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not production malware scanning evidence.

This is not endpoint malicious-detection runtime proof.

This is not production authorization.

This is not enforced download rate limiting.

It is not customer validation, Braincrew acceptance, production readiness, file signature validation, automatic failure-case creation, autonomous workflow execution, and not product-complete.
