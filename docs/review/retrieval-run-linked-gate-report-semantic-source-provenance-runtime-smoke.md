# Retrieval-run-linked Gate/Report Semantic Source Provenance Runtime Smoke

Status: implemented.

Purpose: verify with local Docker PostgreSQL and live FastAPI HTTP that semantic retrieval source provenance survives from a persisted retrieval run through the retrieval-run-linked Evidence Ledger, Noise Gate, Report, and agent-run trace handoffs.

Marker:

```text
retrieval-run-linked Gate/Report semantic source provenance runtime smoke v0
```

Runtime environment:

```text
Docker version 29.4.3
Docker Compose version v5.1.3
Compose project -> noiseproof-phase634
POSTGRES_PORT=55445
API_PORT=8051
DATABASE_URL=postgresql://noiseproof:noiseproof@localhost:55445/noiseproof
```

Database verification:

```text
Initial migration status:
Applied migrations: 0
Pending migrations: 23

Final migration status:
Applied migrations: 23
Pending migrations: 0
```

Smoke path:

```text
GET /health
POST /documents
POST /documents/{document_id}/chunks
POST /chunks/{chunk_id}/embeddings
POST /documents/{document_id}/semantic-retrieval-runs
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
POST /retrieval-runs/{retrieval_run_id}/noise-gate
POST /retrieval-runs/{retrieval_run_id}/report
GET /agent-runs
```

Observed markers:

```text
health_status -> ok
retrieval_mode -> semantic_persisted
retrieval_query_vector_source -> caller_provided_vector
retrieval_persistence_boundary -> semantic_retrieval_run_only_no_evidence_ledger
ledger_entry_count -> 2
ledger_source_retrieval_mode -> semantic_persisted
ledger_query_vector_source -> caller_provided_vector
ledger_is_semantic -> true
ledger_persistence_boundary -> semantic_retrieval_run_only_no_evidence_ledger
gate_source_retrieval_mode -> semantic_persisted
gate_query_vector_source -> caller_provided_vector
gate_is_semantic -> true
gate_handoff_performs_semantic_retrieval -> false
gate_warning_has_source_mode -> true
report_source_retrieval_mode -> semantic_persisted
report_query_vector_source -> caller_provided_vector
report_is_semantic -> true
report_handoff_performs_semantic_retrieval -> false
report_warning_has_source_mode -> true
gate_trace_source_retrieval_mode -> semantic_persisted
gate_trace_query_vector_source -> caller_provided_vector
gate_trace_handoff_performs_semantic_retrieval -> false
report_trace_source_retrieval_mode -> semantic_persisted
report_trace_query_vector_source -> caller_provided_vector
report_trace_handoff_performs_semantic_retrieval -> false
```

Interpretation:

- the semantic persisted retrieval-run provenance is present on the retrieval run;
- the retrieval-run-linked Evidence Ledger persists the semantic source provenance in entry metadata;
- the retrieval-run-linked Noise Gate preserves that provenance in `stage_input_manifest`, warnings, and agent-run trace metadata;
- the retrieval-run-linked Report preserves the same provenance in `stage_input_manifest`, warnings, and agent-run trace metadata;
- downstream handoffs do not perform semantic retrieval again.

Verification:

```text
local Docker PostgreSQL health -> healthy
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
live FastAPI HTTP smoke against http://127.0.0.1:8051
```

Boundary:

- this is local Docker/FastAPI runtime evidence only;
- this is source-provenance handoff evidence;
- this is not semantic retrieval quality evidence;
- this is not embedding generation;
- this is not live OpenAI provider evidence;
- this is not Evidence Ledger quality evidence;
- this is not Noise Gate quality evidence;
- this is not report quality evidence;
- this is not final truth adjudication;
- this is not hosted deployment evidence;
- this is not external reviewer feedback;
- this is not product-complete.

Next gate:

External reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from the current repository state.
