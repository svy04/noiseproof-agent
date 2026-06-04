# External Reviewer Signature-validation Request Refresh

Status: request-surface refresh.

Phase marker: external reviewer signature-validation request refresh v0.

## Purpose

Make the uploaded raw file signature validation runtime smoke discoverable from reviewer-facing repository paths.

This refresh points reviewers to:

```text
docs/review/uploaded-raw-file-signature-validation-runtime-smoke.md
```

## Updated Surfaces

```text
docs/review/external-reader-proof-path.md
docs/review/external-review-request.md
docs/review/external-reviewer-brief.md
docs/review/external-reviewer-link-map.md
docs/application/portfolio-index.md
README.md
docs/GOAL.md
docs/runbook.md
```

## Reviewer Message

The new proof to inspect is:

```text
raw file signature validation runtime smoke
```

It shows local Docker PostgreSQL plus live FastAPI HTTP evidence for:

```text
spoofed CSV upload -> 201
declared PDF mismatch -> 415
blocked response has no raw bytes
mismatch hash is not present in recent raw uploads
local_v0_magic_prefix_allowlist_not_production
```

## Boundary

This is a request-surface refresh.

This is not live issue body edit.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not robust file-type detection.

This is not malware scanning evidence.

This is not production authorization.

This is not endpoint malicious-detection runtime proof.

It is not customer validation, Braincrew acceptance, production readiness, automatic failure-case creation, autonomous workflow execution, and not product-complete.

## Next Gate

```text
external review issue body signature-validation refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
