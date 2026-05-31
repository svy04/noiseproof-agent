# Failure-case workflow creation path decision

## Status

Accepted.

This is a decision-only gate. It adds no runtime behavior.

## Question

Now that a failed deterministic workflow parent can feed `POST /failure-cases/draft-preview`, should the system automatically create a persisted failure case from every failed workflow?

## Decision

No. automatic failure-case creation remains deferred.

The next safe path is a human-confirmed persistence path that can retain workflow parent context without pretending the system has reliable incident classification.

## Why

The current system can prove these narrower facts:

- a deterministic workflow parent can end in `failed`
- workflow failure metadata includes stage and error type
- that metadata can feed the draft-preview endpoint
- draft preview returns `preview_only_not_persisted`
- draft preview leaves `failure_cases` unchanged
- a separate manual handoff can persist a reviewer-confirmed failure case

Those facts do not prove that every workflow failure should become a durable failure-case record automatically.

## Creation path options considered

### Option A - Automatic creation inside workflow execution

Rejected for now.

It would create durable failure cases from operational exceptions without enough proof that the exception is a meaningful product failure, user-visible failure, data-quality failure, or workflow-causality failure.

### Option B - Keep preview-only forever

Rejected as the final shape.

Preview-only is safe, but eventually the project needs an inspectable path from failed workflow evidence to a durable failure-case record.

### Option C - Human-confirmed persistence path

Accepted as the next direction.

The system should continue to produce a draft first. A reviewer should confirm it before persistence. If the project wants workflow-level linkage, `workflow_run_id on failure_cases requires a schema gate` before implementation.

## Boundary

Allowed claim:

```text
NoiseProof can prepare a draft failure case from a failed workflow parent and should keep a human confirmation boundary before persistence.
```

Forbidden claims:

```text
NoiseProof automatically creates failure cases from workflow failures.
NoiseProof classifies all workflow failures correctly.
NoiseProof proves complete workflow failure causality.
NoiseProof has workflow_run_id on failure_cases.
```

## Next bounded gate

The next bounded gate should be:

```text
failure-case workflow parent linkage schema review v0
```

That review should decide whether to add nullable `workflow_run_id` to `failure_cases`, what migration would be needed, and how the API should avoid implying automatic creation.
