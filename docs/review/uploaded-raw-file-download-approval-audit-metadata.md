# Uploaded Raw File Download Approval Audit Metadata

Status: completed.

Phase marker: uploaded raw file download approval audit metadata v0.

## Purpose

Make allowed raw file download audit events more inspectable after the local
approval gate passes.

The previous allowed event recorded `download_approval_id`,
`approval_boundary`, `identity_boundary`, and `approved_by_label`. This phase
keeps those local v0 boundaries and also records the approval status, approval
expiry, approval scan-result reference, and whether that approval reference
matches the latest clean scan result used by the download route.

## Primary references checked

- OWASP Authorization Cheat Sheet:
  https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
- OWASP Logging Cheat Sheet:
  https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
- OWASP File Upload Cheat Sheet:
  https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

These references inform the direction only: security-relevant file access should
be explicit, authorization decisions should be inspectable, and logs should
capture enough context to understand what happened without pretending that a
local v0 operator label is authenticated production identity.

## Implemented Metadata

Allowed raw file download events now include these `metadata_json` fields:

```text
download_approval_id
approval_boundary
identity_boundary
approved_by_label
approval_status
approval_expires_at
approval_latest_scan_result_id
approval_scan_result_matches_latest
```

The important local boundary remains:

```text
identity_boundary: operator_label_not_authenticated_identity
```

The route also keeps:

```text
authorization_boundary: local_v0_no_auth_not_production
approval_boundary: local_v0_manual_operator_approval_not_production_auth
```

## Verification

Focused route behavior:

```powershell
cd apps/api
uv run pytest tests/test_routes.py -q -k "records_allowed_audit_event"
```

Observed result:

```text
1 passed, 138 deselected, 1 warning
```

This test first failed on missing `approval_status`, which confirmed the test
was exercising the newly added audit metadata rather than only existing
behavior.

## Boundary

This is local v0 audit metadata only.

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
approval audit metadata runtime smoke v0, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
