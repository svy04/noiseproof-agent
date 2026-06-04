# External Reviewer Architecture Current-state Request Refresh

Phase marker: external reviewer architecture current-state request refresh v0.

## Why this exists

Phase 336 refreshed `docs/architecture.md` so it no longer describes implemented uploaded-file persistence, chunk/retrieval persistence, caller-provided embeddings, semantic retrieval persistence, and retrieval-run-linked proof handoffs as planned-only work.

External reviewers should be able to find that current-state correction from the request path, otherwise they may review stale architecture boundaries instead of the current proof surface.

## Added reviewer link

```text
docs/review/architecture-current-state-refresh.md
```

This link is added to:

- `docs/review/external-review-request.md`
- `docs/review/external-reviewer-link-map.md`
- `.github/ISSUE_TEMPLATE/external-review-feedback.md`
- `docs/application/portfolio-index.md`
- `README.md`
- `docs/runbook.md`
- `docs/GOAL.md`

## Boundary

This is request infrastructure only.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not endpoint malicious-detection runtime proof.

It is not robust PDF extraction, embedding generation, production semantic retrieval quality, customer validation, Braincrew acceptance, or product-complete evidence.

Next recommended gate remains:

```text
external reviewer feedback v0
```
