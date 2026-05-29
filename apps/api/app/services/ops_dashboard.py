from html import escape
from typing import Any

from app.schemas import OpsSummaryOut


def render_ops_dashboard(
    summary: OpsSummaryOut,
    agent_runs: list[dict[str, Any]],
    failure_cases: list[dict[str, Any]],
    retrieval_runs: list[dict[str, Any]],
) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>NoiseProof Operations Dashboard v0</title>
  <style>
    body {{ background: #0d0f10; color: #eceff1; font-family: ui-monospace, SFMono-Regular, Consolas, monospace; margin: 32px; }}
    h1, h2 {{ font-weight: 650; letter-spacing: 0; }}
    section {{ border-top: 1px solid #3a4045; margin-top: 24px; padding-top: 16px; }}
    table {{ border-collapse: collapse; width: 100%; margin-top: 12px; }}
    th, td {{ border: 1px solid #30363d; padding: 8px; text-align: left; vertical-align: top; }}
    th {{ color: #d7ff3f; font-weight: 600; }}
    .muted {{ color: #9aa4ad; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; }}
    .metric {{ border: 1px solid #30363d; padding: 12px; }}
  </style>
</head>
<body>
  <h1>Operations Dashboard v0</h1>
  <p class="muted">Phase 12 inspectable operations surface. No LLM calls, no new retrieval behavior, no persisted gate/report records.</p>
  <section>
    <h2>Summary</h2>
    <div class="grid">
      {_metric("Workflow", summary.workflow_version)}
      {_metric("Documents", summary.document_count)}
      {_metric("Agent Runs", summary.agent_run_count)}
      {_metric("Failure Cases", summary.failure_case_count)}
      {_metric("Unsupported Claims", summary.unsupported_claim_count)}
      {_metric("Contradictions", summary.contradiction_count)}
      {_metric("Average Latency", summary.average_latency_ms if summary.average_latency_ms is not None else "n/a")}
    </div>
  </section>
  <section>
    <h2>Recent Agent Runs</h2>
    {_agent_runs_table(agent_runs)}
  </section>
  <section>
    <h2>Failure Cases</h2>
    {_failure_cases_table(failure_cases)}
  </section>
  <section>
    <h2>Retrieval Runs</h2>
    {_retrieval_runs_table(retrieval_runs)}
  </section>
  <section>
    <h2>Boundary</h2>
    <ul>
      <li>This dashboard renders existing metadata and preview records only.</li>
      <li>Unsupported claim and contradiction counts come from persisted Evidence Ledger entries.</li>
      <li>Gate records, report records, embeddings, and semantic retrieval are still not implemented.</li>
      <li>Visual polish is intentionally deferred until failure behavior is more complete.</li>
    </ul>
  </section>
</body>
</html>"""


def _metric(label: str, value: object) -> str:
    return f'<div class="metric"><div class="muted">{escape(label)}</div><strong>{_cell(value)}</strong></div>'


def _agent_runs_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return '<p class="muted">No agent runs recorded yet.</p>'
    body = "\n".join(
        "<tr>"
        f"<td>{_cell(row.get('started_at'))}</td>"
        f"<td>{_cell(row.get('status'))}</td>"
        f"<td>{_cell(row.get('user_question'))}</td>"
        f"<td>{_cell(row.get('latency_ms'))}</td>"
        "</tr>"
        for row in rows[:10]
    )
    return f"<table><thead><tr><th>Started</th><th>Status</th><th>Question</th><th>Latency ms</th></tr></thead><tbody>{body}</tbody></table>"


def _failure_cases_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return '<p class="muted">No failure cases recorded yet.</p>'
    body = "\n".join(
        "<tr>"
        f"<td>{_cell(row.get('created_at'))}</td>"
        f"<td>{_cell(row.get('failure_type'))}</td>"
        f"<td>{_cell(row.get('description'))}</td>"
        f"<td>{_cell(row.get('fix_status'))}</td>"
        f"<td>{_cell(row.get('next_action'))}</td>"
        "</tr>"
        for row in rows[:10]
    )
    return f"<table><thead><tr><th>Created</th><th>Type</th><th>Description</th><th>Fix Status</th><th>Next Action</th></tr></thead><tbody>{body}</tbody></table>"


def _retrieval_runs_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return '<p class="muted">No retrieval runs recorded yet.</p>'
    body = "\n".join(
        "<tr>"
        f"<td>{_cell(row.get('created_at'))}</td>"
        f"<td>{_cell(row.get('status'))}</td>"
        f"<td>{_cell(row.get('question'))}</td>"
        f"<td>{_cell(row.get('strategy'))}</td>"
        f"<td>{_cell(row.get('result_count'))}</td>"
        f"<td>{_cell(row.get('missing_evidence_count'))}</td>"
        "</tr>"
        for row in rows[:10]
    )
    return f"<table><thead><tr><th>Created</th><th>Status</th><th>Question</th><th>Strategy</th><th>Results</th><th>Missing Evidence</th></tr></thead><tbody>{body}</tbody></table>"


def _cell(value: object) -> str:
    if value is None or value == "":
        return '<span class="muted">n/a</span>'
    return escape(str(value))
