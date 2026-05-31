# Failure-case Workflow Parent Linkage Stale-claim Cleanup

Status: application-facing cleanup.

Phase marker: failure-case workflow parent linkage stale-claim cleanup v0.

Label: Failure-case workflow parent linkage stale-claim cleanup.

This cleanup updates current-facing application documents after the stale-claim review identified older wording that still described manual workflow parent linkage as deferred.

## Cleanup Scope

Updated current-facing wording in:

- `docs/application/braincrew-role-map.md`
- `docs/review/application-ready-review.md`

The cleanup says manual workflow parent linkage now exists while keeping the older review artifacts as historical context.

## Updated Current Claim

manual workflow parent linkage now exists.

A manually persisted `failure_cases` row can carry nullable `workflow_run_id` provenance to a `workflow_runs` parent. That path is schema-supported, route-smoke verified, fresh-DB verified, and surfaced in the plain operations dashboard through the proof index.

## Preserved Historical Context

historical review artifacts are preserved.

The earlier failure-case workflow linkage review was correct when it was written. It is now historical context for why schema linkage was deferred before the manual linkage gate existed.

## Boundary

This cleanup adds no runtime behavior, schema, migration, API endpoint, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure detection, automatic failure-case creation, automatic persistence from workflow failures, complete workflow failure causality, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

This is not automatic failure-case creation.
This is not complete workflow failure causality.
This is not hosted deployment evidence.

## Next Gate

```text
external-reader proof path review v0
```
