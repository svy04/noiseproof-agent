# Uploaded Raw File Download Approval Input Guard Runtime Smoke

Status: implemented.

Phase marker: uploaded raw file download approval input guard runtime smoke v0.

## Goal

Verify the approval input guard through local Docker FastAPI plus PostgreSQL,
not only through in-memory route tests.

This smoke checks that invalid approval metadata returns `422` at the live HTTP
API boundary while valid local approval metadata can still be created and
listed.

## Runtime

Runtime target:

```text
local Docker FastAPI plus PostgreSQL
```

Commands included:

```bash
docker compose --profile api up -d --build api
```

The API image was rebuilt before the smoke so the running container included the
Phase 416 validator code.

## Observed HTTP Evidence

Healthy API:

```text
health_status: ok
```

Uploaded raw CSV plus scan metadata:

```text
raw_file_id: 05ba41e7-62b0-4d7f-90ff-774f73822f01
scan_status: completed
scan_verdict: clean
```

Valid approval metadata:

```text
valid_approval_status: approved
valid_approval_boundary: local_v0_manual_operator_approval_not_production_auth
valid_identity_boundary: operator_label_not_authenticated_identity
approval_list_count: 1
```

Unknown approval status:

```text
unknown_status_http: 422
literal_error
operator-said-ok
Input should be 'approved', 'revoked' or 'expired'
```

Already expired active approval:

```text
expired_approved_http: 422
value_error
expires_at must be in the future for approved download approvals
```

## Interpretation

The live local API now rejects an unknown manual approval status and rejects an
already expired active approval before creating approval metadata.

The valid approval path remains available for local v0 approval records.

## Boundaries

This is local runtime evidence only.

It is:

```text
not a DB schema change
not production authorization
not authenticated user identity
not signed URL support
not RBAC
not ABAC
not ReBAC
not hosted deployment evidence
not external reviewer feedback
not malware detection proof
not customer validation
not Braincrew acceptance
not product-complete
```

## Next Gate

Recommended next gate:

```text
external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
