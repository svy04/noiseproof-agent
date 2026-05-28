from fastapi import FastAPI

from app.routes import agent_runs, documents, failure_cases, health, ops


def create_app() -> FastAPI:
    app = FastAPI(
        title="NoiseProof Agent API",
        version="0.2.0",
        description="Day 2 service skeleton for metadata persistence and ops visibility.",
    )
    app.include_router(health.router)
    app.include_router(documents.router)
    app.include_router(agent_runs.router)
    app.include_router(failure_cases.router)
    app.include_router(ops.router)
    return app


app = create_app()
