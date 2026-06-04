# Uploaded Raw File Download Approval Gate Behavior Review

Status: review-only.

Phase marker: uploaded raw file download approval gate behavior review v0.

## Purpose

Decide the next smallest gate after local approval metadata create/list runtime proof.

The question is whether NoiseProof should change guarded raw file download behavior immediately.

Decision: do not change route behavior yet.

Add an active approval helper first.

## Primary Sources

- OWASP Authorization Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
- OWASP API1:2023 Broken Object Level Authorization: https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/
- OWASP API5:2023 Broken Function Level Authorization: https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/
- OWASP File Upload Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

Source-first interpretation for this local v0 project:

- authorization-sensitive behavior should deny by default
- access decisions should be checked at the point of use
- object-level checks matter for per-file download paths
- function-level checks matter for approval creation and download behavior
- uploaded file download paths should remain protected, logged, and bounded

## Current State

NoiseProof currently has:

```text
latest clean scan guard on GET /documents/upload-raw-files/{raw_file_id}/download
raw_file_download_events audit rows
raw_file_download_approvals local manual approval rows
metadata-only approval create/list endpoints
local runtime smoke proving approval metadata does not bypass scan guard
```

The current download guard is:

```text
latest clean scan result required before raw file download
```

This is still useful, but approval metadata is not yet consulted by the download route.

## Design Decision

The eventual approval gate should require:

```text
latest clean scan and active approval
```

However, the next code gate should not be route enforcement yet.

The next code gate should add a repository helper:

```text
find_active_raw_file_download_approval
```

The helper should return one active approval for:

```text
raw_file_id
latest_scan_result_id
approval_status = approved
expires_at > now
revoked_at IS NULL
```

This keeps the rule inspectable before it affects raw bytes.

## Future Route Behavior

A later guarded download behavior gate may change the raw download route from:

```text
latest clean scan required
```

to:

```text
latest clean scan and active approval required
```

Expected future block reasons:

```text
missing_clean_scan
missing_download_approval
revoked_or_expired_download_approval
rate_limited
```

Allowed future downloads should record:

```text
download_approval_id in metadata_json
approval_boundary
identity_boundary
```

Use `metadata_json` first rather than adding another migration immediately.

If later inspection needs first-class queries by approval id, a future schema gate can add a typed `download_approval_id` column to `raw_file_download_events`.

## Why Helper Before Route Enforcement

Route enforcement is where mistakes become user-visible.

The helper can be tested without serving raw bytes.

It also makes the future route change easier to inspect:

```text
download route calls helper
helper returns active approval or None
None means deny
```

That shape follows deny by default without pretending to have production authorization.

## Selected Next Gate

```text
selected next gate: uploaded raw file download approval helper v0
```

That gate may add repository/helper code and tests for active approval lookup.

It should not change the download route.

It should not add endpoint behavior.

It should not claim production authorization, authenticated user identity, signed URL support, RBAC, ABAC, ReBAC, hosted deployment evidence, or external reviewer feedback.

## Explicit Non-claims

This is review-only.

This is not route behavior.

This is not approval enforcement.

This is not production authorization.

This is not user identity.

This is not signed URL support.

This is not RBAC.

This is not ABAC.

This is not ReBAC.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.

## Boundary

This review adds no route behavior, approval enforcement, endpoint behavior, authenticated identity, signed URL support, RBAC, ABAC, ReBAC, hosted deployment evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete claim.
