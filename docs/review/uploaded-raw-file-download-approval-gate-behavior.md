# Uploaded Raw File Download Approval Gate Behavior

Status: implemented.

Phase marker: uploaded raw file download approval gate behavior v0.

## Purpose

Wire the active approval helper into the guarded raw file download route.

This changes local v0 route behavior from:

```text
latest clean scan required
```

to:

```text
latest clean scan and active approval required
```

## Implemented Rule

The download route now requires:

```text
latest clean scan and active approval required
```

The route calls:

```text
find_active_raw_file_download_approval
```

after:

```text
raw file exists
rate limit allows the attempt
latest scan result is completed / clean
quarantine_status is stored_quarantined
```

and before raw bytes are returned.

## Block Reasons

The route can now write approval-specific blocked audit events:

```text
missing_download_approval
revoked_or_expired_download_approval
```

The response detail is:

```text
active download approval required before raw file download
```

## Allowed Audit Metadata

Allowed download events now include:

```text
download_approval_id
approval_boundary
identity_boundary
approved_by_label
```

The download response header now uses:

```text
X-NoiseProof-Download-Boundary: scan_first_latest_clean_result_and_active_approval_required
```

## Tests

Focused tests:

```text
tests/test_routes.py::test_document_upload_raw_file_download_requires_active_approval_after_latest_clean_scan
tests/test_routes.py::test_document_upload_raw_file_download_blocks_expired_approval_after_latest_clean_scan
tests/test_routes.py::test_document_upload_raw_file_download_returns_bytes_after_latest_clean_scan_and_active_approval
tests/test_routes.py::test_document_upload_raw_file_download_records_allowed_audit_event
tests/test_docs.py::test_uploaded_raw_file_download_approval_gate_behavior_documents_route_enforcement
```

## Explicit Non-claims

This is local v0 route behavior.

This is not production authorization.

This is not user identity.

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
uploaded raw file download approval gate behavior runtime smoke v0
```

That gate should verify the new local v0 behavior through Docker FastAPI plus PostgreSQL before any reviewer-facing proof refresh.
