import time
from collections.abc import Callable
from typing import TypeVar

from app.db import Repository
from app.schemas import AgentRunCreate
from app.settings import get_settings


T = TypeVar("T")


def run_with_trace(
    repository: Repository,
    *,
    endpoint: str,
    user_question: str,
    trace_json: dict,
    operation: Callable[[], T],
    trace_from_result: Callable[[T], dict] | None = None,
) -> T:
    started_at = time.perf_counter()
    try:
        result = operation()
    except Exception as exc:
        latency_ms = _latency_ms(started_at)
        repository.create_agent_run(
            AgentRunCreate(
                user_question=user_question,
                workflow_version=get_settings().workflow_version,
                status="failed",
                error_message=str(exc),
                latency_ms=latency_ms,
                trace_json={
                    "endpoint": endpoint,
                    "phase": "phase11-auto-trace",
                    **trace_json,
                    "error_type": exc.__class__.__name__,
                },
            )
        )
        raise

    latency_ms = _latency_ms(started_at)
    result_trace = trace_from_result(result) if trace_from_result is not None else {}
    repository.create_agent_run(
        AgentRunCreate(
            user_question=user_question,
            workflow_version=get_settings().workflow_version,
            status="completed",
            latency_ms=latency_ms,
            trace_json={
                "endpoint": endpoint,
                "phase": "phase11-auto-trace",
                **trace_json,
                **result_trace,
            },
        )
    )
    return result


def _latency_ms(started_at: float) -> int:
    return max(0, round((time.perf_counter() - started_at) * 1000))
