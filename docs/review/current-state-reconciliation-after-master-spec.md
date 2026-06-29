# Current State Reconciliation After Master Spec

Status: implemented.

Phase marker: `current_state_reconciliation_after_master_spec_v0`.

## Purpose

Record the rule that future agents must reconcile multiple current-state
surfaces before selecting the next gate.

The correct read path is:

```text
docs/MASTER-SPEC.md
  -> docs/GOAL.md
  -> docs/application/portfolio-index.md
  -> docs/review/external-reader-proof-path.md
  -> current git status and latest commits
  -> relevant short-term spec in docs/specs/
```

This prevents the project from following an outdated top marker when later
proof artifacts, reviewer paths, or issue-state screens have already moved.

## Source-first Basis

| Source | Pattern used |
|---|---|
| `docs/MASTER-SPEC.md` | Master-spec-first loop and claim-boundary rule. |
| `docs/GOAL.md` | Detailed phase ledger and proof-gap vocabulary. |
| `docs/application/portfolio-index.md` | Broad reviewer-readable current-state map. |
| `docs/review/external-reader-proof-path.md` | Current external-reader navigation path. |
| Diataxis | Keep reader path, explanation, and reference surfaces distinct. |
| SLSA Provenance | Treat current-state claims as needing explicit subject and verification metadata. |

## Rule

Before implementing a future gate, answer these questions:

```text
What does MASTER-SPEC require?
What does GOAL say is still unproven?
What does the portfolio index say is currently surfaced?
What does the external-reader proof path route reviewers to first?
What does git say is actually latest?
Which claim would become misleading if we implemented the wrong gate?
```

If the answers conflict, write a short-term reconciliation spec before touching
runtime code.

## Boundary

This is a documentation and operating-loop reconciliation gate only.

It is not new runtime evidence.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not robust PDF extraction evidence.

It is not production semantic retrieval quality evidence.

It is not product-complete.

## Next Gate

After this gate, choose the next highest-value evidence gate from the reconciled
current-state surfaces. Repeated open gaps still include external reviewer
feedback, robust PDF extraction evidence, production semantic retrieval quality,
hosted deployment, and hosted observability.
