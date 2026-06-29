# Current State Reconciliation After Master Spec v0

Status: implemented in this branch.
Date: 2026-06-30
Target gate: `current_state_reconciliation_after_master_spec_v0`

## Current Repo State

`docs/MASTER-SPEC.md` now exists and requires every future gate to begin with
the master spec, `docs/GOAL.md`, and a short-term spec in `docs/specs/`.

The repository already has many later proof artifacts beyond the top-level
`docs/GOAL.md` overlay. Examples include workflow proof bundles, uploaded raw
file safety surfaces, dashboard anchor method boundaries, ClamAV proof
boundaries, and multiple current-state issue verifications in
`docs/application/portfolio-index.md` and `docs/review/external-reader-proof-path.md`.

The immediate risk is that future agents read only one top marker, select an
outdated next gate, and continue the wrong proof path.

## Sources To Absorb

| Source | Local use |
|---|---|
| `docs/MASTER-SPEC.md` | Use the master-spec-first loop as the source of truth for future gate selection. |
| `docs/GOAL.md` | Keep this as the detailed phase ledger, not the only current-state source. |
| `docs/application/portfolio-index.md` | Treat this as a broad current-state map for reviewer-facing proof surfaces. |
| `docs/review/external-reader-proof-path.md` | Treat this as the external-reader route map and a signal of what first-pass reviewers inspect. |
| [Diataxis](https://diataxis.fr/) | Separate explanation/reference/reviewer path needs instead of merging all docs into one wall. |
| [SLSA Provenance](https://slsa.dev/spec/v1.0/provenance) | Use explicit subject/build/run/proof metadata as a pattern for current-state evidence claims. |

## Non-goals

- no API behavior change
- no retrieval, embedding, Evidence Ledger, Noise Gate, report, or dashboard behavior change
- no hosted deployment claim
- no external reviewer feedback claim
- no robust PDF extraction claim
- no semantic retrieval quality claim
- no attempt to rewrite the whole historical `docs/GOAL.md`

## Implementation Scope

Create:

```text
docs/review/current-state-reconciliation-after-master-spec.md
apps/api/tests/test_current_state_reconciliation_after_master_spec.py
```

Update:

```text
README.md
docs/GOAL.md
docs/runbook.md
docs/application/portfolio-index.md
```

## Data Or API Contract

No data model, API, or runtime behavior changes.

## Tests

Run:

```powershell
cd apps/api
uv run pytest tests/test_current_state_reconciliation_after_master_spec.py -q
uv run pytest tests/test_master_spec_operating_loop.py -q
uv run python -m compileall app ../../packages/ingestion
```

If time allows, run:

```powershell
uv run pytest -q
```

## Docs To Update

- README: surface this as the current operating reconciliation gate.
- GOAL: state that master spec plus portfolio/external-reader paths must be inspected before next-gate selection.
- Runbook: add current-state reconciliation to the gate-start checklist.
- Portfolio index: expose the reconciliation artifact for reviewers.

## Stop Conditions

Stop if:

- current repo state contradicts the proposed reconciliation rule
- adding this gate would imply new runtime evidence
- the spec tries to close external reviewer feedback without external feedback
- tests show existing proof-surface expectations are broken

## Claim Boundaries

Implemented:

- a short-term spec for current-state reconciliation after the master spec
- a review artifact documenting how future agents should select next gates
- tests that keep the reconciliation marker discoverable

Not implemented:

- any new runtime capability
- any new external validation
- any hosted deployment proof
- any product-complete claim

Can claim:

- Future gate selection now has an explicit current-state reconciliation step after reading the master spec.

Cannot claim:

- The public issue has external reviewer feedback.
- NoiseProof is product-complete.
- Robust PDF extraction or production semantic retrieval quality is proven.

## Next Gate If Passed

Return to the reconciled current-state sources:

```text
docs/MASTER-SPEC.md
docs/GOAL.md
docs/application/portfolio-index.md
docs/review/external-reader-proof-path.md
```

Then choose the next highest-value evidence gate. Current repeated proof gaps
still include external reviewer feedback, robust PDF extraction evidence,
production semantic retrieval quality, hosted deployment, and hosted
observability.
