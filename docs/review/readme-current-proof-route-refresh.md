# README Current Proof Route Refresh

Status: implemented.

Phase marker: readme current proof route refresh v0.

## Purpose

Keep the first-screen README proof route aligned with the current reviewer issue body and latest high-signal local proof.

The README top fast path previously still named an older persisted Report markdown export proof as the latest route, while issue #1 and the newer application-facing markers point reviewers to the workflow failure auto-created dashboard runtime proof.

## Current Route

The top README fast path now points to:

```text
workflow failure auto-created dashboard runtime proof
docs/review/workflow-failure-auto-created-failure-case-dashboard-runtime-smoke.md
docs/review/external-reviewer-workflow-failure-auto-created-dashboard-runtime-request-refresh.md
docs/review/external-review-issue-body-workflow-failure-auto-created-dashboard-runtime-refresh.md
```

## Preserved State

The external feedback state remains pending:

```text
candidate_count=0
draft_count=0
self_authored_comment
external reviewer feedback remains pending
```

## Boundary

This is README route clarity only.

It is not a new runtime smoke.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not retry behavior.

It is not root-cause automation.

It is not complete workflow failure causality.

It is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
