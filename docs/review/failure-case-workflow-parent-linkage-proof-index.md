# Failure-case Workflow Parent Linkage Proof Index

Status: implemented index.

Phase marker: failure-case workflow parent linkage proof index v0.

Label: Failure-case workflow parent linkage proof index.

This proof index gives a compact reader path for the manual failure-case workflow parent linkage evidence.

It does not replace the source artifacts. It points to them and keeps the claim boundary visible.

## Reader path

reader path keywords: schema boundary, manual persistence, fresh DB persistence, dashboard surfacing, fresh DB dashboard proof.

1. Schema boundary
   - Read: `docs/review/failure-case-workflow-parent-linkage-schema-review.md`
   - Purpose: explains why `failure_cases.workflow_run_id` should be a nullable manual provenance link.

2. Manual persistence
   - Read: `docs/review/failure-case-workflow-parent-linkage-smoke-verification.md`
   - Purpose: verifies route-level create/list retention of a manual `workflow_run_id` on `failure_cases`.

3. Fresh DB persistence
   - Read: `docs/review/failure-case-workflow-parent-linkage-fresh-db-verification.md`
   - Purpose: verifies the same manual link against a local fresh migrated Docker DB and PostgreSQL repository.

4. Dashboard surfacing
   - Read: `docs/review/failure-case-workflow-parent-linkage-dashboard-review.md`
   - Read: `docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-review.md`
   - Purpose: explains why the dashboard should surface the already persisted manual workflow parent link.

5. Fresh DB dashboard proof
   - Read: `docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-verification.md`
   - Purpose: verifies that `GET /ops/dashboard` shows the `Workflow Parent` link after a fresh DB migration, a real FastAPI process, a manual workflow run, and a manual workflow-linked failure case.

6. Application-facing boundary
   - Read: `docs/application/portfolio-index.md`
   - Read: `docs/application/braincrew-role-map.md`
   - Read: `docs/review/application-ready-review.md`
   - Purpose: shows the proof in reviewer-facing language without expanding the claim.

## Allowed claim

Allowed claim:

```text
NoiseProof Agent can manually persist a failure case with workflow parent provenance,
verify that linkage against a local fresh migrated PostgreSQL database, and surface
the existing manual link in the plain operations dashboard.
```

## Forbidden claim

Forbidden claim:

```text
NoiseProof Agent automatically creates failure cases from workflow failures,
proves complete workflow failure causality, or has hosted production deployment evidence.
```

## Boundary

This index adds no runtime behavior, schema, migration, API endpoint, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure detection, automatic failure-case creation, automatic persistence from workflow failures, complete workflow failure causality, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

This is not hosted deployment evidence.
This is not automatic failure-case creation.
This is not complete workflow failure causality.
