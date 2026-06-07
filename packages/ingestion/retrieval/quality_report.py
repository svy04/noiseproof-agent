from typing import Any

from packages.ingestion.retrieval.quality_fixture import SemanticQualityFixture


def build_semantic_quality_report(
    fixture: SemanticQualityFixture,
    evaluation: dict[str, Any],
) -> str:
    aggregate = evaluation["aggregate"]
    per_query = evaluation["per_query"]
    lines = [
        "# Semantic Retrieval Quality Report",
        "",
        "Phase marker: semantic retrieval quality report v0.",
        "",
        "This report records toy fixture metric output for semantic retrieval evaluation plumbing.",
        "",
        "It is not vector search quality evidence.",
        "",
        "## Fixture",
        "",
        f"- fixture: `{fixture.name}`",
        f"- queries: {len(fixture.queries)}",
        f"- corpus chunks: {len(fixture.corpus)}",
        f"- qrels: {sum(len(qrel) for qrel in fixture.qrels.values())}",
        f"- claim boundary: `{evaluation['claim_boundary']}`",
        "",
        "## Aggregate Metrics",
        "",
        "| Metric | Value |",
        "|---|---:|",
    ]
    for metric in [
        "Hit@k",
        "Recall@k",
        "MRR@k",
        "nDCG@k",
        "missing_embedding_rate",
        "semantic_vs_lexical_disagreement",
        "role_coverage_at_k",
    ]:
        lines.append(f"| {metric} | {_format_metric(aggregate.get(metric))} |")

    lines.extend(
        [
            "",
            "## Per-query Metrics",
            "",
            "| Query | Hit@k | Recall@k | MRR@k | nDCG@k | role_coverage_at_k |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for query in fixture.queries:
        metrics = per_query[query.query_id]
        lines.append(
            "| "
            + " | ".join(
                [
                    query.query_id,
                    _format_metric(metrics["Hit@k"]),
                    _format_metric(metrics["Recall@k"]),
                    _format_metric(metrics["MRR@k"]),
                    _format_metric(metrics["nDCG@k"]),
                    _format_metric(metrics["role_coverage_at_k"]),
                ]
            )
            + " |"
        )

    diagnostics = evaluation.get("per_query_diagnostics", {})
    if diagnostics:
        lines.extend(
            [
                "",
                "## Diagnostic Matrix",
                "",
                "This matrix explains fixture misses; it does not prove semantic retrieval quality.",
                "",
                "| Query | Semantic top-k | Missed relevant | Missing roles | Lexical rescue | Warnings |",
                "|---|---|---|---|---|---|",
            ]
        )
        for query in fixture.queries:
            query_diagnostics = diagnostics.get(query.query_id, {})
            lines.append(
                "| "
                + " | ".join(
                    [
                        query.query_id,
                        _format_list(query_diagnostics.get("semantic_top_k")),
                        _format_list(query_diagnostics.get("missed_relevant_chunk_ids")),
                        _format_list(query_diagnostics.get("missing_information_roles")),
                        _format_list(query_diagnostics.get("lexical_rescue_chunk_ids")),
                        _format_list(query_diagnostics.get("warnings")),
                    ]
                )
                + " |"
            )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This report intentionally uses a weak semantic ranking fixture so misses and disagreements remain visible.",
            "",
            "`q-what-missing` retrieves no relevant semantic candidate in this fixture. That is useful because it proves the evaluator can surface a missing-data failure instead of turning every semantic retrieval run into a success story.",
            "",
            f"`semantic_vs_lexical_disagreement = {_format_metric(aggregate.get('semantic_vs_lexical_disagreement'))}` means the toy semantic ranking and toy lexical ranking diverge strongly in this fixture. This is a warning signal, not a quality claim.",
            "",
            "## Boundary",
            "",
            "This is not embedding generation.",
            "",
            "This is not vector search quality evidence.",
            "",
            "This is not a benchmark result.",
            "",
            "This is not a model comparison.",
            "",
            "This is not Evidence Ledger generation.",
            "",
            "This is not hosted deployment evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def _format_metric(value: Any) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        text = f"{value:.4f}".rstrip("0").rstrip(".")
        return text or "0"
    return str(value)


def _format_list(value: Any) -> str:
    if not value:
        return "none"
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return str(value)
