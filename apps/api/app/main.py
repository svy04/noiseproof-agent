from fastapi import FastAPI

from app.routes import agent_runs, documents, failure_cases, health, ops, retrieval_runs


def create_app() -> FastAPI:
    app = FastAPI(
        title="NoiseProof Agent API",
        version="0.5.0",
        description="NoiseProof Agent phased API with profiling, parsing, chunking, and retrieval v0.",
    )
    app.include_router(health.router)
    app.include_router(documents.router)
    app.include_router(agent_runs.router)
    app.include_router(retrieval_runs.router)
    app.include_router(failure_cases.router)
    app.include_router(ops.router)
    return app


app = create_app()
