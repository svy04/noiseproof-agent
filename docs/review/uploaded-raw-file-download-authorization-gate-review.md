# Uploaded Raw File Download Authorization Gate Review

Status: source-first review.

Phase marker: uploaded raw file download authorization gate review v0.

## Purpose

Choose the next small product gate after guarded raw file download audit events without pretending NoiseProof has production authorization.

The current guarded raw file download path is:

```text
latest clean scan required
local in-memory rate limit
filename safety
raw_file_download_events audit persistence
local_v0_no_auth_not_production
local_request_client_host_not_identity
```

That is useful local evidence, but it is still not a real authorization model.

## Sources

Primary sources used for this review:

```text
OWASP Authorization Cheat Sheet
https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

OWASP API1:2023 Broken Object Level Authorization
https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/

OWASP API5:2023 Broken Function Level Authorization
https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/

OWASP File Upload Cheat Sheet
https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html
```

Source interpretation:

```text
OWASP Authorization Cheat Sheet: authorization should deny by default, validate permissions on every request, log appropriately, and have tests.
OWASP API1:2023 Broken Object Level Authorization: every endpoint that receives an object ID and acts on the object needs object-level authorization checks.
OWASP API5:2023 Broken Function Level Authorization: function access should require explicit grants and deny by default.
OWASP File Upload Cheat Sheet: uploaded file handling must consider user permissions plus upload and download limits, not only parser/scanner behavior.
```

## Current Boundary

Implemented local controls:

```text
scan-first guarded download
rate-limited guarded download
safe attachment filename
download event audit trail
missing scan -> 409
rate limit -> 429
allowed clean download -> 200
```

Still not implemented:

```text
authenticated user model
session boundary
tenant boundary
object ownership policy
RBAC
ABAC
ReBAC
signed URL support
production authorization middleware
production authorization tests
```

## Decision

Do not implement production authorization yet.

Marker:

```text
do not implement production authorization yet
```

Do not rename the current no-auth boundary as authorization.

Do not add a fake user/session abstraction just to make the portfolio sound stronger.

The next safe product gate should be a manual approval schema:

```text
uploaded raw file download approval schema v0
```

The planned table name is:

```text
raw_file_download_approvals
```

The purpose of `raw_file_download_approvals` is to make future guarded downloads require an inspectable human/operator approval record before bytes can leave quarantine.

This is not user identity.

`approved_by_label` is an operator-provided label, not authenticated user identity.

## Proposed Approval Record

Future schema fields:

```text
id
raw_file_id
latest_scan_result_id
approval_status
approval_reason
approved_by_label
expires_at
revoked_at
created_at
metadata_json
approval_boundary
identity_boundary
```

Suggested status values:

```text
approved
revoked
expired
```

Suggested boundaries:

```text
approval_boundary: local_v0_manual_operator_approval_not_production_auth
identity_boundary: operator_label_not_authenticated_identity
```

Future guarded download preconditions:

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

## Why This Gate

This gate keeps the product inspectable:

```text
download approval is visible as data
approval expiration is visible as data
approval revocation is visible as data
download audit events can later link to approval id
authorization claims remain bounded
```

It also prevents a common portfolio mistake:

```text
adding an auth-looking header check and calling it production authorization
```

That would not satisfy object-level authorization because there is no authenticated principal, ownership policy, or tenant relationship to evaluate.

## Acceptance For Next Gate

The next implementation gate may add schema only if:

```text
raw_file_download_approvals is documented as local manual approval, not production auth
approved_by_label is documented as operator-provided label, not authenticated user identity
download route behavior is not changed in the schema gate
download audit behavior is not changed in the schema gate
production authorization remains unclaimed
tests check the boundary strings
```

## Boundary

This is a review-only decision.

This is not endpoint code.

This is not schema.

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
selected next gate: uploaded raw file download approval schema v0
```
