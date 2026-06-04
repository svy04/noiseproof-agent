# Uploaded Raw File Download Approval Input Guard

Status: implemented.

Phase marker: uploaded raw file download approval input guard v0.

## Purpose

Tighten the local v0 manual approval metadata boundary before the approval rows
feed guarded raw file downloads.

This gate prevents obviously invalid approval metadata from being accepted at
the API/model boundary instead of relying on PostgreSQL constraints or later
download behavior.

Primary reference checked: OWASP Input Validation Cheat Sheet, applied only as a
small allowlist-style input boundary for approval metadata.

## Implemented Guard

`RawFileDownloadApprovalCreate` now restricts `approval_status` to:

```text
approved
revoked
expired
```

For `approval_status = approved`, `expires_at` must be in the future.

Validation message:

```text
expires_at must be in the future for approved download approvals
```

This keeps active approval rows aligned with the existing download route rule:

```text
latest clean scan and active approval required
```

The output model remains separate from the create model so historical approval
rows that later expire can still be listed as audit records.

## Focused Test Evidence

RED observed before implementation:

```text
tests/test_routes.py::test_document_upload_raw_file_download_approval_rejects_unknown_status
expected 422, observed 201

tests/test_routes.py::test_document_upload_raw_file_download_approval_rejects_expired_active_approval
expected 422, observed 201
```

GREEN after implementation:

```text
uv run pytest tests/test_routes.py -q -k "download_approval"
5 passed, 134 deselected, 1 warning
```

## Explicit Non-claims

This is local v0 API/model input validation.

This is not a DB schema change.

This is not production authorization.

This is not authenticated user identity.

This is not signed URL support.

This is not RBAC.

This is not ABAC.

This is not ReBAC.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not malware detection proof.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
