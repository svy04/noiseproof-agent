# Uploaded Raw File Download Approval Endpoint Runtime Smoke

Status: implemented.

Phase marker: uploaded raw file download approval endpoint runtime smoke v0.

## Purpose

Verify the metadata-only approval endpoint through local Docker FastAPI plus PostgreSQL.

This smoke test checks that approval metadata can be created and listed over HTTP.

It also checks that approval metadata did not override latest clean scan guard.

## Runtime Boundary

Environment:

```text
local Docker FastAPI plus PostgreSQL
```

Start command:

```powershell
docker compose --profile api up -d --build api
```

This uses the local Docker Compose `api` profile and the local PostgreSQL service.

It is not hosted deployment evidence.

## Smoke Flow

The smoke flow executed:

```text
GET /health
POST /documents/upload-raw-files
POST /documents/upload-raw-files/{raw_file_id}/scan-results
POST /documents/upload-raw-files/{raw_file_id}/download-approvals
GET /documents/upload-raw-files/{raw_file_id}/download-approvals
GET /documents/upload-raw-files/{raw_file_id}/download
GET /documents/upload-raw-files/{raw_file_id}/download-events
```

The scan metadata intentionally used:

```text
scan_status = failed
scan_verdict = scan_error
```

That makes the download guard meaningful: approval metadata must not turn a failed latest scan into a downloadable raw file.

## Observed HTTP Results

```text
GET /health -> 200
POST /documents/upload-raw-files -> 201
POST /documents/upload-raw-files/{raw_file_id}/scan-results -> 201
POST /documents/upload-raw-files/{raw_file_id}/download-approvals -> 201
GET /documents/upload-raw-files/{raw_file_id}/download-approvals -> 200
GET /documents/upload-raw-files/{raw_file_id}/download -> 409
```

Observed values:

```text
listed_approval_count: 1
download_event_count: 1
approval_id_present: true
raw_file_id_present: true
scan_result_id_present: true
approved_by_label: runtime-operator
approval_boundary: local_v0_manual_operator_approval_not_production_auth
identity_boundary: operator_label_not_authenticated_identity
download_detail: latest clean scan result required before raw file download
```

## Raw Smoke Output

```json
{
  "approval_boundary": "local_v0_manual_operator_approval_not_production_auth",
  "approval_id_present": true,
  "approval_status": 201,
  "approved_by_label": "runtime-operator",
  "download_detail": "latest clean scan result required before raw file download",
  "download_event_count": 1,
  "download_status": 409,
  "health_status": 200,
  "identity_boundary": "operator_label_not_authenticated_identity",
  "list_status": 200,
  "listed_approval_count": 1,
  "raw_file_id_present": true,
  "scan_result_id_present": true,
  "scan_status": 201,
  "upload_status": 201
}
```

## Interpretation

The metadata-only approval endpoint works locally over HTTP.

Approval rows can be created and listed.

The local boundary strings are preserved.

The guarded raw file download endpoint still blocks when the latest scan result is not clean.

approval metadata did not override latest clean scan guard.

## Explicit Non-claims

This is local runtime evidence only.

This is not approval enforcement.

This is not production authorization.

This is not user identity.

This is not signed URL support.

This is not RBAC.

This is not ABAC.

This is not ReBAC.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not malware detection proof.

This is not endpoint malicious-detection runtime proof.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.

## Next Gate

```text
uploaded raw file download approval gate behavior review v0
```

That gate may decide whether and how guarded downloads should consult unexpired, non-revoked approval rows. It should not jump straight to production authorization, authenticated identity, signed URLs, RBAC, ABAC, or hosted claims.
