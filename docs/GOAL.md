# NoiseProof Agent Goal

Future agents should be able to continue the project by reading this file first, inspecting the current repository state, and executing the next highest-value gate without needing a new day-by-day prompt.

## 1. Top-level Purpose

NoiseProof Agent is a noise-resilient data agent for messy market intelligence.

It should prove that a small service can ingest messy market documents and web data, profile source quality, compare chunking and retrieval behavior, record evidence, surface contradictions, block unsupported claims, and generate claim-bounded reports with citations.

The hiring narrative is:

- Primary target: Braincrew Forward Deployed Engineer
- Secondary / long-term target: Braincrew Product Engineer

The project should show customer-like problem definition, service architecture, RAG/Agent workflow judgment, operational logging, failure records, and technical decision documentation.

## 2. Absolute Non-goals

NoiseProof Agent is not a trading bot.

Do not build:

- buy/sell signals
- automatic order execution
- target prices
- return prediction
- stock recommendations
- financial advice
- real-time trading infrastructure
- reinforcement-learning trader
- multi-tenant SaaS v1
- polished UI before logs, failure cases, and evidence behavior exist

If a request drifts toward trading advice, reframe it into evidence-based market intelligence:

- What happened?
- What evidence supports it?
- Which sources conflict?
- Which claims are weak?
- What data is missing?
- Why should this conclusion not be trusted yet?

## 3. Current Accepted State

Accepted state as of Phase 17:

```text
Ingestion Fixtures, Document Profiler v0, Parser Adapter Stubs, Chunk Strategy Experiment v0, Retrieval v0, Collection Plan Preview v0, Evidence Ledger Preview v0, Noise Gate Preview v0, Claim-bounded Report Preview v0, Operations Dashboard v0, Evaluation/Application Package v0, Auto Trace Recording v0, Persisted Evidence Ledger Records v0, Persisted Noise Gate Records v0, Persisted Report Preview Records v0, Record Linkage v0, Trace-id Lookup v0, and Persisted Record Filtering v0
```

Implemented:

- FastAPI app skeleton
- `GET /health`
- `GET /ops/summary`
- metadata persistence routes for documents, agent runs, and failure cases
- PostgreSQL init schema for `documents`, `agent_runs`, and `failure_cases`
- `pgcrypto` and `vector` extension init
- Docker Compose DB service definition
- local Docker runtime persistence verification with PostgreSQL + pgvector
- local port conflict handled with ignored `.env` using `POSTGRES_PORT=55432`
- GitHub Actions API smoke CI
- runbook
- `docs/GOAL.md` continuation source of truth
- messy market data fixtures
- reusable `packages/ingestion` profiler package
- `POST /documents/profile`
- parser adapter stubs for markdown, CSV, HTML/URL, PDF text-only fallback, and unknown source types
- `POST /documents/parse-preview`
- structured parser warnings and failure-case candidates
- chunk strategy experiment v0 for fixed-window, heading-aware, and row-aware strategies
- `POST /documents/chunk-preview`
- chunk comparison metrics:
  - chunk count
  - source character and line counts
  - min, max, and average chunk character counts
  - empty and oversized chunk counts
  - estimated token count
  - structural boundary count
