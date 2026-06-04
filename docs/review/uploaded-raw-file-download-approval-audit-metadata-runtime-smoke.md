# Uploaded Raw File Download Approval Audit Metadata Runtime Smoke

Status: completed.

Phase marker: uploaded raw file download approval audit metadata runtime smoke v0.

## Purpose

Verify the approval audit metadata enrichment through local Docker FastAPI plus
PostgreSQL runtime, not only route tests.

Evidence type: local Docker FastAPI plus PostgreSQL.

This proves the running API can execute:

```text
upload raw file
-> create clean scan metadata
-> create active local manual approval
-> download raw file
-> list raw file download audit events
```

and show the approval context in the allowed download event metadata.

## Runtime Environment

```powershell
docker compose --profile api up -d --build api
```

Observed:

```text
Container noiseproof-agent-db Healthy
Container noiseproof-agent-api Started
```

Health check:

```text
GET /health -> {"status":"ok","service":"noiseproof-agent-api"}
```

## Smoke Result

Observed JSON:

```json
{
  "approval_boundary": "local_v0_manual_operator_approval_not_production_auth",
  "approval_status": "approved",
  "download_http": 200,
  "event_approval_boundary": "local_v0_manual_operator_approval_not_production_auth",
  "event_approval_expires_at_present": true,
  "event_approval_latest_scan_result_id_matches": true,
  "event_approval_scan_result_matches_latest": true,
  "event_approval_status": "approved",
  "event_approved_by_label": "local-operator-phase-422",
  "event_authorization_boundary": "local_v0_no_auth_not_production",
  "event_count_for_raw_file": 1,
  "event_download_approval_id_matches": true,
  "event_download_result": "allowed",
  "event_http_status_code": 200,
  "event_identity_boundary": "operator_label_not_authenticated_identity",
  "health_status": "ok",
  "identity_boundary": "operator_label_not_authenticated_identity",
  "raw_file_id": "fe8c1ac2-ca63-4082-97bb-51944c151597",
  "scan_status": "completed",
  "scan_verdict": "clean"
}
```

Flattened evidence:

```text
health_status: ok
scan_status: completed
scan_verdict: clean
approval_status: approved
download_http: 200
event_download_result: allowed
event_http_status_code: 200
event_download_approval_id_matches: true
event_approval_status: approved
event_approval_expires_at_present: true
event_approval_latest_scan_result_id_matches: true
event_approval_scan_result_matches_latest: true
event_approval_boundary: local_v0_manual_operator_approval_not_production_auth
event_identity_boundary: operator_label_not_authenticated_identity
event_authorization_boundary: local_v0_no_auth_not_production
event_count_for_raw_file: 1
```

## Boundary

This is local Docker runtime evidence only.

This is not production authorization.

This is not authenticated user identity.

This is not signed URL support.

This is not RBAC, ABAC, or ReBAC.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not malware detection proof.

It is not customer validation, Braincrew acceptance, robust file serving,
automatic failure-case creation, complete workflow failure causality,
autonomous/LLM-backed agents, or product-complete.

## Next Gate

```text
external reviewer approval-audit-metadata request refresh v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
