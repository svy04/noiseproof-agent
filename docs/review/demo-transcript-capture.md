# Demo Transcript Capture

Status: self-authored demo transcript gate.

Phase marker: demo transcript capture v0.

Label: Demo transcript capture.

This artifact captures a reader-facing route walkthrough for NoiseProof Agent after the public portfolio proof surface went live.

The goal is not to prove production readiness. The goal is to show a compact, inspectable path through the current local API surfaces:

```text
collection planning -> deterministic workflow preview -> lineage read model -> operations dashboard
```

## Capture Method

The transcript was captured with FastAPI `TestClient` against the current local route layer.

Representative command:

```text
cd apps/api
uv run python -c "<route capture script using tests.test_routes.make_client>"
```

This is route-level demo evidence. It is not a hosted demo, not external reviewer feedback, not customer validation, not production RAG evidence, and not semantic retrieval evidence.

## Scenario

Question:

```text
Which segment had enterprise demand growth and what evidence supports it?
```

Sources:

```text
market-note-001:
Enterprise segment demand growth was 12 percent in 2026. Consumer demand was flat.

analyst-note-contradiction:
A later analyst note says enterprise demand growth slowed in Q4 and the claim needs updated data.
```

Additional guardrail question:

```text
Should I buy NVDA after this AI infrastructure demand report?
```

## Transcript

### GET /health

Observed:

```json
{
  "status": "ok",
  "service": "noiseproof-agent-api",
  "workflow_version": "phase40-lineage-warning-code-dashboard"
}
```

### POST /collection-plans/preview

Input:

```json
{
  "question": "Should I buy NVDA after this AI infrastructure demand report?"
}
```

Observed excerpt:

```json
{
  "required_roles": [
    "direct_support",
    "contradiction",
    "timeline_anchor",
    "missing_data_signal",
    "user_intent_check",
    "scope_boundary"
  ],
  "stop_conditions": [
    "only same-source repeated narrative found",
    "no contradiction or missing-data signal found",
    "question drifts into buy/sell advice or target price recommendation"
  ],
  "warnings": [
    "Collection Plan Preview does not judge truth or retrieve evidence.",
    "This plan only defines information roles needed before retrieval.",
    "NoiseProof does not provide buy/sell recommendations or financial advice"
  ]
}
```

What this supports:

- buy/sell drift is surfaced before retrieval and report generation
- `user_intent_check` is present
- the route plans information needs; it does not judge truth

### POST /workflow-runs/execute-preview

Input excerpt:

```json
{
  "question": "Which segment had enterprise demand growth and what evidence supports it?",
  "strategy": "fixed-window",
  "sources": [
    {
      "source_id": "market-note-001",
      "source_type": "markdown",
      "content": "Enterprise segment demand growth was 12 percent in 2026. Consumer demand was flat."
    },
    {
      "source_id": "analyst-note-contradiction",
      "source_type": "markdown",
      "content": "A later analyst note says enterprise demand growth slowed in Q4 and the claim needs updated data."
    }
  ],
  "draft_claims": [
    "Enterprise segment demand growth was supported by current retrieved evidence."
  ]
}
```

Observed excerpt:

```json
{
  "execution_boundary": "deterministic_preview_only",
  "workflow_status": "completed",
  "retrieval_result_count": 2,
  "evidence_statuses": [
    "weakly_supported",
    "weakly_supported"
  ],
  "gate_decision": "needs_revision",
  "report_status": "needs_revision",
  "warnings": [
    "Workflow execution preview is deterministic and does not call an LLM.",
    "child records are attached to workflow_run_id while still carrying workflow_trace_id.",
    "stage input manifests record persisted upstream ids consumed by downstream preview stages.",
    "It does not perform semantic retrieval, embeddings, external search, or free-form final answer generation."
  ]
}
```

What this supports:

- a deterministic local workflow can create retrieval, evidence, gate, and report-preview child records
- weak evidence does not automatically become a final generated report
- the preview keeps LLM calls, embeddings, external search, semantic retrieval, and free-form final answer generation out of scope

### GET /workflow-runs/{id}/lineage

Observed excerpt:

```json
{
  "lineage_boundary": "derived_read_model_only",
  "summary": {
    "evidence_ledger_entry_count": 2,
    "noise_gate_record_count": 1,
    "report_record_count": 1,
    "gate_input_evidence_reference_count": 2,
    "report_input_evidence_reference_count": 2,
    "report_input_gate_reference_count": 1,
    "missing_reference_count": 0
  },
  "warning_codes": [
    "derived_read_model_boundary",
    "local_workflow_scope"
  ]
}
```

What this supports:

- the lineage read model can show which persisted evidence rows fed the gate and report preview
- this is a derived local read model, not distributed tracing

### GET /ops/dashboard

Observed excerpt:

```json
{
  "status_code": 200,
  "contains_workflow_runs": true,
  "contains_lineage_link": true
}
```

What this supports:

- the browser-readable operations surface exposes workflow runs and lineage links
- this is local operations visibility, not hosted production observability

## Allowed Claim

NoiseProof Agent has a self-authored local route demo transcript that walks a reviewer through collection planning, deterministic workflow execution preview, lineage, and the operations dashboard while preserving claim boundaries.

## Boundary

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not production RAG evidence.

This is not semantic retrieval, embeddings, or LLM evidence.

This is not market prediction quality evidence.

This is not Braincrew acceptance.

This is not automatic failure-case creation.

This is not complete workflow failure causality.

## Next Gate

The next evidence gate should stop adding self-authored proof unless it improves inspectability. Prefer one of:

```text
external reviewer feedback v0
local browser screenshot walkthrough v0
```

