import re

from packages.ingestion.chunking import compare_chunk_strategies
from packages.ingestion.selector import parse_document
from packages.ingestion.types import (
    ChunkOptions,
    ParseInput,
    RetrievalCandidate,
    RetrievalExperimentResult,
    RetrievalSource,
)

TERM_PATTERN = re.compile(r"[A-Za-z가-힣0-9][A-Za-z가-힣0-9_-]*")
STOP_TERMS = {
    "a",
    "an",
    "and",
    "are",
    "for",
    "had",
    "has",
    "in",
    "is",
    "of",
    "on",
    "or",
    "the",
    "to",
    "was",
    "what",
    "which",
}


def retrieve_candidates(
    question: str,
    sources: list[RetrievalSource],
    strategy: str,
    top_k: int = 5,
    options: ChunkOptions | None = None,
) -> RetrievalExperimentResult:
    query_terms = _terms(question)
    warnings: list[str] = []

    if not query_terms:
        warnings.append("Question produced no searchable terms.")

    candidates: list[RetrievalCandidate] = []
    for source in sources:
        parsed = parse_document(
            ParseInput(
                source_type=source.source_type,
                content=source.content,
                content_bytes=source.content_bytes,
                filename=source.filename,
                source_uri=source.source_uri,
            )
        )
        if parsed.failure_case_candidate is not None:
            warnings.append(
                f"Source {source.source_id} parse warning: {parsed.failure_case_candidate.failure_type}"
            )

        strategy_result = _select_strategy_result(
            compare_chunk_strategies(parsed, options or ChunkOptions()),
            strategy,
        )
        if strategy_result is None:
            warnings.append(f"Strategy '{strategy}' produced no chunks for source {source.source_id}.")
            continue

        for chunk in strategy_result.chunks:
            matched_terms = sorted(set(query_terms).intersection(_terms(chunk.text)))
            if not matched_terms:
                continue
            candidates.append(
                RetrievalCandidate(
                    source_id=source.source_id,
                    source_type=source.source_type,
                    chunk_strategy=strategy_result.strategy,
                    chunk_index=chunk.chunk_index,
                    text=chunk.text,
                    score=round(len(matched_terms) / max(len(set(query_terms)), 1), 4),
                    matched_terms=matched_terms,
                    metadata=chunk.metadata,
                )
            )

    ranked = sorted(
        candidates,
        key=lambda candidate: (candidate.score, len(candidate.matched_terms), -candidate.chunk_index),
        reverse=True,
    )[: max(1, top_k)]
    result_count = len(ranked)

    return RetrievalExperimentResult(
        question=question,
        strategy=strategy,
        results=ranked,
        result_count=result_count,
        missing_evidence_count=0 if result_count else 1,
        hit_rate=round(result_count / max(min(top_k, len(candidates) or top_k), 1), 4),
        citation_coverage=1.0 if result_count and all(candidate.source_id for candidate in ranked) else 0.0,
        warnings=warnings,
    )


def _select_strategy_result(strategy_results, strategy: str):
    for strategy_result in strategy_results:
        if strategy_result.strategy == strategy:
            return strategy_result
    return None


def _terms(text: str) -> list[str]:
    return [
        _normalize_term(term)
        for term in (match.group(0).lower() for match in TERM_PATTERN.finditer(text or ""))
        if len(term) > 1 and term not in STOP_TERMS
    ]


def _normalize_term(term: str) -> str:
    if term in {"grew", "grown", "growing"}:
        return "growth"
    return term