- lexical retrieval v0 over generated chunks
- `POST /retrieval-runs`
- `GET /retrieval-runs`
- source ids attached to retrieval candidates
- retrieval run records persisted in `retrieval_runs`
- no-results retrieval runs recorded with `status: no_results`
- Collection Plan Preview v0
- `POST /collection-plans/preview`
- question-only collection plan input
- required information roles returned before Evidence Ledger work
- buy/sell drift questions include `user_intent_check` and stop conditions
- underspecified, numeric, and source-quality questions expose role-specific warnings
- Evidence Ledger Preview v0
- `POST /evidence-ledgers/preview`
- retrieval candidates converted into claim-level entries
- supported, weakly_supported, contradicted, unsupported, and blocked status labels
- source ids, source types, source dates, evidence spans, confidence, limitations, contradicting source ids, matched terms, and roles returned on entries
- no-evidence questions produce a blocked ledger entry
- buy/sell drift questions produce a blocked ledger entry
- contradiction language is surfaced before report generation
- Noise Gate Preview v0
- `POST /noise-gates/preview`
- pre-report checks over Evidence Ledger entries and optional draft claims
- pass / needs_revision / blocked decisions
- unsupported and blocked ledger entries prevent final response allowance
- buy/sell and financial-advice drift blocks final response allowance
- contradictions, missing source recency, missing limitations, and high-confidence single-source claims require revision
- overconfident draft language is flagged
- Korean fallback message returned for blocked or revision-needed outputs
- Claim-bounded Report Preview v0
- `POST /reports/preview`
- Noise Gate runs before report formatting
- report output is generated only when the gate decision is `pass`
- generated report includes summary, claims, source ids, evidence spans, confidence, limitations, contradictions, and next data needed
- blocked or revision-needed gate outputs return fallback message and required revisions instead of a report
- Operations Dashboard v0
- `GET /ops/dashboard`
- plain browser-readable operations surface over existing metadata
- dashboard shows summary counts, recent agent runs, failure cases, and retrieval runs
- unsupported claim and contradiction counts come from persisted Evidence Ledger entries
- Evaluation/Application Package v0
- `docs/evaluation/eval-plan.md`
- `docs/evaluation/retrieval-eval-report.md`
- `docs/evaluation/failure-cases.md`
- `docs/application/braincrew-role-map.md`
- `docs/application/cover-message.md`
- `docs/application/portfolio-index.md`
- `docs/review/application-ready-review.md`
- Auto Trace Recording v0
- preview endpoints auto-create `agent_runs` metadata records
- `trace_json` records endpoint, phase, source type, counts, gate decisions, and report status where available
- failed preview operations are wrapped so a failed trace can be recorded before the exception is re-raised
- Persisted Evidence Ledger Records v0
- `POST /evidence-ledgers`
- `GET /evidence-ledgers`
- `evidence_ledger_entries` table and migration
- unsupported and contradiction counts in `/ops/summary` come from persisted ledger entries
- Persisted Noise Gate Records v0
- `POST /noise-gates`
- `GET /noise-gates`
- `noise_gate_records` table and migration
- blocked and needs-revision gate counts in `/ops/summary`
- Noise Gate Records section in `/ops/dashboard`
- Persisted Report Preview Records v0
- `POST /reports`
- `GET /reports`
- `report_records` table and migration
- generated, blocked, and needs-revision report counts in `/ops/summary`
- Report Records section in `/ops/dashboard`
- Record Linkage v0
- `workflow_trace_id` on persisted Evidence Ledger records
- `workflow_trace_id` on persisted Noise Gate records
- `workflow_trace_id` on persisted Report records
- matching `workflow_trace_id` in `agent_runs.trace_json` for persisted evidence/gate/report endpoints
- Trace-id Lookup v0
- `GET /traces/{workflow_trace_id}`
- lookup response includes matching agent runs, Evidence Ledger entries, Noise Gate records, Report records, and summary counts
- Persisted Record Filtering v0
- `GET /evidence-ledgers?workflow_trace_id=...`
- `GET /evidence-ledgers?status=...`
- `GET /noise-gates?workflow_trace_id=...`
- `GET /noise-gates?decision=...`
- `GET /reports?workflow_trace_id=...`
- `GET /reports?status=...`
- Document Profiler v0 fields:
  - source type
  - character count
  - line count
  - approximate token count
  - table, URL, date, and number detection
  - extraction quality
  - recommended strategy
  - warnings

Not yet implemented:

- file upload
- robust PDF extraction
- persisted parse records
- persisted chunks
- persisted collection plans
- embeddings
- `agent_run_id` foreign-key-linked Evidence Ledger, Noise Gate, and Report records
- full distributed tracing or hosted observability

## 4. How Future Agents Continue

Every continuation agent must:

