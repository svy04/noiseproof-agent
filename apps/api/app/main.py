from fastapi import FastAPI

from app.routes import (
    agent_runs,
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
)


def create_app() -> FastAPI:
    app = FastAPI(
        title="NoiseProof Agent API",
        version="0.17.0",
        description="NoiseProof Agent phased API with collection planning, retrieval, and evidence boundaries.",
    )
    app.include_router(health.router)
    app.include_router(collection_plans.router)
    app.include_router(documents.router)
    app.include_router(agent_runs.router)
    app.include_router(retrieval_runs.router)
    app.include_router(evidence_ledgers.router)
    app.include_router(noise_gates.router)
    app.include_router(reports.router)
    app.include_router(traces.router)
    app.include_router(failure_cases.router)
    app.include_router(ops.router)
    return app


app = create_app()
