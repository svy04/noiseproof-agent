import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class SemanticQualityChunk:
    chunk_id: str
    document_id: str
    source_type: str
    text: str
    information_roles: list[str]
    embedding: list[float] | None


@dataclass(frozen=True)
class SemanticQualityQuery:
    query_id: str
    question: str
    query_embedding: list[float]
    relevant_chunk_ids: list[str]
    information_roles: list[str]


@dataclass(frozen=True)
class SemanticQualityFixture:
    name: str
    embedding_model: str
    embedding_dimension: int
    no_embedding_generation: bool
    candidate_metrics: list[str]
    claim_boundary: str
    corpus: list[SemanticQualityChunk]
    queries: list[SemanticQualityQuery]
    qrels: dict[str, dict[str, int]]


def load_semantic_quality_fixture(path: Path | str) -> SemanticQualityFixture:
    root = Path(path)
    manifest = _read_json(root / "manifest.json")
    corpus_rows = _read_json(root / "corpus.json")
    query_rows = _read_json(root / "queries.json")

    corpus = [
        SemanticQualityChunk(
            chunk_id=row["chunk_id"],
            document_id=row["document_id"],
            source_type=row["source_type"],
            text=row["text"],
            information_roles=list(row.get("information_roles", [])),
            embedding=row.get("embedding"),
        )
        for row in corpus_rows
    ]
    queries = [
        SemanticQualityQuery(
            query_id=row["query_id"],
            question=row["question"],
            query_embedding=row["query_embedding"],
            relevant_chunk_ids=list(row.get("relevant_chunk_ids", [])),
            information_roles=list(row.get("information_roles", [])),
        )
        for row in query_rows
    ]
    fixture = SemanticQualityFixture(
        name=manifest["name"],
        embedding_model=manifest["embedding_model"],
        embedding_dimension=int(manifest["embedding_dimension"]),
        no_embedding_generation=bool(manifest["no_embedding_generation"]),
        candidate_metrics=list(manifest["candidate_metrics"]),
        claim_boundary=manifest["claim_boundary"],
        corpus=corpus,
        queries=queries,
        qrels={
            query_id: {chunk_id: int(score) for chunk_id, score in qrel.items()}
            for query_id, qrel in manifest["qrels"].items()
        },
    )
    _validate_fixture(fixture)
    return fixture


def summarize_semantic_quality_fixture(fixture: SemanticQualityFixture) -> dict[str, Any]:
    missing_embedding_chunk_ids = [
        chunk.chunk_id for chunk in fixture.corpus if chunk.embedding is None
    ]
    roles = sorted(
        {
            role
            for chunk in fixture.corpus
            for role in chunk.information_roles
        }.union(
            {
                role
                for query in fixture.queries
                for role in query.information_roles
            }
        )
    )
    return {
        "name": fixture.name,
        "query_count": len(fixture.queries),
        "chunk_count": len(fixture.corpus),
        "qrel_count": sum(len(qrel) for qrel in fixture.qrels.values()),
        "missing_embedding_chunk_ids": missing_embedding_chunk_ids,
        "information_roles": roles,
        "candidate_metrics": fixture.candidate_metrics,
        "claim_boundary": fixture.claim_boundary,
        "no_embedding_generation": fixture.no_embedding_generation,
    }


def _validate_fixture(fixture: SemanticQualityFixture) -> None:
    chunk_ids = {chunk.chunk_id for chunk in fixture.corpus}
    query_ids = {query.query_id for query in fixture.queries}

    for chunk in fixture.corpus:
        if chunk.embedding is not None and len(chunk.embedding) != fixture.embedding_dimension:
            raise ValueError(f"Chunk {chunk.chunk_id} embedding dimension mismatch.")

    for query in fixture.queries:
        if len(query.query_embedding) != fixture.embedding_dimension:
            raise ValueError(f"Query {query.query_id} embedding dimension mismatch.")
        missing_relevant = [chunk_id for chunk_id in query.relevant_chunk_ids if chunk_id not in chunk_ids]
        if missing_relevant:
            raise ValueError(f"Query {query.query_id} references missing chunks: {missing_relevant}")

    missing_query_qrels = [query_id for query_id in query_ids if query_id not in fixture.qrels]
    if missing_query_qrels:
        raise ValueError(f"Missing qrels for queries: {missing_query_qrels}")

    for query_id, qrel in fixture.qrels.items():
        if query_id not in query_ids:
            raise ValueError(f"Qrels reference missing query: {query_id}")
        missing_chunks = [chunk_id for chunk_id in qrel if chunk_id not in chunk_ids]
        if missing_chunks:
            raise ValueError(f"Qrels for {query_id} reference missing chunks: {missing_chunks}")


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))
