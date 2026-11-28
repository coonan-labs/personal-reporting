"""Cleanup helpers for end-to-end pipeline tests."""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


def cleanup_e2e_pipeline(pipeline: Any) -> None:
    """Drop the remote test schema and always clear the local dlt pipeline state."""
    pipeline_name = getattr(pipeline, "pipeline_name", "unknown")
    primary_error: Exception | None = None
    try:
        with pipeline.sql_client() as client:
            # dlt's SQL client supplies the qualified, dev-mode dataset name.
            dataset_name = client.fully_qualified_dataset_name()
            client.execute_sql(f"DROP SCHEMA IF EXISTS {dataset_name} CASCADE")
    except Exception as exc:
        primary_error = exc
        raise RuntimeError(
            f"Failed to drop remote schema for pipeline {pipeline_name!r}: {exc}"
        ) from exc
    finally:
        # Pipeline.drop() resets local state only; it does not drop destination data.
        # Do not let a reset failure mask the primary schema-drop error.
        try:
            pipeline.drop()
        except Exception:
            if primary_error is None:
                raise
            logger.warning(
                "Failed to reset local dlt state for pipeline %r",
                pipeline_name,
                exc_info=True,
            )