1. Read this file first.
2. Inspect the repository state.
3. Determine the next incomplete phase from the phase ladder.
4. Implement only that gate.
5. Update tests, `README.md`, `docs/runbook.md`, and relevant docs.
6. Run available verification commands.
7. Commit with a phase-specific message.
8. Report what is implemented, what remains planned, tests run, tests not run and why, and the next recommended gate.

Do not skip gates.
Do not make the project more impressive than it is.
Make it easier to inspect what works, what fails, what is blocked, and what remains unproven.

## 5. Phase Ladder

```text
Phase 0   - Documentation-first package
Phase 1   - Service skeleton and metadata persistence
Phase 1.5 - Runtime persistence verification
Phase 2   - Ingestion fixtures and Document Profiler v0
Phase 3   - Parser adapter stubs
Phase 4   - Chunk strategy experiment v0
Phase 5   - Retrieval v0
Phase 5.5 - Collection Plan Preview v0
Phase 6   - Evidence Ledger v0
Phase 7   - Critic / Noise Gate v0
Phase 8   - Claim-bounded report v0
Phase 9   - Operations dashboard v0
Phase 10  - Evaluation and application package
Phase 11  - Auto Trace Recording v0
Phase 12  - Persisted Evidence Ledger Records v0
Phase 13  - Persisted Noise Gate Records v0
Phase 14  - Persisted Report Preview Records v0
Phase 15  - Record Linkage v0
Phase 16  - Trace-id Lookup v0
Phase 17  - Persisted Record Filtering v0
```

### Phase 1.5 - Runtime Persistence Verification

If Docker is available, verify:

```bash
docker compose config
docker compose up -d db
docker compose ps
cd apps/api
uv sync
uv run uvicorn app.main:app --reload
```

Then call:

```bash
curl http://localhost:8000/health
curl http://localhost:8000/ops/summary
curl -X POST http://localhost:8000/documents ...
curl http://localhost:8000/documents
```

If Docker is not available, report:

```text
Docker runtime verification was not performed in this environment.
```

Do not pretend runtime persistence was verified when it was not.

### Phase 2 - Ingestion Fixtures and Document Profiler v0

Required outputs:

```text
examples/messy-market-data/README.md
examples/messy-market-data/sample-note.md
examples/messy-market-data/sample-market.csv
examples/messy-market-data/sample-report.txt
examples/messy-market-data/sample-page.html
packages/ingestion/__init__.py
packages/ingestion/types.py
packages/ingestion/profiler.py
apps/api/app/services/document_profiler.py
```

Preferred API:

```text
POST /documents/profile
```

Profile fields:

```text
source_type
character_count
line_count
approximate_token_count
has_tables
has_urls
has_dates
has_numbers
extraction_quality
recommended_strategy
warnings
```

Phase 2 should not parse files from uploads. It profiles provided text or fixture-like content only.

### Phase 3 - Parser Adapter Stubs

Implemented outputs:

```text
packages/ingestion/parsers/__init__.py
packages/ingestion/parsers/base.py
packages/ingestion/parsers/markdown.py
packages/ingestion/parsers/csv.py
packages/ingestion/parsers/html.py
packages/ingestion/parsers/pdf.py
packages/ingestion/selector.py
apps/api/app/services/parse_preview.py
POST /documents/parse-preview
```

Parse-preview accepts direct text payloads and returns:

```text
source_type
parser
text
metadata
warnings
failure_case_candidate
profile
```

The PDF parser is currently a text-only fallback. Robust PDF extraction is not claimed.

### Phase 4 - Chunk Strategy Experiment v0

Implemented outputs:

```text
packages/ingestion/chunking/__init__.py
packages/ingestion/chunking/experiment.py
apps/api/app/services/chunk_preview.py
POST /documents/chunk-preview
```

Chunk-preview accepts direct text payloads and returns:

```text
source_type
parser
profile
parse_warnings
failure_case_candidate
strategies
```

Implemented strategies:

```text
fixed-window
heading-aware
row-aware
```

Phase 4 does not persist chunks, run retrieval, compute embeddings, generate Evidence Ledger entries, call LLMs, or build a dashboard.

