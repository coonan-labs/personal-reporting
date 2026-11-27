"""Unit tests for the central pipeline runner and CLI interface."""

import dataclasses
from unittest.mock import ANY, MagicMock, patch

import pytest
from dlt.destinations import databricks, motherduck

from pipelines import RAW_SCHEMA
from pipelines.run_pipeline import main, parse_select
from pipelines.runner import (
    PIPELINE_CONFIG,
    get_databricks_staging_volume,
    get_destination,
    is_motherduck_target,
    normalize_motherduck_database,
    refresh_pipeline,
)


def test_parse_select():
    """Test the parse_select helper function."""
    assert parse_select(None) is None
    assert parse_select([]) is None
    assert parse_select([""]) is None

    # Simple list
    assert parse_select(["hubspot__contacts"]) == ["hubspot__contacts"]

    # Comma-separated strings
    assert parse_select(["hubspot__contacts,hubspot__companies"]) == [
        "hubspot__contacts",
        "hubspot__companies",
    ]

    # Repeated list items with whitespace
    assert parse_select(
        [" hubspot__contacts ,  hubspot__companies ", "  notion__daily_habits  "]
    ) == [
        "hubspot__contacts",
        "hubspot__companies",
        "notion__daily_habits",
    ]


@patch("pipelines.run_pipeline.refresh_pipeline")
def test_cli_main_success(mock_refresh):
    """Test that main succeeds with valid parameters."""
    mock_refresh.return_value = "Loaded 5 rows"

    # Test Notion full refresh with select
    code = main(["notion", "--select", "notion__data_sources", "--full"])
    assert code == 0
    mock_refresh.assert_called_once_with(
        "notion",
        is_incremental=False,
        initial_date=None,
        end_date=None,
        select=["notion__data_sources"],
    )

    mock_refresh.reset_mock()

    # Test HubSpot incremental refresh with custom date ranges
    code = main(
        [
            "hubspot",
            "--incremental",
            "--initial-date",
            "2023-01-01",
            "--end-date",
            "2023-12-31",
        ]
    )
    assert code == 0
    mock_refresh.assert_called_once_with(
        "hubspot",
        is_incremental=True,
        initial_date="2023-01-01",
        end_date="2023-12-31",
        select=None,
    )


def test_cli_main_unknown_pipeline():
    """Test that main returns 2 for unknown pipeline choice."""
    # Since argparse has choices defined, passing an invalid choice raises SystemExit / error
    with pytest.raises(SystemExit):
        main(["unknown_pipeline"])


@patch("pipelines.run_pipeline.refresh_pipeline")
def test_cli_main_exception(mock_refresh):
    """Test that main returns 1 on general exception."""
    mock_refresh.side_effect = ValueError("Some parsing error")
    code = main(["notion"])
    assert code == 1


@patch("pipelines.runner.dlt.secrets.get", return_value="workspace")
def test_get_databricks_staging_volume(mock_dlt_secrets_get):
    """Test that the staging volume derives from the target schema and catalog."""
    assert get_databricks_staging_volume("raw_test") == "workspace.raw_test.staging"


@patch("pipelines.runner.dlt.secrets.get", return_value="workspace")
@patch("pipelines.runner.dlt.pipeline")
@patch("pipelines.runner.validate_required_secrets")
def test_runner_refresh_pipeline(mock_validate, mock_dlt_pipeline, mock_dlt_secrets_get):
    """Test the centralized runner's refresh_pipeline and run_refresh dispatching."""
    mock_pipeline_instance = MagicMock()
    mock_dlt_pipeline.return_value = mock_pipeline_instance
    mock_pipeline_instance.run.return_value = "Loaded 10 rows"

    # Mocking the source factories so we don't query actual APIs
    mock_notion_source = MagicMock()
    mock_notion_source.with_resources.return_value = mock_notion_source

    with patch.dict(
        PIPELINE_CONFIG,
        {
            "notion": dataclasses.replace(
                PIPELINE_CONFIG["notion"],
                source_factory=MagicMock(return_value=mock_notion_source),
            )
        },
    ):
        config = PIPELINE_CONFIG["notion"]

        # Run refresh
        info = refresh_pipeline(
            "notion",
            is_incremental=True,
            initial_date="2024-01-01",
            end_date="2024-06-30",
            select=["notion__data_sources"],
        )

        assert info == "Loaded 10 rows"
        mock_validate.assert_called_once_with(
            secret_store="1password",  # defaults locally to 1password or google depending on environment
            required_secret_keys=["sources.notion.api_key"],
            pipeline_name="Notion Habits",
        )

        # Verify the source factory was called with correct db_name and date limits
        config.source_factory.assert_called_once()
        kwargs = config.source_factory.call_args[1]
        assert kwargs["db_name"] == "Disciplines"
        assert kwargs["initial_date"] == "2024-01-01"
        assert kwargs["end_date"] == "2024-06-30"

        # Verify resources selection
        mock_notion_source.with_resources.assert_called_once_with("notion__data_sources")

        # Verify dlt.pipeline creation and run
        mock_dlt_pipeline.assert_called_once_with(
            pipeline_name="notion_habits_pipeline",
            dataset_name=RAW_SCHEMA,
            destination=ANY,  # databricks factory asserted below
            progress="log",
        )
        destination = mock_dlt_pipeline.call_args.kwargs["destination"]
        assert isinstance(destination, databricks)
        assert destination.config_params["staging_volume_name"] == f"workspace.{RAW_SCHEMA}.staging"
        mock_pipeline_instance.run.assert_called_once_with(
            mock_notion_source,
            write_disposition=None,  # None for is_incremental=True as per get_write_disposition
            loader_file_format="parquet",
        )


