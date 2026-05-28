# ADR 003: Why Evidence Ledger

## Status

Accepted

## Context

The core risk in messy market intelligence is not that the final answer is badly written. The risk is that unsupported claims pass as if they were supported.

The project needs a structured artifact between retrieval and final report generation.

## Decision

Create an Evidence Ledger before final answer generation.

Each planned entry records:

```text
claim
source_id
source_type
source_date
evidence_span
confidence
limitation
contradicting_source_ids
status
```

Allowed statuses:

```text
supported
weakly_supported
contradicted
unsupported
blocked
```

## Alternatives considered

1. Inline citations only
   - Useful but too weak because citations do not record limitations, contradiction state, or blocked claims.
2. Final report with a source list
   - Easy to read, but hides which claim each source supports.
3. Free-form critic notes
   - Flexible, but hard to query, evaluate, or display in an operations dashboard.

## Consequences

- Claims become reviewable before the final report.
- Unsupported and contradicted claims can be blocked or downgraded.
- The dashboard can count unsupported claims and contradictions.
- Implementation must maintain claim-level records, not only document-level metadata.

## What would change this decision

This decision would change if a simpler structured citation format could support claim status, confidence, limitations, contradictions, and dashboard aggregation without a separate ledger concept.
