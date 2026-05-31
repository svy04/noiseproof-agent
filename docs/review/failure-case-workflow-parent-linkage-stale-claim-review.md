# Failure-case Workflow Parent Linkage Stale-claim Review

Status: review-only gate.

Phase marker: failure-case workflow parent linkage proof chain stale-claim review v0.

Label: Failure-case workflow parent linkage stale-claim review.

This review checks whether older application-facing wording still says workflow parent linkage is deferred after Phase 76+ made manual workflow parent linkage real.

## Current State

Manual `failure_cases.workflow_run_id` now exists.

It is verified by:

- schema and API support
- route-level create/list smoke
- local fresh migrated Docker DB persistence smoke
- dashboard surfacing
- local fresh migrated Docker DB dashboard smoke
- proof index

## Stale Claim Candidates

stale claim candidates:

- "failure cases are not linked to workflow parents yet"
- "workflow_run_id remains deferred"
- "workflow_run_id on failure_cases remains deferred"

These older statements were true before the manual-linkage path existed. They are now stale if they appear as current application-facing claims.

They are still acceptable only when framed as historical review notes.

## Decision

Clean up stale application-facing wording next.

The cleanup should:

- keep automatic failure-case creation unclaimed
- keep complete workflow failure causality unclaimed
- preserve historical review artifacts
- update current-facing docs so they say manual workflow parent linkage exists
- keep the proof index as the first reader path

## Boundary

Do not rewrite application-facing claims in this review gate.

This review adds no runtime behavior, schema, migration, API endpoint, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure detection, automatic failure-case creation, automatic persistence from workflow failures, complete workflow failure causality, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

This is not hosted deployment evidence.
This is not automatic failure-case creation.
This is not complete workflow failure causality.

## Next Gate

```text
failure-case workflow parent linkage stale-claim cleanup v0
```
