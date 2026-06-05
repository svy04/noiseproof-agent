# External Review Issue Body Embedding Provider Owner-runtime Smoke Packet Refresh

Status: live issue body refresh completed.

Phase marker: external review issue body embedding provider owner-runtime smoke packet refresh v0.

## Purpose

Record the owner-authored issue #1 body update that points reviewers to the embedding provider owner-runtime smoke packet and its request-refresh record.

This keeps external reviewer feedback v0 pending.

It does not accept feedback.

It does not close the external feedback gate.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Latest Packet

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md
```

## Reviewer Request Refresh

```text
docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-packet-request-refresh.md
```

## Issue-body Refresh Record

```text
docs/review/external-review-issue-body-embedding-provider-owner-runtime-smoke-packet-refresh.md
```

## Observed Issue State

Observed through `gh issue view 1 --repo svy04/noiseproof-agent --json body,updatedAt,comments` after editing the issue body and cleaning the leading BOM with a UTF-8 no-BOM body file.

```json
{
  "updatedAt": "2026-06-05T00:15:12Z",
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_embedding_provider_owner_runtime_smoke_packet": true,
  "has_embedding_provider_request_refresh": true,
  "has_embedding_provider_issue_body_refresh": true,
  "has_api_calls_attempted_false": true,
  "has_openai_api_key_printed_false": true,
  "has_live_embedding_generation_boundary": true,
  "has_external_feedback_boundary": true,
  "comment_count": 1,
  "body_length": 4734
}
```

## Issue Body Highlights

The issue body now asks reviewers to inspect:

```text
Embedding provider owner-runtime smoke packet
Embedding provider request refresh
Issue-body refresh record
Related opt-in wiring boundary
```

It highlights:

```text
route: POST /chunks/embedding-model-preview
packet_status: ready_for_owner_input
required_input: owner-provided OPENAI_API_KEY via environment outside the repository
api_calls_attempted: false
openai_api_key_printed: false
secret_committed_to_repo: false
secret_logged: false
future success criterion: embedding_status owner_runtime_provider_generated
future success criterion: provider_response_dimension_check passed
future success criterion: persistence_boundary preview_only_not_persisted
```

## Boundary

This is an owner-authored live issue body edit only.

It is not external reviewer feedback.

It is not a live issue body edit by an outside reviewer.

It is not live issue body edit by an outside reviewer.

It is not hosted deployment evidence.

It is not live embedding generation proof.

It is not semantic retrieval quality evidence.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

Self-authored issue edits or comments do not close the external reviewer feedback v0 gate.

## Next Gate

```text
external feedback current-state embedding provider owner-runtime smoke packet issue verification v0, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from docs/GOAL.md
```
