# Failure-case Workflow Review Queue Proof Index

Status: implemented index.

Phase marker: failure-case workflow review queue proof index v0.

Label: Failure-case workflow review queue proof index.

This proof index gives a compact reader path for the failure-case workflow review queue evidence.

It does not replace the source artifacts. It points to them and keeps the claim boundary visible.

## Reader Path

reader path keywords: read-model queue boundary, runtime queue smoke, dashboard surfacing review, plain dashboard surfacing, fresh DB dashboard proof.

1. Read-model queue boundary
   - Read: `docs/review/failure-case-workflow-review-queue.md`
   - Purpose: explains why failed, blocked, and needs-revision workflow parents can be surfaced for human failure-case review without creating `failure_cases`.

2. Runtime queue smoke
   - Read: `docs/review/failure-case-workflow-review-queue-runtime-smoke-verification.md`
   - Purpose: verifies the queue read model against a local fresh migrated Docker DB and FastAPI process with one pending workflow, one linked workflow, and one completed workflow excluded.

3. Dashboard surfacing review
   - Read: `docs/review/failure-case-workflow-review-queue-dashboard-surfacing-review.md`
   - Purpose: records the review-only decision for a compact dashboard section before changing dashboard rendering.

4. Plain dashboard surfacing
   - Read: `docs/review/failure-case-workflow-review-queue-dashboard-surfacing.md`
   - Purpose: documents that `GET /ops/dashboard` now renders the same read model as a `Failure-case Workflow Review Queue` section.

5. Fresh DB dashboard proof
   - Read: `docs/review/failure-case-workflow-review-queue-fresh-db-dashboard-smoke-verification.md`
   - Purpose: verifies that the dashboard section appears against a fresh local PostgreSQL database with migrations applied and does not create new `failure_cases`.

6. Application-facing boundary
   - Read: `docs/application/portfolio-index.md`
   - Purpose: shows the proof in reviewer-facing language without expanding the claim.

## Allowed Claim

Allowed claim:

```text
NoiseProof Agent can expose a read-model queue of failed workflow parents that need
human failure-case review, show linked manual failure cases when they exist, and
surface the same review queue in the plain operations dashboard on a local fresh
migrated PostgreSQL database.
```

## Forbidden Claim

Forbidden claim:

```text
NoiseProof Agent automatically creates failure cases from workflow failures,
automatically detects root causes, proves complete workflow failure causality,
or has hosted production deployment evidence.
```

## Boundary

This index adds no runtime behavior, schema, migration, API endpoint, dashboard rendering, smoke execution, hosted deployment evidence, external reviewer feedback, automatic failure detection, automatic failure-case creation, automatic persistence from workflow failures, root-cause automation, complete workflow failure causality, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

This is not hosted deployment evidence.
This is not external reviewer feedback.
This is not automatic failure-case creation.
This is not complete workflow failure causality.
