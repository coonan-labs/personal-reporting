"""End-to-end tests for data loading pipelines.

This module contains integration tests that run the complete pipeline
from data extraction to loading into MotherDuck (or Databricks via
E2E_TARGET=test-db), using real external APIs
and cloud services.
"""

# e2e tests for pipelines

import dlt
import pytest

from tests.test_live_test_range import LIVE_REFRESH_ARGS

# label as end-to-end and disable response mock plugin
pytestmark = [pytest.mark.e2e]


class TestPipelines:
    """End-to-end test suite for all data loading pipelines.

    This class contains tests that verify complete pipeline functionality
    from source to destination using real external services.
    """

    # Narrow live window (7 days) shared with integration tests to keep
    # runtimes and API quota usage low.
    REFRESH_ARGS = LIVE_REFRESH_ARGS

    def test_notion_refresh(self, e2e_pipeline):
        """Test end-to-end refresh of the Notion habits pipeline.

        Args:
            e2e_pipeline: E2E pipeline fixture (MotherDuck by default, Databricks fallback).
        """
        # Delayed import to capture DBT target variable
        from pipelines.runner import refresh_pipeline

        # WHEN
        # Run the pipeline
        info = refresh_pipeline("notion", **self.REFRESH_ARGS, pipeline=e2e_pipeline)

        # THEN
        # Validate jobs were successful
        assert info.has_failed_jobs is False

    def test_hubspot_refresh(self, e2e_pipeline):
        """Test end-to-end refresh of the HubSpot CRM pipeline.

        Args:
            e2e_pipeline: E2E pipeline fixture (MotherDuck by default, Databricks fallback).
        """
        from pipelines.runner import refresh_pipeline

        # WHEN
        info = refresh_pipeline("hubspot", **self.REFRESH_ARGS, pipeline=e2e_pipeline)

        # THEN
        # Validate jobs were successful
        assert info.has_failed_jobs is False

    def test_google_health_refresh(self, e2e_pipeline):
        """Test end-to-end refresh of the Google health pipeline.

        Args:
            e2e_pipeline: E2E pipeline fixture (MotherDuck by default, Databricks fallback).
        """
        # Delayed import to capture DBT target variable
        from pipelines.runner import refresh_pipeline

        # GIVEN
        secrets = dlt.secrets
        # secrets.config_providers[2].only_toml_fragments = False
        secrets["sources.google_health.refresh_token"]

        # WHEN
        # Run the pipeline
        info = refresh_pipeline("google_health", **self.REFRESH_ARGS, pipeline=e2e_pipeline)

        # THEN
        # Validate jobs were successful
        assert info.has_failed_jobs is False
