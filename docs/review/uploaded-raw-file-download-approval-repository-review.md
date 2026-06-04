# Uploaded Raw File Download Approval Repository Review

Status: review-only.

Phase marker: uploaded raw file download approval repository review v0.

## Purpose

This gate selects the smallest repository boundary after `raw_file_download_approvals` was added and verified in the local Docker DB.

It does not add repository code.

It does not add endpoint code.

It does not change download route behavior.

It does not implement production authorization.

It does not create user identity.

It does not add signed URL support.

It does not add RBAC, ABAC, or ReBAC.

## Current State

NoiseProof has:

```text
uploaded_raw_files
raw_file_scan_results
raw_file_download_events
raw_file_download_approvals
db/migrations/021_raw_file_download_approvals.sql
docs/review/uploaded-raw-file-download-approval-schema-runtime-verification.md
```

`raw_file_download_approvals` is a local manual approval table.

`approved_by_label` is an operator-provided label, not authenticated user identity.

The download endpoint still only checks latest clean scan evidence and local rate-limit state.

The approval table is not yet used by the download route.

## Decision

Add repository code next, but keep it persistence-only.

The selected boundary is:

```text
RawFileDownloadApprovalCreate
RawFileDownloadApprovalOut
create_raw_file_download_approval
list_raw_file_download_approvals
```

`create_raw_file_download_approval` should insert a caller-provided manual approval row for an existing raw file and latest scan result.

`list_raw_file_download_approvals` should support operator inspection by:

```text
raw_file_id
approval_status
limit
```

The repository must not decide whether a download should be allowed.

The repository must not infer identity from `approved_by_label`.

The repository must not turn local manual approval into production authorization.

## Required Create Fields

`RawFileDownloadApprovalCreate` should accept:

```text
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
```

The repository should preserve database defaults unless the caller explicitly passes reviewed values:

```text
approval_status = approved
metadata_json = {}
approval_boundary = local_v0_manual_operator_approval_not_production_auth
identity_boundary = operator_label_not_authenticated_identity
```

## Read Boundary

`list_raw_file_download_approvals` should read from:

```text
raw_file_download_approvals
```

It may join or validate against:

```text
uploaded_raw_files
raw_file_scan_results
```

only to ensure parent rows exist or to support later operator inspection.

It should return approval metadata, boundary strings, expiry, and revocation fields.

It must not return raw uploaded bytes.

It must not return a signed URL.

## Deferred Helper

A later gate may add a helper to find an active unexpired approval for a raw file.

That helper is intentionally not selected for the first repository code gate because it would start moving from persistence into authorization behavior.

The first code gate should prove only that local approval rows can be created and inspected.

## Guardrails

do not add endpoint code in this gate.

do not change the download route in this gate.

do not enforce approvals in this gate.

The future repository implementation must not:

- allow downloads
- create signed URLs
- create sessions
- verify JWTs
- infer authenticated users
- add RBAC
- add ABAC
- add ReBAC
- call LLMs
- call scanners
- inspect raw file bytes
- generate Evidence Ledger rows
- create automatic failure cases

## Selected Next Gate

```text
selected next gate: uploaded raw file download approval repository v0
```

That gate may add schema models and repository methods for caller-provided approval rows, but it should not add endpoint code, download route behavior, production authorization, user identity, signed URL support, RBAC, ABAC, ReBAC, hosted deployment evidence, or external reviewer feedback.

## Explicit Non-claims

This is review-only.

This is not repository code.

This is not endpoint code.

This is not download route behavior.

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

This review adds no repository code, endpoint code, download route behavior, authorization enforcement, authenticated identity, signed URL support, RBAC, ABAC, ReBAC, hosted deployment evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete claim.
