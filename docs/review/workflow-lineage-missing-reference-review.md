# Workflow lineage missing-reference review

Status: Phase 33.5 review-only gate.

This review checks whether the existing workflow lineage read model has a bounded way to describe missing `stage_input_manifest` references before adding any new runtime behavior.

## Current behavior

`GET /workflow-runs/{id}/lineage` is a derived read model over existing workflow child records and `stage_input_manifest` values.

It already attempts to resolve:

- Noise Gate input Evidence Ledger ids
- Report input Evidence Ledger ids
- Report input Noise Gate record id

If a manifest id cannot be resolved against the workflow child records, the response can expose:

- `missing_evidence_entry_ids`
- `missing_noise_gate_record_id`
- `missing_reference_count`
- warning text: `One or more stage_input_manifest references could not be resolved.`

This is enough for a bounded read model to say "a manifest points at something that is not present in the local workflow child records." It is not enough to claim strict relational lineage.

## Important caveat

The normal deterministic workflow path currently creates valid local references. There is no public API path whose purpose is to create malformed manifests.

That is good. The project should not add a production-like mutation surface just to manufacture corrupt lineage examples.

## Decision

Do not add runtime behavior in this gate.

Specifically:

- no migrations
- no columns
- no join tables
- no new foreign-key lineage
- do not add runtime mutation path for malformed manifests
- do not add a repair endpoint
- do not add dashboard polish
- do not call LLMs
- do not add embeddings or retrieval changes

This review only records what is already true and defines the smallest next proof step.

## Alternatives considered

### Add direct foreign-key columns now

Rejected. Direct evidence -> gate -> report columns would imply stronger lineage than the current deterministic preview needs.

### Add join tables now

Rejected. Join tables should wait until the project has repeated query-time need that cannot be handled by the derived read model.

### Add an API endpoint for malformed manifests

Rejected. A runtime endpoint that creates corrupt lineage would make the service surface stranger and less trustworthy.

### Add a targeted missing-reference test

Accepted as the next implementation direction. A targeted missing-reference test can prove the read model reports broken manifest references without expanding the public mutation surface.

## Recommended next gate

The next small implementation should be:

```text
Workflow lineage missing-reference test v0
```

It should create a targeted fixture that proves `GET /workflow-runs/{id}/lineage` can return `missing_reference_count > 0` when existing stored records contain a broken `stage_input_manifest`.

Preferred options:

- unit-level route/helper test that inserts a deliberately broken row through the in-memory test repository
- direct SQL fixture in a Docker smoke run if DB-level confidence is needed later

Rejected option:

- a new public API endpoint for creating malformed manifests

## Acceptance criteria for the next gate

The next gate should show:

- a lineage response with `missing_reference_count > 0`
- `missing_evidence_entry_ids` or `missing_noise_gate_record_id` populated
- warning text appears in the response
- no migrations
- no columns
- no join tables
- no runtime mutation path added
- no Evidence Ledger, Critic, report, dashboard, retrieval, embedding, or LLM scope expansion

## Claim boundary

Allowed claim:

```text
NoiseProof has reviewed the missing-reference boundary for the derived workflow lineage read model and selected a targeted test as the next proof step.
```

Forbidden claim:

```text
NoiseProof has fully validated broken lineage recovery, strict relational lineage, or production-grade provenance repair.
```

