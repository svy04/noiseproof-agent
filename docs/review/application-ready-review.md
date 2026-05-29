# Application-ready Review

Status: Phase 15 review packet.

This is an application-ready review, not a product-complete declaration.

Not product-complete: robust PDF extraction, embeddings, semantic retrieval, `agent_run_id` foreign-key-linked Evidence Ledger / Noise Gate / Report records, distributed tracing, hosted deployment, and external user validation are still unproven.

## Summary

Current judgment: Partial application-ready portfolio artifact.

NoiseProof Agent is strong enough to show a Braincrew-style reviewer the project shape, service boundary, evidence-first workflow, operations surface, persisted Evidence Ledger v0 records, persisted Noise Gate v0 records, persisted Report Preview v0 records, `workflow_trace_id` correlation, preview endpoint traces, failure records, and technical decision trail.

It is not strong enough to claim production RAG quality or autonomous market intelligence.

## Checklist

| Application-ready criterion | Status | Evidence | Boundary |
|---|---|---|---|
| local Docker Compose stack runs | Pass | `docker compose ps` shows healthy `noiseproof-agent-db` | local only |
| PDF, CSV, URL/HTML, markdown memo inputs supported | Partial | parser adapter stubs and text-only PDF fallback | robust PDF extraction is not claimed |
| document profile is generated | Pass | `POST /documents/profile` | direct text payloads only |
| three chunk strategies can be compared | Pass | fixed-window, heading-aware, row-aware | chunks are not persisted |
| retrieval returns source ids | Pass | lexical retrieval v0 | semantic retrieval is not implemented |
| Evidence Ledger can be generated before final answer | Pass | `POST /evidence-ledgers/preview`, `POST /evidence-ledgers` | persisted v0 entries are not yet linked to retrieval run ids |
| unsupported claims are blocked | Pass | Noise Gate, persisted Noise Gate, and Report Preview tests | deterministic checks only |
| contradictions are surfaced | Pass | Evidence Ledger and Noise Gate previews | not a full contradiction engine |
| buy/sell recommendation questions are refused or reframed | Pass | collection, ledger, gate, and report boundaries | not legal or financial advice tooling |
| every agent run leaves a trace | Pass for current preview endpoints | preview endpoints auto-create `agent_runs.trace_json`; retrieval has dedicated `retrieval_runs` | metadata trace only, not distributed tracing or a complete multi-stage workflow trace |
| failure cases are recorded | Pass | failure case endpoint and dashboard | not comprehensive |
| operations dashboard shows runs and failures | Pass | `GET /ops/dashboard` | plain HTML, not polished UI |
| README is understandable without explanation | Pass | `README.md` | should still be reviewed by an external reader |
| architecture and ADRs exist | Pass | `docs/architecture.md`, `docs/adr/*` | ADRs cover initial decisions only |
| evaluation report exists | Pass | `docs/evaluation/*` | not a benchmark |
| Braincrew role map exists | Pass | `docs/application/braincrew-role-map.md` | role fit is an argument, not hiring proof |

## Best External Claim

Use:

```text
NoiseProof Agent is a small, inspectable portfolio service that shows how messy market data can be profiled, retrieved, converted into persisted evidence entries, persisted as gate decisions, stored as claim-bounded report preview records, and correlated with preview endpoint traces through `workflow_trace_id`.
```

Do not use:

```text
NoiseProof Agent is a production-ready RAG system.
NoiseProof Agent predicts markets.
NoiseProof Agent automates trading decisions.
```

## Next Proof-link Pass

If this repo is linked from the portfolio site, link only these claims:

- evidence-first data agent
- not a trading bot
- parser/chunk/retrieval preview boundaries
- Evidence Ledger Preview
- Persisted Evidence Ledger Records v0
- Noise Gate Preview
- Persisted Noise Gate Records v0
- Persisted Report Preview Records v0
- Record Linkage v0 through `workflow_trace_id`
- Operations Dashboard v0
- evaluation/application package
- Auto Trace Recording v0 for preview endpoint metadata

Avoid claims about:

- production deployment
- external users
- robust PDF extraction
- semantic retrieval
- `agent_run_id` foreign-key-linked Evidence Ledger / Noise Gate / Report records
- distributed tracing
- market prediction accuracy
