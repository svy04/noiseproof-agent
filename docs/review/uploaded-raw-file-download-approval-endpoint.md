# Uploaded Raw File Download Approval Endpoint

Status: implemented.

Phase marker: uploaded raw file download approval endpoint v0.

## Purpose

This gate adds metadata-only create/list endpoints for caller-provided manual approval rows.

It follows the Phase 406 review boundary.

It does not change download route behavior.

It does not enforce approvals.

It does not implement production authorization.

It does not create user identity.

It does not add signed URL support.

## Implemented Routes

```text
POST /documents/upload-raw-files/{raw_file_id}/download-approvals
GET /documents/upload-raw-files/{raw_file_id}/download-approvals
```

The create route uses:

```text
RawFileDownloadApprovalCreate
RawFileDownloadApprovalOut
create_upload_raw_file_download_approval
create_raw_file_download_approval
```

The list route uses:

```text
RawFileDownloadApprovalOut
list_upload_raw_file_download_approvals
list_raw_file_download_approvals
```

The create route rejects path/body mismatch:

```text
raw_file_id path/body mismatch
```

## Behavior

The endpoint is metadata-only.

It persists and lists approval rows.

It preserves:

```text
approved_by_label
approval_boundary
identity_boundary
metadata_json
expires_at
revoked_at
```

`approved_by_label` remains an operator-provided label, not authenticated user identity.

The download route still requires latest clean scan result.

The approval endpoint does not make a failed latest scan downloadable.

## Tests

Focused tests:

```text
tests/test_routes.py::test_document_upload_raw_file_download_approval_endpoint_persists_metadata_only
tests/test_routes.py::test_document_upload_raw_file_download_approval_rejects_path_body_mismatch
tests/test_docs.py::test_uploaded_raw_file_download_approval_endpoint_documents_metadata_only_code
```

## Explicit Non-claims

This is endpoint code only.

This is metadata-only endpoint code.

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
uploaded raw file download approval endpoint runtime smoke v0
```

That gate may verify the metadata-only endpoint through local Docker FastAPI plus PostgreSQL, but it should not change guarded raw download behavior, enforce approvals, implement production authorization, infer authenticated identity, add signed URL support, or claim hosted evidence.
