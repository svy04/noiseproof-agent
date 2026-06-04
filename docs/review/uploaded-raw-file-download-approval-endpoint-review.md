# Uploaded Raw File Download Approval Endpoint Review

Status: review-only.

Phase marker: uploaded raw file download approval endpoint review v0.

## Purpose

This gate selects the smallest metadata-only API boundary after approval repository persistence was added.

It does not add endpoint code.

It does not change download route behavior.

It does not enforce approvals.

It does not implement production authorization.

It does not create user identity.

It does not add signed URL support.

## Current State

NoiseProof has:

```text
raw_file_download_approvals
RawFileDownloadApprovalCreate
RawFileDownloadApprovalOut
create_raw_file_download_approval
list_raw_file_download_approvals
```

The repository can create and list caller-provided manual approval rows.

`approved_by_label` remains an operator-provided label, not authenticated user identity.

The guarded raw file download route still does not consult approval rows.

## Decision

Add endpoint code next, but keep it metadata-only.

The selected route boundary is:

```text
POST /documents/upload-raw-files/{raw_file_id}/download-approvals
GET /documents/upload-raw-files/{raw_file_id}/download-approvals
```

`POST /documents/upload-raw-files/{raw_file_id}/download-approvals` should accept `RawFileDownloadApprovalCreate` and call `create_raw_file_download_approval`.

`GET /documents/upload-raw-files/{raw_file_id}/download-approvals` should call `list_raw_file_download_approvals`.

Both routes should return `RawFileDownloadApprovalOut` data.

This is a metadata-only endpoint surface.

## Required Route Behavior

The future endpoint implementation should:

- reject path body raw_file_id mismatch
- persist caller-provided manual approval rows
- list approval rows for one raw file
- cap list limits with the repository default guard
- preserve `approval_boundary`
- preserve `identity_boundary`
- preserve `approved_by_label`

The endpoint should not:

- allow a download
- change the guarded download route
- create a signed URL
- infer authenticated identity
- verify JWTs
- create sessions
- enforce RBAC
- enforce ABAC
- enforce ReBAC
- claim production authorization

## Deferred Checks

The metadata endpoint may receive `latest_scan_result_id`, but it should not claim it has proven latest clean scan enforcement.

The later approval gate behavior review must decide whether approval enforcement should check:

```text
latest scan result exists
latest scan result is completed
latest scan result is clean
approval is unexpired
approval is not revoked
download audit event links approval id
```

Those are intentionally not part of this endpoint review.

## Selected Next Gate

```text
selected next gate: uploaded raw file download approval endpoint v0
```

That gate may add metadata-only create/list routes and route tests, but it should not change guarded raw download behavior, enforce approvals, implement production authorization, infer authenticated identity, add signed URL support, add RBAC, ABAC, or ReBAC, claim hosted deployment evidence, or claim external reviewer feedback.

## Explicit Non-claims

This is review-only.

This is not endpoint code.

This is not download route behavior.

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

This review adds no endpoint code, download route behavior, authorization enforcement, authenticated identity, signed URL support, RBAC, ABAC, ReBAC, hosted deployment evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete claim.
