from fastapi import FastAPI

from app.routes import (
    agent_runs,
    chunks,
    collection_plans,
    documents,
    evidence_ledgers,
    failure_cases,
    health,
    noise_gates,
    ops,
    reports,
    retrieval_runs,
    traces,
    workflow_runs,
)
from app.services.trace_context import TRACE_CONTEXT_BOUNDARY, resolve_traceparent


def create_app() -> FastAPI:
    app = FastAPI(
        title="NoiseProof Agent API",
        version="0.33.0",
        description="NoiseProof Agent phased API with collection planning, retrieval, and evidence boundaries.",
    )

    @app.middleware("http")
    async def trace_context_header_middleware(request, call_next):
        traceparent, source = resolve_traceparent(request.headers.get("traceparent"))
        response = await call_next(request)
        response.headers["traceparent"] = traceparent
        response.headers["x-noiseproof-trace-source"] = source
        response.headers["x-noiseproof-trace-boundary"] = TRACE_CONTEXT_BOUNDARY
        return response

    app.include_router(health.router)
    app.include_router(collection_plans.router)
    app.include_router(documents.router)
    app.include_router(chunks.router)
    app.include_router(agent_runs.router)
    app.include_router(retrieval_runs.router)
    app.include_router(evidence_ledgers.router)
    app.include_router(noise_gates.router)
    app.include_router(reports.router)
    app.include_router(traces.router)
    app.include_router(workflow_runs.router)
    app.include_router(failure_cases.router)
    app.include_router(ops.router)
    return app


app = create_app()
