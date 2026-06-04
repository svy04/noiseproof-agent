# Uploaded Raw File Download Approval Gate Behavior Runtime Smoke

Status: implemented

Phase label:

```text
uploaded raw file download approval gate behavior runtime smoke v0
```

## Goal

Verify the raw file download approval gate through local Docker FastAPI plus PostgreSQL, not only through in-memory route tests.

This smoke checks that a guarded raw file download requires:

```text
latest clean scan result
active download approval for that latest scan result
```

## Runtime

Runtime target:

```text
local Docker FastAPI plus PostgreSQL
```

Commands run:

```bash
docker compose --profile api config
docker compose --profile api up -d --build api
uv run python -m app.migration_runner --database-url postgresql://noiseproof:noiseproof@localhost:55432/noiseproof --status
uv run python -m app.migration_runner --database-url postgresql://noiseproof:noiseproof@localhost:55432/noiseproof
uv run python -m app.migration_runner --database-url postgresql://noiseproof:noiseproof@localhost:55432/noiseproof --status
```

Migration runner evidence:

```text
Applied migrations: 20
Pending migrations: 1
pending 022_raw_file_download_event_approval_block_reasons.sql
applied 022_raw_file_download_event_approval_block_reasons.sql
Applied migrations: 21
Pending migrations: 0
```

The runtime DB constraint for `raw_file_download_events.blocked_reason` includes:

```text
missing_download_approval
revoked_or_expired_download_approval
```

Relevant migration:

```text
db/migrations/022_raw_file_download_event_approval_block_reasons.sql
```

## Observed HTTP Evidence

Health and ops:

```text
health_status: 200
ops_status: 200
```

Latest clean scan but no approval:

```text
clean_without_approval_status: 409
clean_without_approval_detail: active download approval required before raw file download
clean_without_approval_blocked_reason: missing_download_approval
```

Latest clean scan with a non-active revoked approval candidate:

```text
revoked_approval_create_status: 201
revoked_approval_status: 409
revoked_approval_detail: active download approval required before raw file download
revoked_approval_blocked_reason: revoked_or_expired_download_approval
```

Latest clean scan with active approval:

```text
active_approval_create_status: 201
active_approval_status: 200
active_download_boundary: scan_first_latest_clean_result_and_active_approval_required
active_approval_event_result: allowed
download_approval_id_present: true
download_approval_id_matches: true
active_approval_boundary: local_v0_manual_operator_approval_not_production_auth
active_identity_boundary: operator_label_not_authenticated_identity
```

## Interpretation

The live API can now block clean scanned raw file downloads without active approval, distinguish missing approval from a non-active approval candidate, and allow the download only when an active approval is tied to the latest clean scan result.

Allowed audit events include `download_approval_id` in `metadata_json`.

## Boundaries

This is local runtime evidence only.

It is:

```text
not production authorization
not user identity
not signed URL support
not RBAC
not ABAC
not ReBAC
not hosted deployment evidence
not external reviewer feedback
not malware detection proof
not product-complete
```

The approval is still a local manual operator-label boundary:

```text
local_v0_manual_operator_approval_not_production_auth
operator_label_not_authenticated_identity
```

## Next Gate

Recommended next gate:

```text
external reviewer request refresh for the approval gate runtime smoke, or another source-first product gate selected from docs/GOAL.md
```