@patch("pipelines.runner.dlt.secrets.get", return_value="workspace")
@patch("pipelines.runner.dlt.pipeline")
@patch("pipelines.runner.validate_required_secrets")
def test_runner_supports_direct_token_skips_secret_validation(
    mock_validate, mock_dlt_pipeline, mock_dlt_secrets_get
):
    """Test that supports_direct_token=True allows a direct access token to bypass secret validation."""
    mock_pipeline_instance = MagicMock()
    mock_dlt_pipeline.return_value = mock_pipeline_instance
    mock_pipeline_instance.run.return_value = "Loaded 5 rows"

    mock_source = MagicMock()

    def fake_source(*, access_token: str, **_kwargs):
        return mock_source

    with patch.dict(
        PIPELINE_CONFIG,
        {
            "google_health": dataclasses.replace(
                PIPELINE_CONFIG["google_health"],
                source_factory=fake_source,
                token_getter=MagicMock(return_value="direct-token"),
                supports_direct_token=True,
            )
        },
    ):
        # First call returns the direct token, second returns workspace for staging volume
        mock_dlt_secrets_get.side_effect = ["direct-token", "workspace"]

        info = refresh_pipeline("google_health", is_incremental=True)

        assert info == "Loaded 5 rows"
        # Secret validation should be skipped when a direct token is available
        mock_validate.assert_not_called()


@patch("pipelines.runner.dlt.secrets.get")
@patch("pipelines.runner.dlt.pipeline")
@patch("pipelines.runner.validate_required_secrets")
def test_runner_refresh_pipeline_uses_motherduck_destination_for_md_target(
    mock_validate, mock_dlt_pipeline, mock_dlt_secrets_get, monkeypatch
):
    """MotherDuck targets load via the motherduck destination, not Databricks."""
    monkeypatch.setattr("pipelines.runner.DBT_TARGET", "dev-md")
    monkeypatch.setattr("pipelines.runner.DBT_SCHEMA", "reporting_dev")
    monkeypatch.setattr("pipelines.runner.RAW_SCHEMA", "raw_dev")
    monkeypatch.setenv("MOTHERDUCK_TOKEN", "test-token")
    monkeypatch.delenv("DESTINATION__MOTHERDUCK__CREDENTIALS__DATABASE", raising=False)

    mock_pipeline_instance = MagicMock()
    mock_dlt_pipeline.return_value = mock_pipeline_instance
    mock_pipeline_instance.run.return_value = "Loaded 10 rows"

    mock_notion_source = MagicMock()
    mock_notion_source.with_resources.return_value = mock_notion_source

    with patch.dict(
        PIPELINE_CONFIG,
        {
            "notion": dataclasses.replace(
                PIPELINE_CONFIG["notion"],
                source_factory=MagicMock(return_value=mock_notion_source),
            )
        },
    ):
        info = refresh_pipeline("notion", is_incremental=True)

    assert info == "Loaded 10 rows"
    mock_dlt_pipeline.assert_called_once_with(
        pipeline_name="notion_habits_pipeline",
        dataset_name="raw_dev",
        destination=ANY,
        progress="log",
    )
    destination = mock_dlt_pipeline.call_args.kwargs["destination"]
    assert isinstance(destination, motherduck)
    assert destination.config_params["credentials"] == {
        "database": "personal",
        "password": "test-token",
    }
    # The Databricks staging volume path must not run for MotherDuck targets.
    mock_dlt_secrets_get.assert_not_called()


def test_get_destination_motherduck_normalizes_database_and_passes_token(
    monkeypatch,
):
    """A md:-prefixed database is normalized and the token is passed explicitly."""
    monkeypatch.setattr("pipelines.runner.DBT_TARGET", "test-md")
    monkeypatch.setenv("DESTINATION__MOTHERDUCK__CREDENTIALS__DATABASE", "md:other-db")
    monkeypatch.setenv("MOTHERDUCK_TOKEN", "tok-123")

    destination = get_destination()

    assert isinstance(destination, motherduck)
    assert destination.config_params["credentials"] == {
        "database": "other-db",
        "password": "tok-123",
    }


def test_get_destination_motherduck_requires_token(monkeypatch):
    """A missing MOTHERDUCK_TOKEN fails fast instead of at connect time."""
    monkeypatch.setattr("pipelines.runner.DBT_TARGET", "dev-md")
    monkeypatch.delenv("MOTHERDUCK_TOKEN", raising=False)

    with pytest.raises(RuntimeError, match="MOTHERDUCK_TOKEN is not set"):
        get_destination()


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("personal", "personal"),
        ("md:personal", "personal"),
        ("md://personal", "personal"),
        ("md:/personal", "personal"),
        ("  personal  ", "personal"),
        (None, "personal"),
        ("", "personal"),
    ],
)
def test_normalize_motherduck_database(value, expected):
    assert normalize_motherduck_database(value) == expected


@pytest.mark.parametrize(
    ("target", "expected"),
    [
        ("dev-md", True),
        ("test-md", True),
        ("prod-md", True),
        ("dev-db", False),
        ("mock", False),
    ],
)
def test_is_motherduck_target(target, expected):
    assert is_motherduck_target(target) is expected


def test_refresh_pipeline_rejects_target_schema_mismatch(monkeypatch):
    """Direct ingestion must not silently write schemas that disagree with the target."""
    monkeypatch.setattr("pipelines.runner.DBT_TARGET", "prod-db")
    monkeypatch.setattr("pipelines.runner.DBT_SCHEMA", "reporting_dev")
    monkeypatch.setattr("pipelines.runner.RAW_SCHEMA", "raw_dev")

    with pytest.raises(ValueError, match="requires DBT_SCHEMA=reporting"):
        refresh_pipeline("notion")
