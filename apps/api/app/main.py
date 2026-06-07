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
from app.services.trace_context import (
    TRACE_CONTEXT_BOUNDARY,
    reset_current_http_trace_context,
    resolve_traceparent,
    set_current_http_trace_context,
)
from app.services.otel_span_export import (
    LOCAL_OTEL_SPAN_EXPORT_BOUNDARY,
    build_otel_span_recorder,
)
from app.settings import Settings, get_settings


def create_app(settings: Settings | None = None) -> FastAPI:
    resolved_settings = settings or get_settings()
    app = FastAPI(
        title="NoiseProof Agent API",
        version="0.33.0",
        description="NoiseProof Agent phased API with collection planning, retrieval, and evidence boundaries.",
    )
    otel_span_recorder = build_otel_span_recorder(
        service_name=resolved_settings.service_name,
        enabled=resolved_settings.enable_otel_span_export,
    )
    app.state.otel_span_recorder = otel_span_recorder

    @app.middleware("http")
    async def trace_context_header_middleware(request, call_next):
        traceparent, source = resolve_traceparent(request.headers.get("traceparent"))
        token = set_current_http_trace_context(
            traceparent=traceparent,
            source=source,
            opentelemetry_span_export=otel_span_recorder.enabled,
            opentelemetry_span_export_boundary=(
                LOCAL_OTEL_SPAN_EXPORT_BOUNDARY
                if otel_span_recorder.enabled
                else None
            ),
        )
        with otel_span_recorder.request_span(
            method=request.method,
            path=request.url.path,
            traceparent=traceparent,
            trace_source=source,
        ) as span:
            try:
                response = await call_next(request)
                otel_span_recorder.finish_request_span(
                    span,
                    status_code=response.status_code,
                )
            finally:
                reset_current_http_trace_context(token)
        response.headers["traceparent"] = traceparent
        response.headers["x-noiseproof-trace-source"] = source
        response.headers["x-noiseproof-trace-boundary"] = TRACE_CONTEXT_BOUNDARY
        response.headers["x-noiseproof-otel-span-export"] = (
            "local_in_memory_enabled"
            if otel_span_recorder.enabled
            else "disabled_no_span_export"
        )
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
