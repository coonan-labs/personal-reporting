"""Configuration and fixtures for DLT end-to-end tests.

This module configures the end-to-end testing environment with real external
services: MotherDuck (destination) and the source APIs.
"""

# base imports
import logging
import os
from collections.abc import Generator

# E2E loads into MotherDuck by default. Set E2E_TARGET=test-db to exercise
# the Databricks fallback path. Set the target before importing pipelines,
# which snapshots DBT_TARGET/DBT_SCHEMA/RAW_SCHEMA at import time.
E2E_TARGET = os.getenv("E2E_TARGET", "test-md")
if E2E_TARGET not in {"test-md", "test-db"}:
    raise RuntimeError(f"E2E_TARGET must be test-md or test-db (got {E2E_TARGET!r})")
os.environ["DBT_TARGET"] = E2E_TARGET
os.environ["DBT_SCHEMA"] = "reporting_test"
os.environ["RAW_SCHEMA"] = "raw_test"

import dlt  # noqa: E402

# PyPI imports
import pytest  # noqa: E402
from dlt.common.configuration.providers.google_secrets import GoogleSecretsProvider  # noqa: E402

from pipelines import SECRET_STORE  # noqa: E402
from pipelines.runner import get_destination  # noqa: E402
from tests.e2e.dlt.cleanup import cleanup_e2e_pipeline  # noqa: E402

logger = logging.getLogger(__name__)

# Only enable Google Secrets when the project uses that secret store. Enabling
# it unconditionally forces a GCP credential lookup even when 1Password (the
# default) supplies the credentials.
if SECRET_STORE == "google":
    os.environ["PROVIDERS__ENABLE_GOOGLE_SECRETS"] = "true"
    os.environ["PROVIDERS__GOOGLE_SECRETS__ONLY_SECRETS"] = "true"
    os.environ["PROVIDERS__GOOGLE_SECRETS__LIST_SECRETS"] = "true"
    os.environ["PROVIDERS__GOOGLE_SECRETS__ONLY_TOML_FRAGMENTS"] = "false"
else:
    os.environ["PROVIDERS__ENABLE_GOOGLE_SECRETS"] = "false"
os.environ["DLT_TELEMETRY_DISABLED"] = "1"


@pytest.fixture(scope="module", autouse=True)
def check_config():
    """Verify dlt configuration for end-to-end tests.

    Ensures that the Google Secrets provider is properly configured
    and available when Google Secrets are used for credential access.
    """
    # Google Cloud credentials are only required by the Google Secrets store.
    if SECRET_STORE == "google":
        assert os.path.exists(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

        # Get providers of dlt secrets
        providers = dlt.secrets.config_providers
        # Environment, Secrets.toml, Google Secrets
        assert len(providers) == 3
        # Allow direct value secrets (like Google Health refresh token)
        google_providers = [p for p in providers if isinstance(p, GoogleSecretsProvider)]
        assert google_providers[0].only_toml_fragments is False


@pytest.fixture(scope="class")
def e2e_pipeline() -> Generator[dlt.Pipeline, None, None]:
    """Pytest fixture providing a cloud pipeline for E2E testing.

    Creates a DLT pipeline using the destination selected by ``E2E_TARGET``:
    MotherDuck by default, or Databricks (``E2E_TARGET=test-db``) as a
    fallback. The pipeline is automatically cleaned up after each test class.

    Yields:
        dlt.Pipeline: Configured DLT pipeline for E2E testing.
    """
    # Test pipeline
    pipeline = dlt.pipeline(
        pipeline_name="live_e2e_test",
        destination=get_destination(E2E_TARGET),
        dataset_name="live_data",
        dev_mode=True,
    )
    logger.info(
        "Running pipeline: %s with dataset: %s",
        pipeline.pipeline_name,
        pipeline.dataset_name,
    )
    yield pipeline
    cleanup_e2e_pipeline(pipeline)
