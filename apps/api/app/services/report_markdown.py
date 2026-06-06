from collections.abc import Mapping, Sequence
from typing import Any


REPORT_MARKDOWN_BOUNDARY = (
    "This markdown export is deterministic. It renders an existing persisted "
    "report record and does not generate new claims, call an LLM, run retrieval, "
    "create Evidence Ledger rows, or provide financial advice."
)


def render_report_record_markdown(record: Mapping[str, Any]) -> str:
    lines = [
        "# Claim-bounded Report",
        "",
        f"Report record id: {_value(record.get('id'))}",
        f"Workflow trace id: {_value(record.get('workflow_trace_id'))}",
        f"Status: {_value(record.get('status'))}",
        f"Gate decision: {_value(record.get('gate_decision'))}",
        f"Question: {_value(record.get('question'))}",
        "",
        f"Boundary: {REPORT_MARKDOWN_BOUNDARY}",
        "",
    ]

    manifest = record.get("stage_input_manifest")
    lines.extend(_render_stage_input_links(manifest))
    lines.extend(_render_local_inspection_paths(record, manifest))
    lines.extend(_render_source_retrieval_provenance(manifest))

    report = record.get("report")
    if isinstance(report, Mapping):
        lines.extend(_render_report(report))
    else:
        lines.extend(_render_no_report(record))

    lines.extend(_render_stage_input_manifest(record.get("stage_input_manifest")))
    lines.extend(_render_section("Warnings", record.get("warnings")))
    return "\n".join(lines).rstrip() + "\n"


def _render_report(report: Mapping[str, Any]) -> list[str]:
    lines = [
        "## Summary",
        "",
        _value(report.get("summary")),
        "",
        "## Claims",
        "",
    ]
    claims = report.get("claims") or []
    if not claims:
        lines.extend(["- None", ""])
    for index, claim in enumerate(claims, start=1):
        if not isinstance(claim, Mapping):
            continue
        lines.extend(
            [
                f"### Claim {index}",
                "",
                f"- Claim: {_value(claim.get('claim'))}",
                f"- Sources: {_join_values(claim.get('source_ids'))}",
                f"- Confidence: {_value(claim.get('confidence'))}",
                f"- Evidence: {_join_values(claim.get('evidence_spans'))}",
                f"- Limitations: {_join_values(claim.get('limitations'))}",
                f"- Contradictions: {_join_values(claim.get('contradictions'))}",
                "",
            ]
        )
    lines.extend(_render_section("Limitations", report.get("limitations")))
    lines.extend(_render_section("Contradictions", report.get("contradictions")))
    lines.extend(_render_section("Next Data Needed", report.get("next_data_needed")))
    return lines


def _render_no_report(record: Mapping[str, Any]) -> list[str]:
    lines = [
        "## Report",
        "",
        "No generated report body is stored for this record.",
        "",
    ]
    fallback = record.get("fallback_message")
    if fallback:
        lines.extend(["## Fallback Message", "", _value(fallback), ""])
    lines.extend(_render_section("Required Revisions", record.get("required_revisions")))
    return lines


def _render_stage_input_manifest(value: Any) -> list[str]:
    if not isinstance(value, Mapping) or not value:
        return ["## Stage Input Manifest", "", "- None", ""]
    lines = ["## Stage Input Manifest", ""]
    for key in sorted(value):
        item = value[key]
        if isinstance(item, Sequence) and not isinstance(item, str):
            lines.append(f"- {key}: {_join_values(item)}")
        else:
            lines.append(f"- {key}: {_value(item)}")
    lines.append("")
    return lines


def _render_stage_input_links(value: Any) -> list[str]:
    lines = ["## Stage Input Links", ""]
    if not isinstance(value, Mapping) or not value:
        lines.extend(["- None", ""])
        return lines

    rendered_any = False
    retrieval_run_id = value.get("retrieval_run_id")
    if retrieval_run_id:
        lines.append(f"- Retrieval run id: {_value(retrieval_run_id)}")
        rendered_any = True

    evidence_entry_ids = value.get("input_evidence_ledger_entry_ids")
    if isinstance(evidence_entry_ids, Sequence) and not isinstance(
        evidence_entry_ids, str
    ):
        for entry_id in evidence_entry_ids:
            lines.append(f"- Evidence Ledger entry id: {_value(entry_id)}")
            rendered_any = True

    noise_gate_record_id = value.get("input_noise_gate_record_id")
    if noise_gate_record_id:
        lines.append(f"- Noise Gate record id: {_value(noise_gate_record_id)}")
        rendered_any = True

    if not rendered_any:
        lines.append("- None")
    lines.append("")
    return lines


def _render_local_inspection_paths(
    record: Mapping[str, Any],
    manifest: Any,
) -> list[str]:
    lines = ["## Local Inspection Paths", ""]
    record_id = record.get("id")
    if record_id:
        lines.append(f"- Current report markdown: /reports/{_value(record_id)}/markdown")

    workflow_trace_id = record.get("workflow_trace_id")
    if workflow_trace_id:
        trace_id = _value(workflow_trace_id)
        lines.append(f"- Current report record: /reports?workflow_trace_id={trace_id}")
        lines.append(f"- Current workflow trace: /traces/{trace_id}")

    if isinstance(manifest, Mapping):
        if manifest.get("retrieval_run_id"):
            lines.append("- Retrieval runs: /retrieval-runs (match retrieval run id above)")
        evidence_entry_ids = manifest.get("input_evidence_ledger_entry_ids")
        if isinstance(evidence_entry_ids, Sequence) and not isinstance(
            evidence_entry_ids, str
        ):
            lines.append(
                "- Evidence Ledger entries: /evidence-ledgers "
                "(match Evidence Ledger entry ids above)"
            )
        if manifest.get("input_noise_gate_record_id"):
            lines.append(
                "- Noise Gate records: /noise-gates "
                "(match Noise Gate record id above)"
            )

    if len(lines) == 2:
        lines.append("- None")
    lines.append("")
    return lines


def _render_source_retrieval_provenance(value: Any) -> list[str]:
    lines = ["## Source Retrieval Provenance", ""]
    if not isinstance(value, Mapping) or not value:
        lines.extend(["- None", ""])
        return lines

    fields = [
        ("source_retrieval_mode", "Source retrieval mode"),
        ("source_query_vector_source", "Source query vector source"),
        ("source_is_semantic_retrieval_run", "Source is semantic retrieval run"),
        (
            "source_retrieval_persistence_boundary",
            "Source retrieval persistence boundary",
        ),
        (
            "handoff_performs_semantic_retrieval",
            "Handoff performs semantic retrieval",
        ),
    ]
    rendered_any = False
    for key, label in fields:
        if key in value:
            lines.append(f"- {label}: {_provenance_value(value.get(key))}")
            rendered_any = True
    if not rendered_any:
        lines.append("- None")
    lines.append("")
    return lines


def _render_section(title: str, value: Any) -> list[str]:
    lines = [f"## {title}", ""]
    if not value:
        lines.extend(["- None", ""])
        return lines
    if isinstance(value, Sequence) and not isinstance(value, str):
        lines.extend(f"- {_value(item)}" for item in value)
        lines.append("")
        return lines
    lines.extend([f"- {_value(value)}", ""])
    return lines


def _join_values(values: Any) -> str:
    if not values:
        return "None"
    if isinstance(values, Sequence) and not isinstance(values, str):
        return ", ".join(_value(value) for value in values) or "None"
    return _value(values)


def _value(value: Any) -> str:
    if value is None:
        return "None"
    return str(value)


def _provenance_value(value: Any) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    return _value(value)
