# External Reviewer Filename-safety Request Refresh

Status: request-surface refresh.

Phase marker: external reviewer filename-safety request refresh v0.

## Purpose

Make the uploaded raw file download filename safety runtime smoke discoverable from reviewer-facing repository paths.

This refresh points reviewers to:

```text
docs/review/uploaded-raw-file-download-filename-safety-runtime-smoke.md
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
raw file download filename safety runtime smoke
```

It shows local Docker FastAPI evidence for:

```text
path-like and URL-encoded-control filename input
manual clean scan metadata handoff
guarded download -> 200
X-NoiseProof-Download-Filename-Boundary: local_v0_content_disposition_filename_safety_not_production
safe_filename_length 120
no_path/no_dotdot/no_crlf/no_injected/ends_csv/lte_120 checks all true
```

## Boundary

This is a request-surface refresh.

This is not live issue body edit.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not production authorization.

This is not robust file serving.

This is not malware detection proof.

This is not endpoint malicious-detection runtime proof.

It is not customer validation, Braincrew acceptance, production readiness, automatic failure-case creation, autonomous workflow execution, and not product-complete.

## Next Gate

```text
external review issue body filename-safety refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