Current local `docs/GOAL.md` does not include a separate `Parallel research track` section. Phase 4 research influence is intentionally limited to strategy names and comparison metrics.

### Phase 5 - Retrieval v0

Implemented outputs:

```text
packages/ingestion/retrieval/__init__.py
packages/ingestion/retrieval/lexical.py
apps/api/app/services/retrieval_run.py
apps/api/app/routes/retrieval_runs.py
POST /retrieval-runs
GET /retrieval-runs
```

Retrieval v0 accepts direct text sources and returns:

```text
id
question
strategy
status
latency_ms
result_count
hit_rate
citation_coverage
missing_evidence_count
metadata_json
created_at
results
warnings
```

Each result includes:

```text
source_id
source_type
chunk_strategy
chunk_index
text
score
matched_terms
metadata
```

Phase 5 does not persist chunks, compute embeddings, create Evidence Ledger entries, call LLMs, generate final answers, create reports, run a Critic / Noise Gate, or build a dashboard.

### Phase 5.5 - Collection Plan Preview v0

Implemented outputs:

```text
packages/ingestion/collection/__init__.py
packages/ingestion/collection/planner.py
apps/api/app/services/collection_plan.py
apps/api/app/routes/collection_plans.py
POST /collection-plans/preview
```

Collection Plan Preview accepts a question and returns:

```text
question
information_need
possible_claims
required_roles
source_types_to_check
minimum_evidence_needed
known_risks
stop_conditions
warnings
```

Implemented role examples:

```text
direct_support
contradiction
quantitative_anchor
timeline_anchor
definition_anchor
source_quality_check
missing_data_signal
scope_boundary
user_intent_check
```

Phase 5.5 is a deterministic preview boundary. It does not call LLMs, search external sources, expand retrieval, create Evidence Ledger entries, run a Critic / Noise Gate, generate final answers, create reports, build a dashboard, or persist collection plans.

### Phase 6 - Evidence Ledger Preview v0

Implemented outputs:

```text
packages/ingestion/evidence/__init__.py
packages/ingestion/evidence/ledger.py
apps/api/app/services/evidence_ledger.py
apps/api/app/routes/evidence_ledgers.py
POST /evidence-ledgers/preview
```

Evidence Ledger Preview accepts a question and direct retrieval candidates, then returns:

```text
question
entries
summary
warnings
```

Each entry includes:

```text
claim
source_id
source_type
source_date
evidence_span
confidence
limitation
contradicting_source_ids
status
matched_terms
role
```

Implemented statuses:

```text
supported
weakly_supported
contradicted
unsupported
blocked
```

Phase 6 is a deterministic preview boundary. It does not call LLMs, search external sources, persist Evidence Ledger entries, run a Critic / Noise Gate, generate final answers, create reports, or build a dashboard.

### Phase 7 - Noise Gate Preview v0

Implemented outputs:

```text
packages/ingestion/noise_gate/__init__.py
packages/ingestion/noise_gate/gate.py
apps/api/app/services/noise_gate.py
apps/api/app/routes/noise_gates.py
POST /noise-gates/preview
```

Noise Gate Preview accepts a question, Evidence Ledger entries, and optional draft claims, then returns:

```text
question
decision
final_response_allowed
checks
blocked_claims
downgraded_claims
allowed_claims
required_revisions
fallback_message
warnings
```

Implemented checks:

```text
every_strong_claim_has_evidence
unsupported_claim_blocking
contradictions_are_surfaced
source_recency_visible
high_confidence_has_two_sources
limitations_explicit
trading_advice_drift
overconfident_language
```

Phase 7 is a deterministic preview boundary. It does not call LLMs, search external sources, persist gate records, generate final answers, create reports, or build a dashboard.

### Phase 8 - Claim-bounded Report Preview v0

Implemented outputs:

```text
packages/ingestion/reports/__init__.py
packages/ingestion/reports/report.py
apps/api/app/services/report_preview.py
apps/api/app/routes/reports.py
POST /reports/preview
```

Report Preview accepts a question, Evidence Ledger entries, and optional draft claims. It runs Noise Gate Preview first, then returns:

