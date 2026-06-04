# Uploaded Raw File Download Approval Repository

Status: implemented.

Phase marker: uploaded raw file download approval repository v0.

## Purpose

This gate adds repository-only persistence for caller-provided manual approval rows in `raw_file_download_approvals`.

It follows the Phase 404 review boundary.

It does not add endpoint code.

It does not change download route behavior.

It does not enforce approvals.

It does not implement production authorization.

It does not create user identity.

## Implemented Boundary

The implemented repository boundary is:

```text
RawFileDownloadApprovalCreate
RawFileDownloadApprovalOut
create_raw_file_download_approval
list_raw_file_download_approvals
```

`RawFileDownloadApprovalCreate` accepts caller-provided manual approval fields.

`approved_by_label` remains an operator-provided label, not authenticated user identity.

`create_raw_file_download_approval` inserts caller-provided manual approval rows.

`list_raw_file_download_approvals` returns approval rows for operator inspection.

## Repository Behavior

`create_raw_file_download_approval` writes to:

```text
raw_file_download_approvals
```

It stores:

```text
raw_file_id
latest_scan_result_id
approval_status
approval_reason
approved_by_label
expires_at
revoked_at
metadata_json
approval_boundary
identity_boundary
```

It does not inspect raw bytes.

It does not decide whether the file can be downloaded.

It does not write a download event.

It does not create a signed URL.

`list_raw_file_download_approvals` supports:

```text
raw_file_id
approval_status
limit
```

It orders rows by:

```text
created_at DESC, id DESC
```

## Local Boundary Defaults

The schema defaults remain explicit:

```text
approval_status = approved
metadata_json = {}
approval_boundary = local_v0_manual_operator_approval_not_production_auth
identity_boundary = operator_label_not_authenticated_identity
```

These names are intentionally loud.

They prevent a reader from mistaking local v0 manual approval records for production authorization, authenticated identity, or signed URL access control.

## Tests

Focused tests:

```text
tests/test_db.py::test_raw_file_download_approval_create_defaults_preserve_local_boundaries
tests/test_db.py::test_create_raw_file_download_approval_inserts_manual_row_without_authorization_enforcement
tests/test_db.py::test_list_raw_file_download_approvals_filters_without_allowing_downloads
tests/test_docs.py::test_uploaded_raw_file_download_approval_repository_documents_code_boundary
```

## Explicit Non-claims

This is repository code only.

This is not endpoint code.

This does not add endpoint code.

This does not change download route behavior.

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
uploaded raw file download approval endpoint review v0
```

That gate may select a small metadata-only endpoint boundary, but it should not change guarded raw download behavior, enforce production authorization, infer authenticated identity, add signed URL support, or claim hosted evidence.
