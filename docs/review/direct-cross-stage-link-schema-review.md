# Direct cross-stage link schema review

Status: Phase 31.5 review-only gate. Follow-up implemented in Phase 32.

This review asks whether Phase 31's `stage_input_manifest` is enough evidence to add direct evidence -> gate -> report foreign-key links or join tables.

## Current State

Phase 31 added local stage input manifests to deterministic workflow-created records:

- `noise_gate_records.stage_input_manifest`
- `report_records.stage_input_manifest`

The deterministic workflow now creates persisted Evidence Ledger rows first, converts those persisted rows back into preview-shaped evidence entries, then records the persisted Evidence Ledger row ids in the Noise Gate manifest.

The Report stage records the same persisted Evidence Ledger row ids plus the persisted Noise Gate record id.

This is a meaningful improvement:

```text
workflow_run
  -> persisted Evidence Ledger rows
  -> Noise Gate record with stage_input_manifest.input_evidence_ledger_entry_ids
  -> Report record with stage_input_manifest.input_evidence_ledger_entry_ids
  -> Report record with stage_input_manifest.input_noise_gate_record_id
```

JSON manifest is enough for local deterministic stage input provenance.

It shows which persisted upstream ids were handed to downstream deterministic preview stages.

## Decision

Do not add direct evidence -> gate -> report foreign-key links yet.

Do not add join tables yet.

The project should keep Phase 31's manifest as the current source of local stage input provenance and add a derived read model before changing relational schema again.

## Why The Manifest Is Not Yet A Relational Contract

The manifest is useful, but it is not enough for strict relational lineage.

It does not yet prove:

- every persisted Noise Gate row can only be created from persisted Evidence Ledger row ids
- every persisted Report row can only be created from a persisted Noise Gate row id
- standalone `/noise-gates` and `/reports` calls obey the same manifest contract
- downstream stage inputs are normalized enough for referential integrity
- deletions or backfills would preserve cross-stage integrity
- the project needs query-time joins more than a read-only lineage projection

Adding relational links now would make a stronger claim than the current runtime boundary supports.

## Alternatives Considered

### Add direct JSON columns for evidence and gate ids

Rejected as redundant.

Phase 31 already stores this data in `stage_input_manifest`. Adding parallel columns would split the source of truth before there is a proven query need.

### Add join tables

Rejected for now.

Join tables such as `noise_gate_evidence_entries` and `report_evidence_entries` would imply stronger lifecycle and referential guarantees than the service currently offers, especially because standalone gate/report endpoints can still receive payload-shaped inputs.

### Treat `stage_input_manifest` as the final lineage surface

Rejected as final wording.

The manifest is a good local provenance surface for the deterministic preview, but it is still JSON. It should be easy to inspect before the project decides whether normalized schema is worth the added weight.

### Add a derived lineage read model

Accepted as the next safest implementation.

The next implementation should derive a lineage-shaped response from existing persisted records and manifests without adding new storage:

```text
workflow_run
  evidence_entries[]
  noise_gate_records[]
    input_evidence_ledger_entry_ids[]
  report_records[]
    input_evidence_ledger_entry_ids[]
    input_noise_gate_record_id
  warnings[]
```

This would make the manifest easier to inspect while keeping schema claims conservative.

## Acceptance Criteria For Schema Links Later

Direct foreign-key links or join tables become justified only when:

- deterministic workflow execution is the primary path for report generation
- standalone gate/report persistence either records equivalent manifests or is explicitly marked as payload-only
- tests prove downstream persisted rows cannot claim upstream ids that were not actually passed in
- the dashboard or API has shown a stable need for query-time joins over derived lineage projection
- deletion and backfill behavior is specified
- docs can truthfully distinguish local relational lineage from distributed tracing

## Boundary

This review does not add migrations.
It does not add columns.
It does not add join tables.
It does not add endpoints.
It does not change runtime behavior.
It does not claim distributed tracing.
It does not claim autonomous workflow execution.

The current honest claim is:

```text
NoiseProof has deterministic workflow-created gate and report records with local stage input manifests. Those manifests expose persisted upstream ids consumed by preview stages. Direct evidence -> gate -> report foreign-key lineage is still not implemented.
```

## Next Gate

Recommended next implementation:

```text
Workflow lineage read model v0
```

That gate should expose a derived lineage view from existing workflow child records and `stage_input_manifest` values without changing storage.

## Phase 32 Follow-up

Phase 32 implemented the recommended read model:

```text
GET /workflow-runs/{id}/lineage
```

It derives lineage from existing workflow child records and `stage_input_manifest` values, resolves referenced Evidence Ledger and Noise Gate ids where possible, and surfaces missing manifest references as warnings.

Direct evidence -> gate -> report foreign-key links and join tables remain unimplemented.

## Phase 33 Follow-up

Phase 33 made the derived read model discoverable from the plain operations dashboard by adding workflow-row links to:

```text
GET /workflow-runs/{id}
GET /workflow-runs/{id}/lineage
```

This is a navigation improvement only. It does not add dashboard polish, new lineage storage, direct evidence -> gate -> report foreign-key links, or join tables.
