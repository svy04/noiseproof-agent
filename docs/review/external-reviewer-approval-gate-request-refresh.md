# External Reviewer Approval-gate Request Refresh

Status: request-surface refresh.

Phase marker: external reviewer approval-gate request refresh v0.

## Purpose

Make the uploaded raw file download approval gate runtime smoke discoverable from reviewer-facing repository paths.

This refresh points reviewers to:

```text
docs/review/uploaded-raw-file-download-approval-gate-behavior-runtime-smoke.md
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
raw file download approval gate behavior runtime smoke
```

It shows local Docker FastAPI plus PostgreSQL evidence for:

```text
clean_without_approval_status: 409
clean_without_approval_blocked_reason: missing_download_approval
revoked_approval_status: 409
revoked_approval_blocked_reason: revoked_or_expired_download_approval
active_approval_status: 200
active_download_boundary: scan_first_latest_clean_result_and_active_approval_required
download_approval_id_present: true
db/migrations/022_raw_file_download_event_approval_block_reasons.sql
```

## Boundary

This is a request-surface refresh.

This is not live issue body edit.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not production authorization.

This is not user identity.

This is not signed URL support.

This is not RBAC, ABAC, or ReBAC.

This is not malware detection proof.

It is not customer validation, Braincrew acceptance, production readiness, automatic failure-case creation, autonomous workflow execution, and not product-complete.

## Next Gate

```text
external review issue body approval-gate refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
