# Failure-case draft persistence handoff review

## Status

Accepted.

This is a review-only gate.

## Question

Phase 61 added `POST /failure-cases/draft-preview`, and Phase 63 verified that it returns a non-persisting draft payload while leaving `failure_cases` unchanged.

The next question is:

```text
Should NoiseProof automatically persist draft-preview output, add a confirm endpoint, or first prove a manual handoff from draft preview to the existing failure-case persistence API?
```

## Current evidence

Implemented evidence:

- `POST /failure-cases/draft-preview` returns a `draft` shaped like `FailureCaseCreate`
- `persistence_boundary` returns `preview_only_not_persisted`
- `human_confirmation_required` returns `true`
- route-level smoke confirms `failure_cases` remain unchanged after preview
- `POST /failure-cases` already persists manually submitted failure records
- `docs/review/failure-case-persistence-smoke-verification.md` verifies manual failure persistence on a fresh migrated Docker DB

## Decision

Do not add automatic persistence in this review gate.

Do not add a confirm endpoint in this review gate.

The next bounded proof should be a manual handoff smoke:

```text
POST /failure-cases/draft-preview
  -> inspect response.draft
  -> POST /failure-cases with that draft payload
  -> GET /failure-cases
  -> confirm the persisted row matches the human-confirmed draft
```

This preserves the human confirmation boundary while proving that the preview output can become a real failure-case record through the existing persistence API.

## Alternatives considered

### Automatically persist every draft preview

Rejected for now.

This would imply automatic failure detection and failure-case creation. The project has not proved that workflow failure evidence is always specific enough to create a durable incident record without human review.

### Add `POST /failure-cases/confirm-draft`

Rejected for now.

A confirm endpoint may become useful later, but adding it before a manual handoff smoke would create a new API surface without proving that the existing two-step boundary is insufficient.

### Add `workflow_run_id` to `failure_cases`

Rejected for now.

The previous linkage reviews already deferred this. A manually confirmed draft can still be persisted through `agent_run_id` or descriptive fields until workflow-level failure-case causality is stronger.

### Prove manual handoff with existing endpoints

Accepted.

This is the smallest honest next step because it uses existing endpoints, keeps human confirmation visible, and avoids stronger automation claims.

## Required next smoke

The next smoke should verify:

- draft preview returns `draft.fix_status = draft`
- the smoke runner treats the draft as requiring human confirmation
- the draft can be submitted to `POST /failure-cases`
- the persisted row is returned by `GET /failure-cases`
- `fix_status` may remain `draft` or be manually changed to `open`, but the change must be explicit in the smoke

## Claim boundary

Allowed claim after this review:

```text
NoiseProof has selected a manual draft-to-persistence handoff as the next proof step before adding automation.
```

Forbidden claims:

```text
This is not automatic failure detection.
This is not automatic failure-case persistence.
This does not add a confirm endpoint.
This does not add workflow_run_id to failure_cases.
This does not prove complete workflow failure causality.
```

## Next bounded gate

The next bounded gate should be:

```text
failure-case draft manual handoff smoke verification v0
```

That gate should prove the existing draft-preview output can be manually submitted to the existing failure-case persistence endpoint without adding a new endpoint or automatic persistence.