```text
question
status
report
gate
fallback_message
required_revisions
warnings
```

When the gate passes, `report` includes:

```text
summary
claims
limitations
contradictions
next_data_needed
```

Each report claim includes:

```text
claim
source_ids
evidence_spans
confidence
limitations
contradictions
```

Phase 8 is a deterministic preview boundary. It does not call LLMs, search external sources, persist report records, or generate free-form answers beyond the bounded report shape.

### Phase 9 - Operations Dashboard v0

Implemented outputs:

```text
apps/api/app/services/ops_dashboard.py
GET /ops/dashboard
```

Operations Dashboard v0 is a plain FastAPI HTML view over current metadata. It shows:

```text
summary counts
recent agent runs
failure cases
retrieval runs
unsupported and contradiction counts from persisted Evidence Ledger entries
```

Phase 9 did not add Next.js, UI polish, LLM calls, new retrieval behavior, persisted Evidence Ledger entries, persisted Noise Gate records, or persisted report records. Phase 12 later added persisted Evidence Ledger entries, and Phase 13 later added persisted Noise Gate records.

### Phase 10 - Evaluation and Application Package v0

Implemented outputs:

```text
docs/evaluation/eval-plan.md
docs/evaluation/retrieval-eval-report.md
docs/evaluation/failure-cases.md
docs/application/braincrew-role-map.md
docs/application/cover-message.md
docs/application/portfolio-index.md
docs/review/application-ready-review.md
apps/api/tests/test_docs.py
```

Phase 10 does not add new runtime product behavior. It makes the current evidence, failures, role fit, and unproven boundaries easier to inspect.

Phase 10 handoff:

```text
Auto Trace Recording v0
```

### Phase 11 - Auto Trace Recording v0

Implemented outputs:

```text
apps/api/app/services/run_trace.py
preview endpoint trace creation in agent_runs
trace phase uses the current workflow version
```

The current preview endpoints create `agent_runs` metadata records:

```text
POST /documents/profile
POST /documents/parse-preview
POST /documents/chunk-preview
POST /collection-plans/preview
POST /evidence-ledgers/preview
POST /noise-gates/preview
POST /reports/preview
```

Trace records include:

```text
endpoint
phase
latency_ms
status
source_type where available
route-specific counts
gate decisions where available
report status where available
```

Phase 11 does not add LLM calls, embeddings, retrieval expansion, persisted Noise Gate records, persisted report records, distributed tracing, hosted observability, or dashboard UI polish.

Phase 11 handoff:

```text
Persisted Evidence Ledger records v0
```

### Phase 12 - Persisted Evidence Ledger Records v0

Implemented outputs:

```text
db/migrations/002_evidence_ledger_entries.sql
POST /evidence-ledgers
GET /evidence-ledgers
evidence_ledger_entries table
ops summary unsupported/contradiction counts from persisted ledger entries
```

Persisted entries include:

```text
id
run_id
question
claim
source_id
source_type
source_date
evidence_span
confidence
limitation
contradicting_source_ids
status
matched_terms
role
created_at
```

Phase 12 does not add retrieval expansion, embeddings, semantic retrieval, LLM calls, persisted Noise Gate records, persisted report records, or dashboard UI polish. Current persisted entries are not yet linked to retrieval run ids.

Phase 12 handoff:

```text
Persisted Noise Gate records v0
```

### Phase 13 - Persisted Noise Gate Records v0

Implemented outputs:

```text
db/migrations/003_noise_gate_records.sql
POST /noise-gates
GET /noise-gates
noise_gate_records table
ops summary blocked/revision gate counts
ops dashboard Noise Gate Records section
```

Persisted records include:

```text
id
question
decision
final_response_allowed
checks
blocked_claims
downgraded_claims
allowed_claims
required_revisions
fallback_message
warnings
evidence_entry_count
draft_claim_count
created_at
```

Phase 13 does not add retrieval expansion, embeddings, semantic retrieval, LLM calls, persisted report records, final report generation beyond the preview shape, agent-run-linked gate records, or dashboard UI polish.

