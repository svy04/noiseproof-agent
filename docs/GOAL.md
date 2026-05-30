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

Accepted state as of Phase 56:

```text
Ingestion Fixtures, Document Profiler v0, Parser Adapter Stubs, Chunk Strategy Experiment v0, Retrieval v0, Collection Plan Preview v0, Evidence Ledger Preview v0, Noise Gate Preview v0, Claim-bounded Report Preview v0, Operations Dashboard v0, Evaluation/Application Package v0, Auto Trace Recording v0, Persisted Evidence Ledger Records v0, Persisted Noise Gate Records v0, Persisted Report Preview Records v0, Record Linkage v0, Trace-id Lookup v0, Persisted Record Filtering v0, Dashboard Trace/Filter Links v0, Agent-run Linkage Review v0, Agent-run Lifecycle v0, Persisted Child Record Agent-run Linkage v0, Dashboard Parent/Child Provenance Links v0, Evidence Ledger Dashboard Table v0, Evidence-to-gate/report Local Cross-links Review v0, Single Workflow Parent Review v0, WorkflowRun Schema v0, WorkflowRun Metadata Persistence v0, WorkflowRun Dashboard Table v0, WorkflowRun Child-link Review v0, Deterministic Workflow Execution Preview v0, WorkflowRun Child-record Links v0, WorkflowRun Child Inspection Surface v0, Direct Evidence-to-gate/report Cross-link Review v0, Workflow Stage Input Manifest v0, Direct Cross-stage Link Schema Review v0, Workflow Lineage Read Model v0, Workflow Lineage Dashboard Links v0, Workflow Lineage Missing-reference Review v0, Workflow Lineage Missing-reference Test v0, Workflow Lineage Boundary Hardening Review v0, Workflow Lineage Manifest-shape Hardening v0, Workflow Lineage Warning Taxonomy Review v0, Structured Warning Taxonomy v0, Workflow Lineage Warning Code Documentation Review v0, Workflow Lineage Warning Code Runbook Example v0, Workflow Lineage Warning Code Dashboard Review v0, Workflow Lineage Warning Code Dashboard Surfacing v0, Workflow Lineage Warning Code Dashboard Smoke Example v0, Workflow Version Naming Review v0, Workflow Version Naming Update v0, Workflow Version Naming Smoke Example v0, Workflow Version Naming Consistency Review v0, Schema Default Workflow Version Update v0, Schema Default Workflow Version Smoke Example v0, Runtime DB Schema Default Verification v0, Migration Runner Review v0, Lightweight SQL Migration Runner v0, Runtime Migration Runner Verification v0, Migration Runner Fresh DB Verification v0, Migration Runner Runbook Cleanup v0, Fresh DB API Smoke Verification v0, Application Evidence Index Refresh v0, Failure-case Persistence Smoke Verification v0, Failure-case Application Evidence Refresh v0, Agent-run Failure Linkage Smoke Verification v0, Agent-run Failure Linkage Application Refresh v0, Workflow Failure Provenance Review v0, and Workflow Failure Linkage Smoke Verification v0
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
- workflow lineage warning taxonomy review artifact
- `warning_codes` on `GET /workflow-runs/{id}/lineage`
- workflow lineage warning code documentation review artifact
- runbook lineage warning-code response example
- workflow lineage warning code dashboard review artifact
- Lineage warning codes legend in `GET /ops/dashboard`
- runbook dashboard warning-code smoke example
- workflow version naming review artifact
- runtime `workflow_version` renamed to `phase40-lineage-warning-code-dashboard`
- runbook workflow-version smoke checks for `/health` and `/ops/summary`
- workflow version naming consistency review artifact
- stale schema defaults identified in `db/init/001_schema.sql` and `db/migrations/007_workflow_runs.sql`
- fresh schema defaults now use `phase40-lineage-warning-code-dashboard`
- forward migration `db/migrations/010_workflow_version_defaults.sql`
- runbook schema-default workflow-version smoke example
- runtime Docker DB schema defaults verified after applying migration 010
- migration runner review artifact
- lightweight SQL migration runner at `python -m app.migration_runner`
- `schema_migrations` tracking table managed by the runner
- baseline, status, and apply modes
- runtime migration runner status and baseline verified against local Docker DB
- migration runner apply path verified against an isolated fresh Docker DB
- fresh DB runner status moved from 0 applied / 9 pending to 9 applied / 0 pending
- fresh DB `schema_migrations` contained all 9 migration filenames after apply
- fresh DB workflow-version defaults verified as `phase40-lineage-warning-code-dashboard`
- isolated fresh DB test volume removed after verification
- migration runbook now presents the runner as the default path
- manual SQL piping is documented as a legacy/debug fallback
- fresh/reset DB and existing already-migrated DB runner paths are separated
- fresh migrated Docker DB API smoke verified with `GET /health`, `GET /ops/summary`, `POST /documents`, and `GET /documents`
- fresh DB document persistence smoke verified with `Sample fresh DB smoke document`
- fresh DB API smoke test volume removed after verification
- application-facing evidence index refreshed with migration runner and fresh DB API smoke artifacts
- Braincrew role map now includes local runtime proof surfaces and hosted-deployment boundary
- application-ready review now includes migration/API smoke evidence without claiming hosted deployment evidence
- failure-case persistence smoke verified against an isolated fresh migrated Docker DB
- `POST /failure-cases` and `GET /failure-cases` verified with a parser_timeout failure record
- `/ops/summary` failure_case_count verified from 0 to 1 after failure creation
- application-facing evidence index refreshed with failure-case persistence smoke artifact
- Braincrew role map now distinguishes failure-case persistence from automatic failure detection
- application-ready review now includes failure-case persistence smoke without claiming automatic failure detection
- agent-run failure linkage smoke verified against an isolated fresh migrated Docker DB
- `POST /agent-runs`, `POST /failure-cases`, `GET /failure-cases`, and `GET /agent-runs` verified with linked ids
- `/ops/summary` verified `agent_run_count: 1` and `failure_case_count: 1` after linked failure creation
- application-facing evidence index refreshed with agent-run failure linkage smoke artifact
- Braincrew role map now distinguishes linked failure-case proof from complete workflow failure causality
- application-ready review now includes agent-run failure linkage smoke without claiming complete workflow failure causality
- workflow failure provenance reviewed before adding schema
- `workflow_run_id` on `failure_cases` deferred until a real workflow failure path exists
- automatic failure detection deferred and explicitly unclaimed
- workflow failure linkage smoke verified with a route-level test fixture
- failed deterministic workflow preview parents are marked `failed` when a downstream stage raises
- `failure_cases` remain unchanged by the workflow failure smoke fixture
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
- Dashboard Trace/Filter Links v0
- `GET /ops/dashboard` exposes trace lookup links for observed `workflow_trace_id` values
- `GET /ops/dashboard` exposes quick filter links for Evidence Ledger statuses, Noise Gate decisions, and Report statuses
- Agent-run Linkage Review v0
- `docs/review/agent-run-linkage-review.md`
- direct `agent_run_id` foreign-key linkage reviewed before Phase 20 implementation
- Agent-run Lifecycle v0
- `run_with_trace()` creates a parent `agent_runs` row before operation execution
- `run_with_trace()` updates the same row to `completed` or `failed` after execution
- Persisted Child Record Agent-run Linkage v0
- `agent_run_id` on persisted Evidence Ledger records
- `agent_run_id` on persisted Noise Gate records
- `agent_run_id` on persisted Report records
- `db/migrations/006_child_agent_run_ids.sql`
- Dashboard Parent/Child Provenance Links v0
- `GET /ops/dashboard` shows parent run links for persisted Noise Gate records
- `GET /ops/dashboard` shows parent run links for persisted Report records
- parent run links use trace lookup, not a separate agent-run detail endpoint
- Evidence Ledger Dashboard Table v0
- `GET /ops/dashboard` shows persisted Evidence Ledger rows
- Evidence Ledger dashboard rows include trace links, parent run links, status filters, claim, evidence span, source, and confidence
- Evidence-to-gate/report Local Cross-links Review v0
- `docs/review/evidence-to-gate-report-cross-links-review.md`
- direct evidence -> gate -> report cross-links are deferred until a single workflow parent exists
- Single Workflow Parent Review v0
- `docs/review/single-workflow-parent-review.md`
- `agent_runs` remains operation-level provenance, not workflow-level provenance
- future implementation direction is a separate `workflow_runs` table before cross-stage links
- WorkflowRun Schema v0
- `workflow_runs` table in `db/init/001_schema.sql`
- `db/migrations/007_workflow_runs.sql`
- workflow parent status values: `created`, `running`, `completed`, `failed`, `blocked`, `needs_revision`
- WorkflowRun Metadata Persistence v0
- `POST /workflow-runs`
- `GET /workflow-runs`
- WorkflowRun route, schemas, and repository methods
- WorkflowRun Dashboard Table v0
- `GET /ops/dashboard` shows workflow-run metadata rows
- dashboard boundary copy labels workflow-run rows as metadata-only, not workflow execution
- WorkflowRun Child-link Review v0
- `docs/review/workflow-run-child-link-review.md`
- child `workflow_run_id` columns were deferred before Phase 28 and implemented after the deterministic execution preview in Phase 29
- Deterministic Workflow Execution Preview v0
- `POST /workflow-runs/execute-preview`
- parent `workflow_runs` row creation before deterministic execution
- parent workflow row completion/failure updates after execution
- deterministic retrieval -> evidence -> gate -> report preview sequence
- child records correlated by `workflow_trace_id`
- WorkflowRun Child-record Links v0
- `db/migrations/008_child_workflow_run_ids.sql`
- nullable `workflow_run_id` on `retrieval_runs`
- nullable `workflow_run_id` on `evidence_ledger_entries`
- nullable `workflow_run_id` on `noise_gate_records`
- nullable `workflow_run_id` on `report_records`
- `POST /workflow-runs/execute-preview` attaches its deterministic child records to the parent workflow run id
- WorkflowRun Child Inspection Surface v0
- `GET /workflow-runs/{id}`
- workflow-run detail response with linked retrieval, evidence, gate, and report records
- child record summary counts by workflow parent
- Direct Evidence-to-gate/report Cross-link Review v0
- `docs/review/direct-evidence-gate-report-cross-link-review.md`
- direct evidence -> gate -> report foreign-key links remain deferred until downstream stages consume persisted upstream row ids
- Workflow Stage Input Manifest v0
- `db/migrations/009_stage_input_manifest.sql`
- `stage_input_manifest` JSONB on persisted Noise Gate records
- `stage_input_manifest` JSONB on persisted Report records
- deterministic workflow-created Noise Gate records record persisted Evidence Ledger row ids used as input
- deterministic workflow-created Report records record persisted Evidence Ledger row ids and the persisted Noise Gate record id used as input
- `GET /workflow-runs/{id}` returns those manifests with linked child records
- `GET /ops/dashboard` exposes those manifests in the plain record tables
- Direct Cross-stage Link Schema Review v0
- `docs/review/direct-cross-stage-link-schema-review.md`
- decision not to add direct evidence -> gate -> report foreign-key links or join tables yet
- next direction for a derived Workflow lineage read model v0
- Workflow Lineage Read Model v0
- `GET /workflow-runs/{id}/lineage`
- derived read model over existing workflow child records and stage_input_manifest values
- resolves Noise Gate input Evidence Ledger ids back to linked Evidence Ledger records
- resolves Report input Evidence Ledger ids and Noise Gate record ids back to linked records
- missing manifest references are surfaced in the response
- does not add migrations, columns, join tables, direct foreign-key links, or new storage
- Workflow Lineage Dashboard Links v0
- detail and lineage links from workflow rows in `GET /ops/dashboard`
- links point to `GET /workflow-runs/{id}` and `GET /workflow-runs/{id}/lineage`
- no dashboard polish, frontend framework, new storage, or lineage schema added
- Workflow Lineage Missing-reference Review v0
- `docs/review/workflow-lineage-missing-reference-review.md`
- review-only decision to keep missing-reference proof as a targeted test before schema or mutation changes
- no migrations, columns, join tables, or runtime mutation paths added
- Workflow Lineage Missing-reference Test v0
- targeted route test proves `GET /workflow-runs/{id}/lineage` returns `missing_reference_count > 0` for broken `stage_input_manifest` values
- missing Evidence Ledger ids and missing Noise Gate ids are surfaced without a malformed-manifest mutation API
- no migrations, columns, or join tables added
- Workflow Lineage Boundary Hardening Review v0
- `docs/review/workflow-lineage-boundary-hardening-review.md`
- non-list manifest values, duplicate references, and cross-workflow references reviewed before schema changes
- next direction for manifest-shape hardening without adding migrations, columns, join tables, mutation endpoints, or repair endpoints
- Workflow Lineage Manifest-shape Hardening v0
- non-list `input_evidence_ledger_entry_ids` values produce an empty id list and a structured warning
- string values are not treated as iterable evidence id lists
- duplicate manifest references preserve order and count
- cross-workflow references remain local missing references
- workflow version `phase36-structured-warning-taxonomy`
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
- autonomous or LLM-backed workflow execution
- embeddings
- direct evidence -> gate -> report foreign-key lineage
- direct evidence -> gate -> report join tables
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
Phase 18  - Dashboard Trace/Filter Links v0
Phase 18.5 - Agent-run Linkage Review v0
Phase 19  - Agent-run Lifecycle v0
Phase 20  - Persisted Child Record Agent-run Linkage v0
Phase 21  - Dashboard Parent/Child Provenance Links v0
Phase 22  - Evidence Ledger Dashboard Table v0
Phase 22.5 - Evidence-to-gate/report Local Cross-links Review v0
Phase 23  - Single Workflow Parent Review v0
Phase 24  - WorkflowRun Schema v0
Phase 25  - WorkflowRun Metadata Persistence v0
Phase 26  - WorkflowRun Dashboard Table v0
Phase 27  - WorkflowRun Child-link Review v0
Phase 28  - Deterministic Workflow Execution Preview v0
Phase 29  - WorkflowRun Child-record Links v0
Phase 30  - WorkflowRun Child Inspection Surface v0
Phase 30.5 - Direct Evidence-to-gate/report Cross-link Review v0
Phase 31  - Workflow Stage Input Manifest v0
Phase 31.5 - Direct Cross-stage Link Schema Review v0
Phase 32  - Workflow Lineage Read Model v0
Phase 33  - Workflow Lineage Dashboard Links v0
Phase 33.5 - Workflow Lineage Missing-reference Review v0
Phase 34  - Workflow Lineage Missing-reference Test v0
Phase 34.5 - Workflow Lineage Boundary Hardening Review v0
Phase 35  - Workflow Lineage Manifest-shape Hardening v0
Phase 35.5 - Workflow Lineage Warning Taxonomy Review v0
Phase 36  - Structured Warning Taxonomy v0
Phase 36.5 - Workflow Lineage Warning Code Documentation Review v0
Phase 37  - Workflow Lineage Warning Code Runbook Example v0
Phase 37.5 - Workflow Lineage Warning Code Dashboard Review v0
Phase 38  - Workflow Lineage Warning Code Dashboard Surfacing v0
Phase 38.5 - Workflow Lineage Warning Code Dashboard Smoke Example v0
Phase 39  - Workflow Version Naming Review v0
Phase 40  - Workflow Version Naming Update v0
Phase 40.5 - Workflow Version Naming Smoke Example v0
Phase 41  - Workflow Version Naming Consistency Review v0
Phase 42  - Schema Default Workflow Version Update v0
Phase 42.5 - Schema Default Workflow Version Smoke Example v0
Phase 43  - Runtime DB Schema Default Verification v0
Phase 44  - Migration Runner Review v0
Phase 45  - Lightweight SQL Migration Runner v0
Phase 46  - Runtime Migration Runner Verification v0
Phase 47  - Migration Runner Fresh DB Verification v0
Phase 48  - Migration Runner Runbook Cleanup v0
Phase 49  - Fresh DB API Smoke Verification v0
Phase 50  - Application Evidence Index Refresh v0
Phase 51  - Failure-case Persistence Smoke Verification v0
Phase 52  - Failure-case Application Evidence Refresh v0
Phase 53  - Agent-run Failure Linkage Smoke Verification v0
Phase 54  - Agent-run Failure Linkage Application Refresh v0
Phase 55  - Workflow Failure Provenance Review v0
Phase 56  - Workflow Failure Linkage Smoke Verification v0
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

### Phase 18 - Dashboard Trace/Filter Links v0

Implemented outputs:

```text
GET /ops/dashboard trace lookup links
GET /ops/dashboard persisted record filter links
```

Phase 18 is a small inspectability improvement over existing metadata and persisted records. It does not add search, ranking, semantic retrieval, LLM calls, dashboard polish, or hosted observability.

### Phase 18.5 - Agent-run Linkage Review v0

Implemented outputs:

```text
docs/review/agent-run-linkage-review.md
```

Phase 18.5 is a review-only gate. It does not add migrations, endpoints, or runtime behavior. It keeps the direct `agent_run_id` foreign-key boundary explicit and concludes that the next implementation should create the agent run first before inserting child evidence, gate, or report records.

### Phase 19 - Agent-run Lifecycle v0

Implemented outputs:

```text
run_with_trace creates parent agent_runs row before operation execution
run_with_trace updates the same row to completed or failed
Repository.update_agent_run
```

Phase 19 changes trace lifecycle only. It does not add child-record `agent_run_id` foreign-key linkage, migrations for persisted evidence/gate/report records, distributed tracing, hosted observability, LLM calls, embeddings, or semantic retrieval.

### Phase 20 - Persisted Child Record Agent-run Linkage v0

Implemented outputs:

```text
agent_run_id on persisted Evidence Ledger entries
agent_run_id on persisted Noise Gate records
agent_run_id on persisted Report records
db/migrations/006_child_agent_run_ids.sql
trace lookup returns child records with parent agent_run_id
```

Phase 20 adds local parent/child linkage for persisted evidence, gate, and report records. It does not add distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, or a full multi-stage workflow parent table.

### Phase 21 - Dashboard Parent/Child Provenance Links v0

Implemented:

```text
parent run links on Noise Gate dashboard rows
parent run links on Report dashboard rows
dashboard boundary copy updated from missing agent_run_id linkage to local parent/child provenance
```

Phase 21 is a plain inspectability change. It does not add a polished UI, a new dashboard framework, distributed tracing, hosted observability, LLM calls, embeddings, or semantic retrieval.

### Phase 22 - Evidence Ledger Dashboard Table v0

Implemented:

```text
Evidence Ledger Records section in GET /ops/dashboard
trace lookup links for evidence rows
parent run links for evidence rows
status filter links for evidence rows
claim, evidence span, source, and confidence columns
```

Phase 22 is a plain inspectability change. It does not add dashboard polish, semantic evidence search, distributed tracing, hosted observability, LLM calls, embeddings, or new retrieval behavior.

### Phase 22.5 - Evidence-to-gate/report Local Cross-links Review v0

Implemented:

```text
docs/review/evidence-to-gate-report-cross-links-review.md
decision not to add cross-link columns in the review gate
future acceptance criteria for a single workflow parent before direct cross-stage links
```

Phase 22.5 is a review-only gate. It does not add migrations, columns, endpoints, dashboard behavior, LLM calls, embeddings, retrieval behavior, distributed tracing, hosted observability, or final report generation.

### Phase 23 - Single Workflow Parent Review v0

Implemented:

```text
docs/review/single-workflow-parent-review.md
decision not to reuse agent_runs as the workflow parent
future direction for a separate workflow_runs table
acceptance criteria for workflow-level provenance
```

Phase 23 is a review-only gate. It does not add migrations, a `workflow_runs` table, `workflow_run_id` columns, workflow execution endpoints, dashboard behavior, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, or final report generation.

### Phase 24 - WorkflowRun Schema v0

Implemented:

```text
workflow_runs table in db/init/001_schema.sql
db/migrations/007_workflow_runs.sql
schema-level workflow parent status boundary
```

Phase 24 is schema-only. It does not add `workflow_run_id` columns to child records, workflow execution endpoints, repository methods, dashboard behavior, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, or final report generation.

### Phase 25 - WorkflowRun Metadata Persistence v0

Implemented:

```text
POST /workflow-runs
GET /workflow-runs
WorkflowRun request/response schemas
PostgresRepository create/list methods for workflow_runs
```

Phase 25 is metadata-only. It does not add workflow orchestration, `workflow_run_id` columns to child records, evidence -> gate -> report execution, dashboard behavior, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, or final report generation.

### Phase 26 - WorkflowRun Dashboard Table v0

Implemented:

```text
GET /ops/dashboard workflow-run metadata table
metadata-only boundary copy for workflow runs
```

Phase 26 is visibility-only. It does not add workflow orchestration, `workflow_run_id` columns to child records, evidence -> gate -> report execution, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, or final report generation.

### Phase 27 - WorkflowRun Child-link Review v0

Implemented:

```text
docs/review/workflow-run-child-link-review.md
decision to defer child workflow_run_id columns until a workflow execution boundary exists
acceptance criteria for adding child workflow links later
```

Phase 27 is review-only. It does not add migrations, child columns, endpoints, dashboard behavior, workflow orchestration, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, or final report generation.

### Phase 28 - Deterministic Workflow Execution Preview v0

Implemented:

```text
POST /workflow-runs/execute-preview
parent workflow_runs row creation before deterministic execution
parent workflow_runs row completion/failure updates after execution
deterministic retrieval -> evidence -> gate -> report preview sequence
child records correlated by workflow_trace_id
```

Phase 28 is deterministic preview execution only. It did not add child `workflow_run_id` columns, direct evidence -> gate -> report foreign-key links, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation. Child workflow links were added later in Phase 29.

### Phase 29 - WorkflowRun Child-record Links v0

Implemented:

```text
db/migrations/008_child_workflow_run_ids.sql
nullable workflow_run_id on retrieval_runs
nullable workflow_run_id on evidence_ledger_entries
nullable workflow_run_id on noise_gate_records
nullable workflow_run_id on report_records
POST /workflow-runs/execute-preview attaches deterministic child records to its parent workflow run
```

Phase 29 is local workflow provenance only. It does not add direct evidence -> gate -> report foreign-key links, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

### Phase 30 - WorkflowRun Child Inspection Surface v0

Implemented:

```text
GET /workflow-runs/{id}
workflow-run detail response with linked retrieval runs
workflow-run detail response with linked Evidence Ledger records
workflow-run detail response with linked Noise Gate records
workflow-run detail response with linked Report records
summary counts for child records
```

Phase 30 is a read-only inspectability surface over existing local workflow child links. It does not add direct evidence -> gate -> report foreign-key links, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

### Phase 30.5 - Direct Evidence-to-gate/report Cross-link Review v0

Implemented:

```text
docs/review/direct-evidence-gate-report-cross-link-review.md
decision not to add direct evidence -> gate -> report foreign-key links in this review gate
acceptance criteria for proving downstream stages consumed persisted upstream row ids
next direction for a workflow stage input manifest
```

Phase 30.5 is a review-only gate. It does not add migrations, columns, endpoints, dashboard behavior, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 31:

```text
Workflow stage input manifest v0
```

### Phase 31 - Workflow Stage Input Manifest v0

Implemented:

```text
db/migrations/009_stage_input_manifest.sql
stage_input_manifest JSONB on noise_gate_records
stage_input_manifest JSONB on report_records
POST /workflow-runs/execute-preview records persisted Evidence Ledger row ids consumed by the Noise Gate preview
POST /workflow-runs/execute-preview records persisted Evidence Ledger row ids and persisted Noise Gate record id consumed by the Report preview
GET /workflow-runs/{id} returns those manifests with linked child records
GET /ops/dashboard exposes those manifests in plain Noise Gate and Report record rows
```

Phase 31 is local stage input provenance for deterministic preview rows. It does not add direct evidence -> gate -> report foreign-key links, join tables, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 31.5:

```text
Direct cross-stage link schema review v0
```

### Phase 31.5 - Direct Cross-stage Link Schema Review v0

Implemented:

```text
docs/review/direct-cross-stage-link-schema-review.md
decision not to add direct evidence -> gate -> report foreign-key links yet
decision not to add join tables yet
decision to prefer a derived workflow lineage read model before new storage
```

Phase 31.5 is a review-only gate. It does not add migrations, columns, join tables, endpoints, dashboard behavior, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 32:

```text
Workflow lineage read model v0
```

### Phase 32 - Workflow Lineage Read Model v0

Implemented:

```text
GET /workflow-runs/{id}/lineage
derived read model over existing workflow child records and stage_input_manifest values
Noise Gate input Evidence Ledger ids resolved to linked Evidence Ledger records
Report input Evidence Ledger ids resolved to linked Evidence Ledger records
Report input Noise Gate record id resolved to the linked Noise Gate record
missing manifest references surfaced as response warnings and summary counts
```

Phase 32 does not add migrations, columns, join tables, direct evidence -> gate -> report foreign-key links, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 33:

```text
Workflow lineage dashboard links v0
```

### Phase 33 - Workflow Lineage Dashboard Links v0

Implemented:

```text
detail and lineage links from workflow rows in GET /ops/dashboard
detail links target GET /workflow-runs/{id}
lineage links target GET /workflow-runs/{id}/lineage
plain operations dashboard copy labels the lineage surface as a derived read model
```

Phase 33 is an inspectability change only. It adds no dashboard polish, frontend framework, migrations, columns, join tables, direct evidence -> gate -> report foreign-key links, distributed tracing, hosted observability, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 33.5:

```text
Workflow lineage missing-reference review v0
```

### Phase 33.5 - Workflow Lineage Missing-reference Review v0

Implemented:

```text
docs/review/workflow-lineage-missing-reference-review.md
review of missing manifest reference behavior in GET /workflow-runs/{id}/lineage
decision not to add migrations, columns, join tables, foreign-key lineage, or runtime mutation paths
next direction for a targeted missing-reference test fixture
```

Phase 33.5 is a review-only gate. It adds no runtime behavior, migrations, columns, join tables, direct evidence -> gate -> report foreign-key links, malformed-manifest creation endpoint, repair endpoint, dashboard polish, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 34:

```text
Workflow lineage missing-reference test v0
```

### Phase 34 - Workflow Lineage Missing-reference Test v0

Implemented:

```text
targeted missing-reference fixture in apps/api/tests/test_routes.py
GET /workflow-runs/{id}/lineage test with deliberately broken stage_input_manifest values
assertion that missing_reference_count > 0
assertions for missing_evidence_entry_ids and missing_noise_gate_record_id
workflow version phase34-workflow-lineage-missing-reference-test
```

Phase 34 proves missing-reference surfacing in the existing derived lineage read model. It adds no malformed-manifest mutation endpoint, repair endpoint, migrations, columns, join tables, direct evidence -> gate -> report foreign-key links, dashboard polish, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 34.5:

```text
Workflow lineage boundary hardening review v0
```

### Phase 34.5 - Workflow Lineage Boundary Hardening Review v0

Implemented:

```text
docs/review/workflow-lineage-boundary-hardening-review.md
review of non-list manifest values for input_evidence_ledger_entry_ids
review of duplicate references and cross-workflow references
decision to harden manifest-shape parsing before adding schema
```

Phase 34.5 is a review-only gate. It adds no runtime behavior, migrations, columns, join tables, malformed-manifest mutation endpoint, repair endpoint, dashboard polish, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 35:

```text
Workflow lineage manifest-shape hardening v0
```

### Phase 35 - Workflow Lineage Manifest-shape Hardening v0

Implemented:

```text
GET /workflow-runs/{id}/lineage ignores non-list input_evidence_ledger_entry_ids values
invalid manifest shape warning: input_evidence_ledger_entry_ids must be a list
cross-workflow references remain local missing references
duplicate manifest references preserve order and count
workflow version phase35-workflow-lineage-manifest-shape-hardening
```

Phase 35 hardens the existing derived lineage read model. It adds no migrations, columns, or join tables. It also adds no direct evidence -> gate -> report foreign-key links, malformed-manifest mutation endpoint, repair endpoint, dashboard polish, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 35.5:

```text
Workflow lineage warning taxonomy review v0
```

### Phase 35.5 - Workflow Lineage Warning Taxonomy Review v0

Implemented:

```text
docs/review/workflow-lineage-warning-taxonomy-review.md
warning categories reviewed before API shape changes
derived_read_model_boundary
missing_manifest_reference
invalid_manifest_shape
local_workflow_scope
decision to keep warning strings human-readable in this review gate
```

Phase 35.5 is a review-only gate. It adds no runtime behavior, migrations, columns, join tables, warning enum field, direct evidence -> gate -> report foreign-key links, malformed-manifest mutation endpoint, repair endpoint, dashboard polish, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 36:

```text
structured warning taxonomy v0
```

### Phase 36 - Structured Warning Taxonomy v0

Implemented:

```text
GET /workflow-runs/{id}/lineage returns warning_codes
existing warnings strings remain human-readable
derived_read_model_boundary
local_workflow_scope
missing_manifest_reference
invalid_manifest_shape
workflow version phase36-structured-warning-taxonomy
```

Phase 36 exposes a machine-readable warning taxonomy on the existing lineage response. It adds no migrations, columns, or join tables. It also adds no warning enum table, stored warning-code records, direct evidence -> gate -> report foreign-key links, malformed-manifest mutation endpoint, repair endpoint, dashboard polish, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 36.5:

```text
workflow lineage warning code documentation review v0
```

### Phase 36.5 - Workflow Lineage Warning Code Documentation Review v0

Implemented:

```text
Workflow lineage warning code documentation review v0
docs/review/workflow-lineage-warning-code-documentation-review.md
documentation boundary for warning_codes
human-readable warnings remain canonical for readers
warning code meaning table
decision to avoid runtime behavior in the review gate
```

Phase 36.5 is a review-only gate. It adds no runtime behavior, migrations, columns, join tables, warning-code persistence, warning-code enum table, dashboard rendering change, mutation endpoint, repair endpoint, direct evidence -> gate -> report foreign-key links, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 37:

```text
workflow lineage warning code runbook example v0
```

### Phase 37 - Workflow Lineage Warning Code Runbook Example v0

Implemented:

```text
Expected /workflow-runs/{id}/lineage response shape in docs/runbook.md
warnings and warning_codes shown together
derived_read_model_boundary
local_workflow_scope
response-level taxonomy only boundary
```

Phase 37 is a documentation gate. It adds no runtime behavior, migrations, columns, or join tables. It also adds no warning-code persistence, warning-code enum table, dashboard rendering change, mutation endpoint, repair endpoint, direct evidence -> gate -> report foreign-key links, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 37.5:

```text
workflow lineage warning code dashboard review v0
```

### Phase 37.5 - Workflow Lineage Warning Code Dashboard Review v0

Implemented:

```text
Workflow lineage warning code dashboard review v0
docs/review/workflow-lineage-warning-code-dashboard-review.md
dashboard boundary for warning_codes
decision to avoid dashboard rendering in the review gate
next direction for warning code dashboard surfacing v0
```

Phase 37.5 is a review-only gate. It adds no runtime behavior, dashboard rendering, migrations, columns, or join tables. It also adds no warning-code persistence, warning-code enum table, mutation endpoint, repair endpoint, direct evidence -> gate -> report foreign-key links, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 38:

```text
workflow lineage warning code dashboard surfacing v0
```

### Phase 38 - Workflow Lineage Warning Code Dashboard Surfacing v0

Implemented:

```text
Lineage warning codes legend in GET /ops/dashboard
derived_read_model_boundary
local_workflow_scope
missing_manifest_reference
invalid_manifest_shape
response-level taxonomy only boundary
not persisted dashboard analytics boundary
```

Phase 38 is a small dashboard surfacing gate. It adds no migrations, columns, or join tables. It also adds no warning-code persistence, warning-code enum table, dashboard analytics, mutation endpoint, repair endpoint, direct evidence -> gate -> report foreign-key links, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 38.5:

```text
workflow lineage warning code dashboard smoke example v0
```

### Phase 38.5 - Workflow Lineage Warning Code Dashboard Smoke Example v0

Implemented:

```text
Expected /ops/dashboard warning-code legend in docs/runbook.md
Lineage warning codes
derived_read_model_boundary
local_workflow_scope
missing_manifest_reference
invalid_manifest_shape
not persisted dashboard analytics boundary
```

Phase 38.5 is a documentation gate. It adds no runtime behavior, dashboard rendering changes, migrations, columns, or join tables. It also adds no warning-code persistence, warning-code enum table, dashboard analytics, mutation endpoint, repair endpoint, direct evidence -> gate -> report foreign-key links, LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 39:

```text
workflow version naming review v0
```

### Phase 39 - Workflow Version Naming Review v0

Implemented:

```text
docs/review/workflow-version-naming-review.md
review of current workflow_version value
phase36-structured-warning-taxonomy was the reviewed runtime value before Phase 40
decision to avoid runtime rename in the review gate
next direction for workflow version naming update v0
```

Phase 39 is a review-only gate. It adds no runtime behavior, `workflow_version` rename, migrations, columns, join tables, trace schema changes, dashboard rendering changes, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

Follow-up implemented by Phase 40:

```text
workflow version naming update v0
```

### Phase 40 - Workflow Version Naming Update v0

Implemented:

```text
runtime workflow_version renamed to phase40-lineage-warning-code-dashboard
app settings default updated
AgentRunCreate default updated
WorkflowRunCreate default updated
route test constant updated
runbook examples updated
```

Phase 40 updates the runtime identifier and examples only. It adds no workflow semantics, migrations, columns, join tables, trace schema changes, dashboard rendering changes, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 40.5 - Workflow Version Naming Smoke Example v0

Goal:

```text
show the expected workflow-version marker in simple smoke checks after the runtime rename
```

Implemented:

```text
workflow version naming smoke example v0
docs/runbook.md expected workflow-version smoke checks
/health expected workflow_version example
/ops/summary expected workflow_version example
README status entry
```

Phase 40.5 documents how a reviewer should see `phase40-lineage-warning-code-dashboard` on the smallest service surfaces. It changes no runtime behavior, workflow semantics, migrations, columns, join tables, trace schema, dashboard rendering, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 41 - Workflow Version Naming Consistency Review v0

Goal:

```text
review whether the renamed runtime workflow_version is consistent across runtime, docs, tests, and executable schema defaults
```

Implemented:

```text
docs/review/workflow-version-naming-consistency-review.md
runtime-facing workflow_version surfaces reviewed
stale schema defaults identified
```

Phase 41 is a review-only gate. It identifies that `db/init/001_schema.sql` and `db/migrations/007_workflow_runs.sql` still contain older executable schema defaults. It changes no runtime behavior, schema defaults, migrations, columns, join tables, trace schema, dashboard rendering, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 42 - Schema Default Workflow Version Update v0

Goal:

```text
make fresh database init and forward migrations default to the current workflow_version marker
```

Implemented:

```text
db/init/001_schema.sql fresh defaults updated
db/migrations/010_workflow_version_defaults.sql forward migration added
schema default workflow version update v0
```

Do not rewrite historical migration 007. It remains historical context for when the `workflow_runs` table was introduced. Current executable schema defaults are updated by fresh init SQL and the new forward migration.

Phase 42 changes only executable schema defaults for omitted `workflow_version` values. It adds no workflow semantics, columns, join tables, trace schema changes, dashboard rendering changes, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 42.5 - Schema Default Workflow Version Smoke Example v0

Goal:

```text
document the SQL smoke check for current workflow_version schema defaults
```

Implemented:

```text
docs/runbook.md expected schema-default workflow-version smoke checks
```

Phase 42.5 documents how a reviewer can inspect PostgreSQL defaults for `agent_runs.workflow_version` and `workflow_runs.workflow_version`. It proves schema defaults only; it adds no runtime behavior, workflow semantics, migrations, columns, join tables, trace schema changes, dashboard rendering changes, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 43 - Runtime DB Schema Default Verification v0

Goal:

```text
verify the local Docker DB schema defaults and record before/after migration evidence
```

Implemented:

```text
docs/review/runtime-db-schema-default-verification.md
Docker DB started healthy on local port 55432
pre-migration stale defaults recorded
db/migrations/010_workflow_version_defaults.sql applied to the running DB
post-migration defaults verified as phase40-lineage-warning-code-dashboard
```

Phase 43 records that the existing Docker volume carried stale defaults until migration 010 was applied. No volume deletion was performed. This changes no repo runtime behavior, columns, join tables, trace schema, dashboard rendering, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 44 - Migration Runner Review v0

Goal:

```text
decide whether migration handling should remain manual, adopt Alembic, or add a small SQL migration runner
```

Implemented:

```text
docs/review/migration-runner-review.md
runbook-only psql piping reviewed
Alembic reviewed as too large for the current phase
lightweight SQL migration runner selected as the next bounded implementation
```

Phase 44 is a review-only gate. It adds no migration runner, schema tables, columns, endpoints, dashboard rendering, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 45 - Lightweight SQL Migration Runner v0

Goal:

```text
add the smallest inspectable runner for existing SQL migration files
```

Implemented:

```text
apps/api/app/migration_runner.py
schema_migrations table creation by the runner
sorted db/migrations/*.sql discovery
checksum and byte-count drift checks
--status mode
--baseline mode
default apply-pending mode
unit tests for discovery, planning, drift checks, and schema_migrations SQL
```

No Alembic dependency was added. The runner reuses existing SQL files and `DATABASE_URL`. It is not a production migration platform; it is a local inspectability tool that fails loudly on SQL errors and records applied filenames, checksums, byte counts, and timestamps.

Phase 45 adds no API endpoint, dashboard rendering, workflow execution semantics, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 46 - Runtime Migration Runner Verification v0

Goal:

```text
verify the lightweight migration runner against the local Docker DB
```

Implemented:

```text
docs/review/runtime-migration-runner-verification.md
initial --status showed 0 applied and 9 pending migrations
--baseline recorded 9 existing migrations without executing SQL
final --status showed 9 applied and 0 pending migrations
```

Phase 46 verifies baseline/status behavior for an existing local DB that already contained migration effects. It adds no runner behavior, API endpoint, dashboard rendering, workflow execution semantics, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 47 - Migration Runner Fresh DB Verification v0

Goal:

```text
verify that the lightweight migration runner can apply pending SQL files on an isolated fresh Docker DB
```

Implemented:

```text
docs/review/migration-runner-fresh-db-verification.md
isolated Compose project noiseproof-agent-fresh on POSTGRES_PORT=55433
initial --status showed 0 applied and 9 pending migrations
default runner apply command applied all 9 migrations
final --status showed 9 applied and 0 pending migrations
schema_migrations contained all 9 migration filenames
workflow_version schema defaults verified as phase40-lineage-warning-code-dashboard
isolated test volume was removed after verification
```

Phase 47 verifies the apply path for a local fresh DB. It adds no migration runner behavior, rollback support, production migration orchestration, hosted deployment safety, API endpoint, dashboard rendering, workflow execution semantics, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 48 - Migration Runner Runbook Cleanup v0

Goal:

```text
make the runbook runner-first and demote manual SQL piping to an emergency/debug fallback
```

Implemented:

```text
Default path: use the migration runner
Fresh or reset local DB runner sequence
Existing already-migrated local DB without schema_migrations runner sequence
Do not use --baseline on a fresh DB
manual SQL piping is a legacy/debug fallback
```

Phase 48 changes only documentation ordering and boundary language. It adds no migration runner behavior, rollback support, production migration orchestration, hosted deployment safety, API endpoint, dashboard rendering, workflow execution semantics, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 49 - Fresh DB API Smoke Verification v0

Goal:

```text
verify that a fresh migrated Docker DB can serve the smallest API persistence path
```

Implemented:

```text
docs/review/fresh-db-api-smoke-verification.md
isolated Compose project noiseproof-agent-api-smoke on POSTGRES_PORT=55435
migration runner applied 9 pending migrations before API start
temporary API served GET /health on port 8018
temporary API served GET /ops/summary before and after document creation
temporary API served POST /documents and GET /documents
Sample fresh DB smoke document persisted and was listed
isolated test volume was removed after verification
```

Phase 49 verifies a local API smoke path against a fresh migrated Docker DB. It adds no API features, migration runner behavior, rollback support, production migration orchestration, hosted deployment safety, dashboard polish, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 50 - Application Evidence Index Refresh v0

Goal:

```text
make application-facing docs point to the newest local runtime evidence without claiming product completion
```

Implemented:

```text
docs/application/portfolio-index.md includes migration runner and fresh DB API smoke artifacts
docs/application/braincrew-role-map.md includes local runtime proof surfaces
docs/review/application-ready-review.md includes local migration/API smoke evidence
hosted deployment evidence remains explicitly unclaimed
```

Phase 50 changes only application-facing evidence indexes and claim boundaries. It adds no runtime behavior, API endpoint, schema, migration runner behavior, dashboard rendering, hosted deployment evidence, production migration orchestration, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 51 - Failure-case Persistence Smoke Verification v0

Goal:

```text
verify that failure cases can be persisted and listed on a fresh migrated Docker DB
```

Implemented:

```text
docs/review/failure-case-persistence-smoke-verification.md
isolated Compose project noiseproof-agent-failure-smoke on POSTGRES_PORT=55436
migration runner applied 9 pending migrations before API start
temporary API served GET /health on port 8019
temporary API served POST /failure-cases and GET /failure-cases
parser_timeout failure record persisted with root_cause simulated parser timeout
GET /ops/summary failure_case_count moved from 0 to 1
isolated test volume was removed after verification
```

Phase 51 verifies a local failure-ledger persistence path against a fresh migrated Docker DB. It adds no automatic failure detection, production incident handling, hosted deployment evidence, distributed tracing, external observability, LLM-backed failure analysis, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 52 - Failure-case Application Evidence Refresh v0

Goal:

```text
make the failure-case persistence smoke artifact visible in application-facing docs without claiming automatic failure detection
```

Implemented:

```text
docs/application/portfolio-index.md includes the failure-case persistence smoke artifact
docs/application/braincrew-role-map.md includes failure-ledger proof surface and boundary language
docs/review/application-ready-review.md includes failure-case persistence smoke evidence
automatic failure detection remains explicitly unclaimed
```

Phase 52 changes only application-facing evidence indexes and claim boundaries. It adds no runtime behavior, API endpoint, schema, dashboard rendering, automatic failure detection, hosted deployment evidence, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 53 - Agent-run Failure Linkage Smoke Verification v0

Goal:

```text
verify that a failure case can carry agent_run_id linkage to a persisted failed agent run on a fresh migrated Docker DB
```

Implemented:

```text
docs/review/agent-run-failure-linkage-smoke-verification.md
isolated Compose project noiseproof-agent-failure-link-smoke on POSTGRES_PORT=55437
migration runner applied 9 pending migrations before API start
temporary API served POST /agent-runs and GET /agent-runs
temporary API served POST /failure-cases and GET /failure-cases
linked_parser_timeout failure record retained the created agent_run_id
GET /ops/summary returned agent_run_count 1 and failure_case_count 1
isolated test volume was removed after verification
```

Phase 53 verifies local `agent_run_id` linkage for manually created failure cases on a fresh migrated Docker DB. It adds no automatic failure detection, complete workflow failure causality, repair automation, hosted deployment evidence, distributed tracing, external observability, LLM-backed failure analysis, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 54 - Agent-run Failure Linkage Application Refresh v0

Goal:

```text
make linked failure-case proof visible in application-facing docs without claiming automatic detection or complete workflow failure causality
```

Implemented:

```text
docs/application/portfolio-index.md includes the agent-run failure linkage smoke artifact
docs/application/braincrew-role-map.md includes linked failure-case proof and boundary language
docs/review/application-ready-review.md includes agent-run failure linkage smoke evidence
complete workflow failure causality remains explicitly unclaimed
```

Phase 54 changes only application-facing evidence indexes and claim boundaries. It adds no runtime behavior, API endpoint, schema, dashboard rendering, automatic failure detection, complete workflow failure causality, hosted deployment evidence, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 55 - Workflow Failure Provenance Review v0

Goal:

```text
review whether operation-level failure linkage is enough to add workflow-level failure causality links
```

Implemented:

```text
docs/review/workflow-failure-provenance-review.md
operation-level failure linkage reviewed
workflow-level failure causality kept unclaimed
workflow_run_id on failure_cases deferred
automatic failure detection deferred
next bounded direction identified as workflow failure linkage smoke verification v0
```

Phase 55 is a review-only gate. It adds no runtime behavior, API endpoint, schema, migration, dashboard rendering, `workflow_run_id` column on `failure_cases`, automatic failure detection, complete workflow failure causality, repair automation, hosted deployment evidence, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

### Phase 56 - Workflow Failure Linkage Smoke Verification v0

Goal:

```text
verify that the deterministic workflow preview marks its parent workflow as failed when a downstream stage raises
```

Implemented:

```text
docs/review/workflow-failure-linkage-smoke-verification.md
tests/test_routes.py workflow failure fixture
workflow_run.status = failed
workflow_run.error_message records the stage exception
workflow_run.trace_json.error_type records RuntimeError
retrieval child record remains linked to the failed workflow parent
failure_cases remain unchanged
```

Phase 56 is a test-fixture smoke gate. It adds no runtime behavior, API endpoint, schema, migration, dashboard rendering, `workflow_run_id` column on `failure_cases`, automatic failure detection, fresh Docker DB evidence, production incident handling, complete workflow failure causality, hosted deployment evidence, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

Next recommended implementation phase:

```text
workflow failure linkage application refresh v0
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
