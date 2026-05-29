from dataclasses import asdict
import time

from packages.ingestion.retrieval import retrieve_candidates
from packages.ingestion.types import ChunkOptions, RetrievalSource

from app.db import Repository
from app.schemas import (
    RetrievalRunCreate,
    RetrievalRunRequest,
    RetrievalRunResponse,
)


def run_retrieval(
    payload: RetrievalRunRequest,
    repository: Repository,
) -> RetrievalRunResponse:
    started_at = time.perf_counter()
    experiment = retrieve_candidates(
        question=payload.question,
        sources=[
            RetrievalSource(
                source_id=source.source_id,
                source_type=source.source_type,
                content=source.content,
                filename=source.filename,
                source_uri=source.source_uri,
            )
            for source in payload.sources
        ],
        strategy=payload.strategy,
        top_k=payload.top_k,
        options=ChunkOptions(max_characters=payload.max_characters, overlap=payload.overlap),
    )
    latency_ms = max(0, round((time.perf_counter() - started_at) * 1000))
    status = "completed" if experiment.result_count else "no_results"
    run = repository.create_retrieval_run(
        RetrievalRunCreate(
            question=payload.question,
            strategy=payload.strategy,
            status=status,
            latency_ms=latency_ms,
            result_count=experiment.result_count,
            hit_rate=experiment.hit_rate,
            citation_coverage=experiment.citation_coverage,
            missing_evidence_count=experiment.missing_evidence_count,
            metadata_json={
                "source_count": len(payload.sources),
                "top_k": payload.top_k,
                "max_characters": payload.max_characters,
                "overlap": payload.overlap,
                "warning_count": len(experiment.warnings),
            },
        )
    )

    return RetrievalRunResponse(
        **run,
        results=[asdict(candidate) for candidate in experiment.results],
        warnings=experiment.warnings,
    )
