# Architecture Current-state Refresh

Phase marker: architecture current-state refresh v0.

## Why this exists

`docs/architecture.md` had several stale planned-only boundaries from earlier phases. Those lines still said file upload parsing, persisted chunks, retrieval-run-linked Evidence Ledger handoff, Noise Gate linkage, and Report linkage were not implemented, even though later bounded phases added explicit uploaded-file persistence, chunk persistence, retrieval persistence, caller-provided embedding storage, semantic retrieval persistence, and retrieval-run-linked proof handoffs.

This refresh keeps the architecture page aligned with the current repository state.

## Refreshed claims

The architecture now says the following surfaces exist:

- uploaded file intake manifest persistence
- uploaded file parsed document metadata persistence
- uploaded file chunk persistence
- uploaded file retrieval persistence
- uploaded raw file quarantine storage
- metadata-only raw-file scan records
- explicit raw-file scan execution with scanner-unavailable defaults
- ClamAV opt-in clean-file endpoint proof
- caller-provided chunk embeddings
- caller-provided semantic retrieval persistence
- retrieval-run-linked Evidence Ledger
- retrieval-run-linked Noise Gate
- retrieval-run-linked Report
- workflow lineage read models
- dashboard lineage links
- failure-case records

## Still unproven

This refresh does not add runtime behavior. It does not prove:

- robust PDF extraction
- embedding generation
- production semantic retrieval quality
- hosted deployment evidence
- hosted observability
- external reviewer feedback
- endpoint malicious-detection runtime proof
- autonomous/LLM-backed agents
- polished web app behavior

## Boundary

This is documentation/current-state alignment only. It adds no schema, migration, endpoint, LLM call, retrieval behavior, malware scanning proof, hosted deployment evidence, external validation, or product-complete claim.

Next recommended gate remains:

```text
external reviewer feedback v0
```
