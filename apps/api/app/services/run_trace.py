import time
from collections.abc import Callable
from typing import TypeVar
from uuid import UUID

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
    operation: Callable[[UUID], T],
    trace_from_result: Callable[[T], dict] | None = None,
) -> T:
    started_at = time.perf_counter()
    workflow_version = get_settings().workflow_version
    initial_trace = {
        "endpoint": endpoint,
        "phase": workflow_version,
        **trace_json,
    }
    agent_run = repository.create_agent_run(
        AgentRunCreate(
            user_question=user_question,
            workflow_version=workflow_version,
            status="running",
            trace_json=initial_trace,
        )
    )
    agent_run_id = agent_run["id"]
    try:
        result = operation(agent_run_id)
    except Exception as exc:
        latency_ms = _latency_ms(started_at)
        repository.update_agent_run(
            agent_run_id,
            status="failed",
            error_message=str(exc),
            latency_ms=latency_ms,
            trace_json={
                **initial_trace,
                "error_type": exc.__class__.__name__,
            },
        )
        raise

    latency_ms = _latency_ms(started_at)
    result_trace = trace_from_result(result) if trace_from_result is not None else {}
    repository.update_agent_run(
        agent_run_id,
        status="completed",
        error_message=None,
        latency_ms=latency_ms,
        trace_json={
            **initial_trace,
            **result_trace,
        },
    )
    return result


def _latency_ms(started_at: float) -> int:
    return max(0, round((time.perf_counter() - started_at) * 1000))
