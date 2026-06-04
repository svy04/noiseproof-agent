# Uploaded Raw File Download Readiness Preview

Status: implemented.

Phase marker: uploaded raw file download readiness preview v0.

## Purpose

Expose a read-only preflight view of whether a guarded uploaded raw file download
would currently pass the local v0 conditions.

This endpoint is for inspection before serving bytes. It does not download the
file, consume the local rate-limit counter, or write download audit events.

Endpoint:

```text
GET /documents/upload-raw-files/{raw_file_id}/download-readiness
```

## Source-first Basis

This gate follows the earlier source-first approval behavior review:

```text
docs/review/uploaded-raw-file-download-approval-gate-behavior-review.md
```

That review used:

- OWASP Authorization Cheat Sheet:
  https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
- OWASP API1:2023 Broken Object Level Authorization:
  https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/
- OWASP API5:2023 Broken Function Level Authorization:
  https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/
- OWASP File Upload Cheat Sheet:
  https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

Local interpretation:

```text
show the point-of-use checks before serving raw bytes
deny by default when clean scan or active approval is missing
keep local operator labels separate from authenticated production identity
```

## Implemented Behavior

The route returns:

```text
raw_file_id
decision
blocked_reason
http_status_code_if_download_attempted
latest_scan_result_id
active_approval_id
approval_boundary
identity_boundary
readiness_boundary
authorization_boundary
rate_limit_boundary
rate_limit_consumed
raw_bytes_returned
checks
```

Important fixed boundaries:

```text
readiness_boundary: download_readiness_preflight_no_raw_bytes_not_authorization
authorization_boundary: local_v0_no_auth_not_production
rate_limit_boundary: local_v0_in_memory_fixed_window_not_production
rate_limit_consumed: false
raw_bytes_returned: false
```

The check list currently includes:

```text
raw_file_exists
latest_clean_scan
quarantine_status
active_download_approval
```

## Decisions

No scan result:

```text
decision: blocked
blocked_reason: missing_clean_scan
http_status_code_if_download_attempted: 409
raw_bytes_returned: false
rate_limit_consumed: false
```

Latest clean scan but no active approval:

```text
decision: blocked
blocked_reason: missing_download_approval
http_status_code_if_download_attempted: 409
raw_bytes_returned: false
rate_limit_consumed: false
```

Latest clean scan and active approval:

```text
decision: allowed
blocked_reason: null
http_status_code_if_download_attempted: 200
raw_bytes_returned: false
rate_limit_consumed: false
```

## Verification

Focused tests:

```powershell
cd apps/api
uv run pytest tests/test_routes.py::test_document_upload_raw_file_download_readiness_blocks_without_scan_and_returns_no_raw_bytes tests/test_routes.py::test_document_upload_raw_file_download_readiness_blocks_without_active_approval tests/test_routes.py::test_document_upload_raw_file_download_readiness_allows_after_clean_scan_and_active_approval -q
```

Observed result:

```text
3 passed
```

The route tests also verify that readiness checks do not create download audit
events.

## Explicit Non-claims

This is local v0 preflight behavior only.

This is not production authorization.

This is not authenticated user identity.

This is not signed URL support.

This is not RBAC, ABAC, or ReBAC.

This is not raw byte download.

This is not audit event persistence.

This is not rate-limit consumption.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not production malware scanning evidence.

This is not robust file serving.

This is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, raw file
download readiness runtime smoke v0 if Docker/API verification is desired, or
another source-first product gate selected from docs/GOAL.md
```
