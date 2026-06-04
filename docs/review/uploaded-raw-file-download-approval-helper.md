# Uploaded Raw File Download Approval Helper

Status: implemented.

Phase marker: uploaded raw file download approval helper v0.

## Purpose

Add a repository-only helper for finding one active local manual approval row.

This follows the Phase 409 gate behavior review.

It does not change the raw download route.

It does not enforce approvals.

It does not implement production authorization.

It does not create user identity.

It does not add signed URL support.

## Implemented Boundary

The implemented helper is:

```text
find_active_raw_file_download_approval
```

This is a repository-only helper.

It accepts:

```text
raw_file_id
latest_scan_result_id
now
```

It returns the newest matching row or `None`.

## Active Approval Rule

The helper checks:

```text
raw_file_id matches
latest_scan_result_id matches
approval_status = approved
expires_at > now
revoked_at IS NULL
```

The SQL orders by:

```text
created_at DESC, id DESC
LIMIT 1
```

The helper does not inspect raw bytes.

The helper does not create download events.

The helper does not allow a download.

## Tests

Focused tests:

```text
tests/test_db.py::test_find_active_raw_file_download_approval_requires_active_matching_row
tests/test_db.py::test_find_active_raw_file_download_approval_returns_none_without_row
tests/test_docs.py::test_uploaded_raw_file_download_approval_helper_documents_repository_only_code
```

## Explicit Non-claims

This is repository-only helper code.

This is not route behavior.

This is not approval enforcement.

This is not production authorization.

This is not user identity.

This is not signed URL support.

This is not RBAC.

This is not ABAC.

This is not ReBAC.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.

## Next Gate

```text
uploaded raw file download approval gate behavior v0
```

That gate may wire the helper into the guarded raw download route, but it should preserve deny-by-default behavior, latest clean scan evidence, local boundary strings, and audit events. It should not claim production authorization, authenticated identity, signed URL support, RBAC, ABAC, ReBAC, or hosted evidence.
