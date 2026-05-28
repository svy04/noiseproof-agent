# ADR 005: Why Human Approval

## Status

Accepted

## Context

NoiseProof Agent operates in a domain where source ambiguity, contradictions, and unsupported claims matter. Fully autonomous final conclusions would be the wrong signal for the portfolio. The project should show that the system knows where to stop.

Human approval is not a cosmetic safety layer. It is part of the product thesis: unsupported answers should not pass.

## Decision

Keep humans responsible for accepting final interpretations.

The system should:

- produce evidence-led reports
- surface contradictions
- mark weak and unsupported claims
- refuse trading-advice drift
- show missing data
- record failure cases

The system should not silently convert weak evidence into strong conclusions.

## Alternatives considered

1. Fully autonomous report publishing
   - Faster demo, but hides approval boundaries and increases risk of unsupported claims.
2. Manual-only analyst workflow
   - Safe, but does not prove agent workflow design or service implementation.
3. Human approval only after final report
   - Too late because unsupported claims should be blocked before final report generation.

## Consequences

- The Critic / Noise Gate becomes a required stage.
- Reports need confidence, limitations, and next-data-needed fields.
- The operations dashboard should show blocked and failed runs.
- The project prioritizes inspectability over autonomy theater.

## What would change this decision

This decision would change if the system had strong enough evaluation results, domain review, compliance constraints, and production monitoring to justify narrower automated actions. That is not part of MVP.
