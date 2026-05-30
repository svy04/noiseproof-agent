# Evidence-to-gate/report local cross-links review

Status: Phase 22.5 review-only gate.

This is a review-only gate. It decides whether persisted Evidence Ledger rows should be directly cross-linked to persisted Noise Gate and Report rows before adding any migration, endpoint, dashboard behavior, or schema claim.

## Current State

NoiseProof now persists these local records:

- Evidence Ledger entries
- Noise Gate records
- Report Preview records
- parent `agent_runs`

Each persisted evidence, gate, and report record has:

- `workflow_trace_id` for local trace grouping
- `agent_run_id` for parent run provenance

The dashboard exposes:

- Evidence Ledger rows
- Noise Gate rows
- Report rows
- trace lookup links
- parent run links
- status / decision filters

This makes each record inspectable, but it does not prove that a specific Noise Gate record consumed a specific persisted Evidence Ledger row, or that a specific Report record was generated from a specific persisted Noise Gate row.

## Decision

Do not add cross-link columns in this review gate.

Adding direct columns such as `noise_gate_record.evidence_ledger_entry_ids`, `report_record.noise_gate_record_id`, or `report_record.evidence_ledger_entry_ids` now would create a false sense of causal lineage.

The current endpoints are deterministic preview/persistence boundaries. A caller can submit the same evidence-shaped payload to `/noise-gates` or `/reports` without first persisting an Evidence Ledger row. That means a direct foreign-key cross-link would often be absent, synthetic, or misleading unless the runtime first introduces a single workflow parent that owns the full evidence -> gate -> report sequence.

The correct next implementation should either:

- keep the current local trace grouping and parent run provenance as honest inspectability, or
- introduce an explicit workflow-level orchestration record before cross-linking child records across stages.

## Alternatives Considered

### Add `noise_gate_record.evidence_ledger_entry_ids`

Rejected for this gate.

Noise Gate payloads currently receive evidence-shaped entries, not persisted Evidence Ledger row ids. Backfilling ids from matching text, claim, source, and status would be brittle and would imply stronger lineage than the service has actually recorded.

### Add `report_record.noise_gate_record_id`

Rejected for this gate.

Report persistence currently runs the deterministic gate logic inside the report operation. It does not persist or reuse a separate Noise Gate record as an upstream parent. A nullable link would look more mature than the actual runtime.

### Infer links by `workflow_trace_id`

Rejected as a causal claim.

`workflow_trace_id` is valuable for local grouping, but separate `/evidence-ledgers`, `/noise-gates`, and `/reports` calls each create their own trace id. Matching by trace id only proves local trace membership, not evidence -> gate -> report causality.

### Use `agent_run_id` as the cross-stage link

Rejected as a cross-stage claim.

`agent_run_id` currently identifies the parent run for one endpoint invocation. It does not yet represent a multi-stage workflow parent. Treating it as a cross-stage chain would create a false sense of causal lineage.

### Introduce a single workflow parent

Accepted as the likely future direction, but deferred.

A single workflow parent would let the service run evidence, gate, and report stages under one orchestrated id. Only then can the repo honestly add child-stage links such as:

- workflow run -> evidence ledger entries
- workflow run -> noise gate record
- workflow run -> report record
- report record -> gate record
- gate record -> evidence ledger entries

This is larger than the current review gate.

## Future Acceptance Criteria

Cross-stage links should be added only when:

- the runtime has a single workflow parent for evidence -> gate -> report execution
- persisted Evidence Ledger rows are created before a persisted Noise Gate consumes them
- persisted Noise Gate rows are created before a persisted Report consumes them
- child records store non-null ids for their actual upstream records
- tests prove the links are created from runtime execution order, not inferred by matching text
- the dashboard shows cross-links as local workflow provenance, not distributed tracing
- runtime smoke proves the links against PostgreSQL

## Boundary

This review does not add migrations.
It does not add columns.
It does not add endpoints.
It does not change dashboard behavior.
It does not claim full workflow orchestration, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, or final report generation.

The current honest claim remains:

```text
Persisted evidence, gate, and report records are locally inspectable through workflow_trace_id and parent agent_run_id. Direct evidence -> gate -> report cross-links are not implemented yet because the service does not yet have a single workflow parent that owns all three stages.
```

## Follow-up status after Phase 30.5

Phase 30 added a workflow parent detail endpoint, and Phase 30.5 reviewed direct evidence -> gate -> report links again.

The newer review keeps direct foreign-key links deferred. A workflow parent now proves common workflow membership, but downstream stages still consume evidence-shaped values rather than persisted upstream row ids.

See:

```text
docs/review/direct-evidence-gate-report-cross-link-review.md
```
