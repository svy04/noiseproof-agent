# Workflow lineage boundary hardening review

Status: Phase 34.5 review-only gate.

This review decides what should be hardened after the derived lineage read model proved that missing `stage_input_manifest` references can be surfaced.

## Current evidence

Phase 32 added:

```text
GET /workflow-runs/{id}/lineage
```

Phase 34 added a targeted missing-reference fixture proving the read model can return:

- `missing_reference_count > 0`
- `missing_evidence_entry_ids`
- `missing_noise_gate_record_id`
- missing-reference warning text

That covers missing local ids. It does not cover malformed manifest shapes.

## Boundary risks to harden next

### Non-list manifest values

The most important next risk is `input_evidence_ledger_entry_ids`.

The deterministic workflow writes this field as a list. But if a stored manifest is malformed, non-list manifest values should be treated as invalid manifest shape, not as a valid evidence id list.

In particular:

```text
string values must not be treated as iterable evidence id lists
```

Without a hardening test, a string value could be accidentally interpreted character by character by list-like code. That would inflate missing reference counts and make the warning less useful.

### Duplicate references

Duplicate references are not currently a schema risk, but they are a read-model clarity risk.

The next implementation should decide whether duplicate references should:

- preserve manifest order and count every reference
- be deduplicated for resolved record display
- be reported as a warning

The safest next step is only to document and test current intended behavior. Do not add schema for duplicates.

### Cross-workflow references

The derived read model resolves references only against child records attached to the current `workflow_run_id`.

That means a manifest id that exists elsewhere but not inside the current workflow should still be reported as missing for this local workflow. This is correct for local deterministic workflow lineage.

Do not broaden lookup scope across all persisted records unless a later review proves that global provenance lookup is needed.

## Decision

Do not add schema or runtime mutation surfaces in this gate.

Specifically:

- no migrations
- no columns
- no join tables
- no direct evidence -> gate -> report foreign keys
- no malformed-manifest mutation endpoint
- no repair endpoint
- no dashboard polish
- no LLM calls
- no embeddings or retrieval changes

The next implementation should be a small route/helper test plus a narrow parser hardening change if the current helper treats non-list values incorrectly.

## Recommended next gate

```text
Workflow lineage manifest-shape hardening v0
```

Acceptance criteria:

- non-list `input_evidence_ledger_entry_ids` values are not treated as iterable evidence id lists
- malformed manifest shape produces a structured warning or empty id list
- duplicate references behavior is explicitly tested or documented
- cross-workflow references remain missing in the local workflow lineage response
- no migrations
- no columns
- no join tables
- no mutation endpoint
- no repair endpoint

## Claim boundary

Allowed claim:

```text
NoiseProof has reviewed the next lineage hardening risk and selected manifest-shape validation as the next narrow proof step.
```

Forbidden claim:

```text
NoiseProof has production-grade lineage repair, strict relational provenance, or globally normalized evidence-to-gate/report lineage.
```