### Phase 14 - Persisted Report Preview Records v0

Implemented outputs:

```text
db/migrations/004_report_records.sql
POST /reports
GET /reports
report_records table
ops summary generated/blocked/revision report counts
ops dashboard Report Records section
```

Persisted records include:

```text
id
question
status
report
gate
gate_decision
fallback_message
required_revisions
warnings
claim_count
evidence_entry_count
draft_claim_count
created_at
```

Phase 14 does not add retrieval expansion, embeddings, semantic retrieval, LLM calls, free-form final report generation, agent-run-linked report records, or dashboard UI polish.

### Phase 15 - Record Linkage v0

Implemented outputs:

```text
db/migrations/005_workflow_trace_ids.sql
workflow_trace_id on evidence_ledger_entries
workflow_trace_id on noise_gate_records
workflow_trace_id on report_records
matching workflow_trace_id in agent_runs.trace_json for POST /evidence-ledgers, POST /noise-gates, and POST /reports
```

Phase 15 is not full distributed tracing and does not add `agent_run_id` foreign-key linkage. It only makes persisted records and their trace metadata joinable by a shared local workflow trace id.

### Phase 16 - Trace-id Lookup v0

Implemented outputs:

```text
GET /traces/{workflow_trace_id}
trace lookup response with agent_runs
trace lookup response with evidence_ledger_entries
trace lookup response with noise_gate_records
trace lookup response with report_records
trace lookup summary counts
```

Phase 16 does not add distributed tracing, hosted observability, `agent_run_id` foreign-key linkage, LLM calls, embeddings, semantic retrieval, or dashboard polish.

### Phase 17 - Persisted Record Filtering v0

Implemented outputs:

```text
GET /evidence-ledgers?workflow_trace_id=...
GET /evidence-ledgers?status=...
GET /noise-gates?workflow_trace_id=...
GET /noise-gates?decision=...
GET /reports?workflow_trace_id=...
GET /reports?status=...
```

Phase 17 is read-only filtering over existing persisted records. It does not add search, ranking, semantic retrieval, LLM calls, dashboard polish, or hosted observability.

Next recommended implementation phase:

```text
Dashboard trace/filter links v0
```

## 6. Ordering Rules

Do not implement embeddings before profiler exists.
Do not implement retrieval before chunk strategy exists.
Do not implement report generation before Evidence Ledger exists.
Do not build a dashboard before logs and failures exist.
Do not polish UI before the system has inspectable failure behavior.

## 7. Testing Rules

Every phase must add or update tests for the new boundary.

Minimum checks:

- `uv run python -m compileall app` from `apps/api`
- `uv run pytest -q` from `apps/api`
- schema or fixture checks when relevant
- Docker checks only when Docker is available

If a verification command cannot run in the environment, report the exact reason.

## 8. Documentation Rules

When a phase changes the system, update:

- `README.md`
- `docs/runbook.md`
- relevant architecture or evaluation docs

Always distinguish:

- implemented
- planned
- unverified

## 9. Commit and Report Rules

Use phase-specific commit messages, for example:

```text
docs: add project goal and continuation gates
feat: add document profiler v0
feat: add parser adapter stubs
feat: add chunk strategy experiment v0
```

Final report must include:

- commit hash
- what is implemented
- what remains planned
- tests run
- tests not run and why
- next recommended gate

## 10. Application-ready Definition

NoiseProof Agent is application-ready only when:

- local Docker Compose stack runs
- at least PDF, CSV, URL/HTML, and markdown memo inputs are supported
- document profile is generated
- three chunk strategies can be compared
- retrieval returns source ids
- Evidence Ledger can be generated before final answer
- unsupported claims are blocked
- contradictions are surfaced
- buy/sell recommendation questions are refused or reframed
- each agent run leaves a trace
- failure cases are recorded
- operations dashboard shows runs and failures
- README is understandable without explanation
- architecture and ADRs exist
- evaluation report exists
- Braincrew role map exists

Until then, report progress as phased evidence, not product completion.
