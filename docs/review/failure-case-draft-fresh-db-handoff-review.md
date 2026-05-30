# Failure-case draft fresh DB handoff review

## Status

Accepted.

This is a review-only gate.

## Question

Phase 66 proved the manual draft-to-persistence handoff with a route-level in-memory repository smoke.

The next question is:

```text
Is route-level smoke enough, or should the same handoff be verified against a fresh migrated Docker DB before stronger application claims?
```

## Current evidence

Implemented evidence:

- manual handoff route-level smoke exists
- `POST /failure-cases/draft-preview` returns a draft with `fix_status: draft`
- the test makes an explicit human confirmation step by changing `fix_status` to `open`
- `POST /failure-cases` persists that human-confirmed payload in the route-level test
- `GET /failure-cases` returns the persisted row

Missing evidence:

- the same handoff has not been run through a real FastAPI process against PostgreSQL
- the same handoff has not been verified on a fresh migrated Docker DB
- the same handoff has not been documented as local runtime smoke evidence

## Decision

The next bounded proof should verify the same handoff on a fresh migrated Docker DB.

Do not add automatic persistence in this review gate.

Do not add a confirm endpoint in this review gate.

Do not add `workflow_run_id` to `failure_cases` in this review gate.

## Required next smoke

The next smoke should use an isolated Compose project and a fresh database:

```text
docker compose -p noiseproof-agent-draft-handoff-smoke up -d db
python -m app.migration_runner
uvicorn app.main:app
POST /failure-cases/draft-preview
human-confirm draft.fix_status from draft to open
POST /failure-cases
GET /failure-cases
GET /ops/summary
docker compose -p noiseproof-agent-draft-handoff-smoke down -v
```

The smoke must record:

- database port
- API port
- migration status
- draft preview output boundary
- persisted failure row
- `/ops/summary.failure_case_count`
- cleanup command

## Alternatives considered

### Stop at route-level smoke

Rejected for now.

Route-level smoke is useful, but the project already has a proof pattern for fresh migrated Docker DB evidence. A reviewer will trust the handoff more if it passes through the real repository path.

### Add automatic persistence now

Rejected.

That would skip the human confirmation boundary and imply automatic failure-case creation.

### Add a confirm endpoint now

Rejected.

A confirm endpoint may eventually reduce manual copy/paste, but the current system can prove the handoff with existing endpoints first.

## Claim boundary

Allowed claim after this review:

```text
NoiseProof has selected fresh migrated Docker DB smoke as the next proof step for draft-to-persistence handoff.
```

Forbidden claims:

```text
This is not automatic failure detection.
This is not automatic failure-case persistence.
This is not hosted deployment evidence.
This does not add a confirm endpoint.
This does not add workflow_run_id to failure_cases.
This does not prove complete workflow failure causality.
```

## Next bounded gate

The next bounded gate should be:

```text
failure-case draft fresh-db handoff smoke verification v0
```

That gate should run the manual draft handoff through a local fresh migrated Docker DB and record the evidence without claiming hosted deployment or automatic persistence.
