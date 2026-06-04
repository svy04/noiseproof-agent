# Uploaded Raw File Download Readiness Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: uploaded raw file download readiness runtime smoke v0.

## Purpose

Verify the raw file download readiness preflight through local Docker FastAPI
plus PostgreSQL, not only through route tests.

Endpoint:

```text
GET /documents/upload-raw-files/{raw_file_id}/download-readiness
```

This smoke verifies:

```text
upload raw file
-> readiness before scan
-> create clean scan metadata
-> readiness before approval
-> create active local manual approval
-> readiness after active approval
-> list download events
```

The important side-effect check is that readiness calls do not create download
events, do not consume the local download rate limit, and do not return raw
bytes.

## Runtime Environment

Commands run:

```powershell
docker compose --profile api config
docker compose --profile api up -d --build api
docker compose --profile api ps
uv run python -m app.migration_runner --database-url postgresql://noiseproof:noiseproof@localhost:55432/noiseproof --status
```

Observed:

```text
Docker version 29.4.3
Docker Compose version v5.1.3
noiseproof-agent-db Up / healthy
noiseproof-agent-api Up / port 8000
Applied migrations: 21
Pending migrations: 0
```

Evidence type:

```text
local Docker FastAPI plus PostgreSQL
```

## Observed HTTP Evidence

Observed JSON:

```json
{
  "allowed_active_approval_id_matches": true,
  "allowed_all_checks_passed": true,
  "allowed_blocked_reason": null,
  "allowed_check_names": [
    "raw_file_exists",
    "latest_clean_scan",
    "quarantine_status",
    "active_download_approval"
  ],
  "allowed_decision": "allowed",
  "allowed_http_status_code_if_download_attempted": 200,
  "allowed_latest_scan_result_id_matches": true,
  "approval_boundary": "local_v0_manual_operator_approval_not_production_auth",
  "approval_id": "574b0f9e-5c11-4a4f-b63f-2963f167422c",
  "authorization_boundary": "local_v0_no_auth_not_production",
  "clean_no_approval_blocked_reason": "missing_download_approval",
  "clean_no_approval_decision": "blocked",
  "clean_no_approval_http_status_code_if_download_attempted": 409,
  "clean_no_approval_latest_scan_result_id_matches": true,
  "clean_no_approval_rate_limit_consumed": false,
  "clean_no_approval_raw_bytes_returned": false,
  "events_after_readiness_count": 0,
  "health_status": "ok",
  "identity_boundary": "operator_label_not_authenticated_identity",
  "no_scan_blocked_reason": "missing_clean_scan",
  "no_scan_decision": "blocked",
  "no_scan_http_status_code_if_download_attempted": 409,
  "no_scan_rate_limit_consumed": false,
  "no_scan_raw_bytes_returned": false,
  "rate_limit_boundary": "local_v0_in_memory_fixed_window_not_production",
  "rate_limit_consumed": false,
  "raw_bytes_returned": false,
  "raw_file_id": "6e376a84-991c-4213-ae41-c4c6496aa26b",
  "readiness_boundary": "download_readiness_preflight_no_raw_bytes_not_authorization",
  "scan_result_id": "21a17244-6b0f-4ff8-8304-3e5b09a645d9",
  "service": "noiseproof-agent-api"
}
```

Flattened evidence:

```text
health_status: ok
service: noiseproof-agent-api
no_scan_decision: blocked
no_scan_blocked_reason: missing_clean_scan
no_scan_http_status_code_if_download_attempted: 409
no_scan_raw_bytes_returned: false
no_scan_rate_limit_consumed: false
clean_no_approval_decision: blocked
clean_no_approval_blocked_reason: missing_download_approval
clean_no_approval_http_status_code_if_download_attempted: 409
clean_no_approval_latest_scan_result_id_matches: true
clean_no_approval_raw_bytes_returned: false
clean_no_approval_rate_limit_consumed: false
allowed_decision: allowed
allowed_blocked_reason: null
allowed_http_status_code_if_download_attempted: 200
allowed_latest_scan_result_id_matches: true
allowed_active_approval_id_matches: true
allowed_all_checks_passed: true
allowed_check_names: raw_file_exists,latest_clean_scan,quarantine_status,active_download_approval
raw_bytes_returned: false
rate_limit_consumed: false
readiness_boundary: download_readiness_preflight_no_raw_bytes_not_authorization
authorization_boundary: local_v0_no_auth_not_production
rate_limit_boundary: local_v0_in_memory_fixed_window_not_production
approval_boundary: local_v0_manual_operator_approval_not_production_auth
identity_boundary: operator_label_not_authenticated_identity
events_after_readiness_count: 0
```

## Interpretation

The live API can show the current download-readiness state for a stored raw file:

- before any clean scan exists
- after a latest clean scan exists but before approval
- after a latest clean scan and active approval both exist

It does this without returning raw bytes and without creating download audit
events.

## Boundary

This is local Docker runtime evidence only.

This is not production authorization.

This is not authenticated user identity.

This is not signed URL support.

This is not RBAC, ABAC, or ReBAC.

This is not raw byte download.

This is not download audit event persistence.

This is not rate-limit consumption.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not production malware scanning evidence.

It is not customer validation, Braincrew acceptance, robust file serving,
automatic failure-case creation, complete workflow failure causality,
autonomous/LLM-backed agents, or product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, external
reviewer readiness-runtime request refresh v0, or another source-first product
gate selected from docs/GOAL.md
```
