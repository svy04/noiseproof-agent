# Uploaded Raw File Download Approval Schema

Status: schema-only.

Phase marker: uploaded raw file download approval schema v0.

## Purpose

Add a local manual approval table before changing guarded raw file download behavior.

This gate creates:

```text
raw_file_download_approvals
```

Migration:

```text
db/migrations/021_raw_file_download_approvals.sql
```

Fresh schema:

```text
db/init/001_schema.sql
```

## Schema

The schema records a local operator approval for future guarded raw file downloads.

Core fields:

```text
id
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
created_at
```

Status values:

```text
approved
revoked
expired
```

Default boundaries:

```text
approval_boundary: local_v0_manual_operator_approval_not_production_auth
identity_boundary: operator_label_not_authenticated_identity
```

`approved_by_label` is an operator-provided label, not authenticated user identity.

## Intended Future Use

Future guarded downloads may require:

```text
latest scan result is completed / clean
active approval exists for raw_file_id
approval latest_scan_result_id matches the latest clean scan result
approval has not expired
approval has not been revoked
local rate limit has not been exceeded
```

Future blocked reason:

```text
missing_download_approval
```

## Current Behavior

This phase is schema-only.

Download route behavior unchanged.

Marker:

```text
download route behavior unchanged
```

No endpoint reads or writes `raw_file_download_approvals` yet.

No repository method reads or writes `raw_file_download_approvals` yet.

## Boundary

This is schema only.

This is not endpoint code.

This is not repository code.

This is not download route behavior.

This is not production authorization.

This is not user identity.

This is not signed URL support.

This is not RBAC.

This is not ABAC.

This is not ReBAC.

This is not hosted deployment evidence.

It is not customer validation, Braincrew acceptance, production readiness, malware detection proof, endpoint malicious-detection runtime proof, automatic failure-case creation, complete workflow failure causality, or product-complete.

## Next Gate

```text
uploaded raw file download approval schema runtime verification v0
```
