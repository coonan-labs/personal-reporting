# base imports
import json
import os
import re
from collections.abc import Callable
from datetime import UTC, datetime

import dlt

# PyPI imports
import pytest
from pytest import MonkeyPatch

# local imports
from pipelines.sources.hubspot import hubspot_source
from tests.unit.dlt.conftest import (
    pipeline_state,
    resolve_mock_path,
    sample_data,
    sample_resource,
    sample_response,
)

pytestmark = pytest.mark.local

# All CRM objects in the HubSpot pipeline
CRM_OBJECTS = [
    "contacts",
    "companies",
    "meetings",
    "calls",
    "communications",
    "tasks",
    "notes",
    "deals",
    "tickets",
]

# Objects that have association endpoints configured
OBJECTS_WITH_ASSOCIATIONS = {
    "meetings",
    "calls",
    "communications",
    "tasks",
    "notes",
    "deals",
    "tickets",
}


@pytest.fixture
def mock_hs_apis(monkeypatch: MonkeyPatch, mock_responses) -> Callable:
    BASE_URL = "https://api.hubapi.com"

    # mock the dlt.secrets.value to prevent credential errors
    monkeypatch.setenv("SOURCES__HUBSPOT__API_KEY", "dummy_api_key")
    initial_starts: dict[str, str] = {}

    def search_callback(request, object: str):
        payload = json.loads(request.body)
        after = payload.get("after")
        filters = payload["filterGroups"][0]["filters"]
        start_filter = next(f for f in filters if f["operator"] == "GTE")
        initial_start = initial_starts.setdefault(object, start_filter["value"])
        if after is None:
            if start_filter["value"] != initial_start:
                file_name = f"hubspot__{object}-run2.json"
            else:
                file_name = f"hubspot__{object}-run1_page1.json"
        else:
            page1 = sample_data(f"hubspot__{object}-run1_page1.json")
            assert str(after) == str(page1["paging"]["next"]["after"])
            file_name = f"hubspot__{object}-run1_page2.json"

        file_path = resolve_mock_path(file_name)
        if not os.path.exists(file_path):
            return (200, {}, json.dumps({"total": 0, "results": []}))
        return sample_response(file_name)

    def setup(endpoints=None):
        """Nested function to only register mock endpoints for tests.

        Args:
            endpoints (list, optional): Specific endpoints to register. Defaults to None (all).
        """
        if endpoints is None:
            endpoints = []

        # Mock association endpoints for full pipeline only — individual resource
        # tests use with_resources() which does not fetch association child resources
        if not endpoints:
            mock_responses.add(
                mock_responses.GET,
                re.compile(BASE_URL + r"/crm/v4/objects/\w+/\d+/associations/\w+"),
                json={"results": []},
                status=200,
            )

        # Mock CRM search endpoints
        for obj in CRM_OBJECTS:
            if not endpoints or obj in endpoints:
                mock_responses.add_callback(
                    mock_responses.POST,
                    BASE_URL + f"/crm/v3/objects/{obj}/search",
                    callback=lambda r, o=obj: search_callback(r, o),
                    content_type="application/json",
                )

        # Mock archived-sweep endpoints (GET /crm/v3/objects/{obj}?archived=true)
        # used by the deletion-tombstone resources. Registered for the full
        # source run, or when a test explicitly lists "{obj}_archived" in
        # endpoints. Single-resource tests that only fetch the live resource
        # must not register the archived mock, or `responses` fails teardown
        # for the unused mock.
        for obj in CRM_OBJECTS:
            if not endpoints or f"{obj}_archived" in endpoints:
                mock_responses.add_callback(
                    mock_responses.GET,
                    re.compile(BASE_URL + f"/crm/v3/objects/{obj}(\\?.*)?$"),
                    callback=lambda r, o=obj: sample_response(f"hubspot__{o}-archived.json"),
                    content_type="application/json",
                )

        if not endpoints or "schemas_contacts" in endpoints:
            mock_responses.add(
                mock_responses.GET,
                re.compile(BASE_URL + r"/crm-object-schemas/v3/schemas/\w+"),
                json=sample_data("hubspot__schemas_contacts.json"),
                status=200,
            )

    return setup


@pytest.mark.parametrize(
    ("resource", "expected_tables", "configs"),
    (
        ("contacts", 1, {}),
        ("companies", 1, {}),
        ("meetings", 1, {}),
        ("calls", 1, {}),
        (
            "schemas_contacts",
            1,
            {
                "max_table_nesting": 1,
                "columns": {
                    "searchable_properties": {"data_type": "json"},
                    "secondary_display_properties": {"data_type": "json"},
                },
            },
        ),
    ),
)
class TestHubspotPhases:
    def test_extract(
        self,
        mock_hs_apis,
        duckdb_pipeline: dlt.Pipeline,
        resource: str,
        expected_tables: int,
        configs: dict,
    ):
        # GIVEN
        # Mocked APIs
        mock_hs_apis(endpoints=[resource])

        # WHEN
        source = hubspot_source().with_resources(f"hubspot__{resource}")
        info = duckdb_pipeline.extract(source)

        # THEN
        assert len(info.loads_ids) == 1

    def test_normalize(
        self,
        duckdb_pipeline: dlt.Pipeline,
        resource: str,
        expected_tables: int,
        configs: dict,
    ):
        # GIVEN
        # Includes nested table rows for schemas
        expected_rows = 20 if "schemas" in resource else 3
        file_name = f"hubspot__{resource}-run1_page1.json"
        file_name2 = f"hubspot__{resource}.json"
        source = sample_resource(
            file_name,
            fallback=file_name2,
            data_selector=None if "schemas" in resource else "results",
            resource_configs=configs,
        )
        duckdb_pipeline.extract(source, table_name=resource)

        # WHEN
        info = duckdb_pipeline.normalize()

        # THEN
        # _dlt_state table, source table, and any child tables
        assert len([r for r in info.row_counts if r.startswith(resource)]) == expected_tables
        # first page record count
        assert info.row_counts[resource] == expected_rows

    def test_load(
        self,
        duckdb_pipeline: dlt.Pipeline,
        resource: str,
        expected_tables: int,
        configs: dict,
    ):
        # GIVEN
        # Files to load for sample test
        file_name = f"hubspot__{resource}-run1_page1.json"
        file_name2 = f"hubspot__{resource}.json"
        source = sample_resource(
            file_name,
            fallback=file_name2,
            resource_configs=configs,
        )
        duckdb_pipeline.extract(
            source,
            table_name=resource,
        )
        duckdb_pipeline.normalize()

        # WHEN
        info = duckdb_pipeline.load()

        # THEN
        assert info.has_failed_jobs is False
        assert all(p.state == "loaded" for p in info.load_packages)


@pytest.mark.parametrize(
    ("resource", "increment"),
    (
        ("contacts", True),
        ("companies", True),
        ("contacts", False),
        ("companies", False),
        ("meetings", False),
        ("schemas_contacts", False),
    ),
)
def test_hubspot_refresh(
    mock_hs_apis,
    duckdb_pipeline: dlt.Pipeline,
    resource: str,
    increment: bool,
):
    # GIVEN (1)
    # Mock APIs
    mock_hs_apis(endpoints=[resource])
    expected_rows = 1 if "schemas" in resource else 5
    # Dataset from pipeline (dev mode)
    dataset = duckdb_pipeline.dataset_name
    table = resource.split("_")[0]
    # Defaults to append for most resources
    write_disposition = None if increment else "replace"

    # WHEN (1)
    source = hubspot_source().with_resources(f"hubspot__{resource}")
    info = duckdb_pipeline.run(source)

    # THEN (1)
    # Run pipeline the first time
    assert info.first_run is True
    assert info.has_failed_jobs is False
    if "schemas" not in resource:
        expected_cursor = max(
            item["updatedAt"]
            for page in ("run1_page1", "run1_page2")
            for item in sample_data(f"hubspot__{resource}-{page}.json")["results"]
        )
        assert (
            pipeline_state(duckdb_pipeline)["sources"]["hubspot_source"]["resources"][
                f"hubspot__{resource}"
            ]["incremental"]["updatedAt"]["last_value"]
            == expected_cursor
        )
    # Validate loaded data from initial run
    with duckdb_pipeline.sql_client() as client:
        table_rows = client.execute_sql(f"SELECT 1 FROM {dataset}.hubspot__{table}")
    assert len(table_rows) == expected_rows

    # GIVEN (2)
    expected_rows += 1 if increment else 0

    # WHEN (2)
    info2 = duckdb_pipeline.run(source, write_disposition=write_disposition)

    # THEN (2)
    # Run pipeline again
    assert info2.first_run is False
    assert info2.has_failed_jobs is False
    # Validate loaded data from incremental run
    with duckdb_pipeline.sql_client() as client:
        table_rows2 = client.execute_sql(f"SELECT 1 FROM {dataset}.hubspot__{table}")
    assert len(table_rows2) == expected_rows


def test_hubspot_pipeline(mock_hs_apis, duckdb_pipeline):
    """
    Test that the HubSpot pipeline runs and loads data correctly.
    """
    # GIVEN
    mock_hs_apis()

    # WHEN
    # Run the pipeline
    source = hubspot_source()
    info = duckdb_pipeline.run(source)

    # THEN
    # Assert that the pipeline ran successfully
    assert info.first_run is True
    assert info.has_failed_jobs is False
    assert len(info.loads_ids) == 1

    # Check the loaded data
    dataset = duckdb_pipeline.dataset_name
    with duckdb_pipeline.sql_client() as client:
        # Check schemas table
        schema_table = client.execute_sql(f"SELECT 1 FROM {dataset}.hubspot__schemas")
        assert len(schema_table) == 1

        # Check contacts table (5 live rows + 1 archived tombstone)
        contacts_table = client.execute_sql(
            f"SELECT 1 FROM {dataset}.hubspot__contacts",
        )
        assert len(contacts_table) == 6

        # Check companies table (5 live rows + 1 archived tombstone)
        companies_table = client.execute_sql(
            f"SELECT 1 FROM {dataset}.hubspot__companies",
        )
        assert len(companies_table) == 6

        # Check meetings table (5 live rows + 1 archived tombstone)
        meetings_table = client.execute_sql(
            f"SELECT 1 FROM {dataset}.hubspot__meetings",
        )
        assert len(meetings_table) == 6


def test_hubspot_archived_tombstone(mock_hs_apis, duckdb_pipeline):
    """
    Test that the archived-sweep resource loads a deletion tombstone for an
    archived contact, and that the live resource's incremental cursor is
    unchanged by the sweep.
    """
    # GIVEN
    # Register the live contacts search endpoint and the archived endpoint.
    mock_hs_apis(endpoints=["contacts", "contacts_archived"])
    dataset = duckdb_pipeline.dataset_name

    # WHEN
    # Run the live contacts resource and its archived-sweep sibling.
    source = hubspot_source().with_resources("hubspot__contacts", "hubspot__contacts_archived")
    info = duckdb_pipeline.run(source)

    # THEN
    assert info.first_run is True
    assert info.has_failed_jobs is False

    # The tombstone row (id 82767429517, also present as a live row) is
    # flagged deleted with the archived timestamp.
    with duckdb_pipeline.sql_client() as client:
        tombstones = client.execute_sql(
            f"SELECT _deleted, _deleted_at FROM {dataset}.hubspot__contacts "
            "WHERE id = 82767429517 AND _deleted = true"
        )
    assert len(tombstones) == 1
    assert tombstones[0][0] is True
    # dlt stores the ISO8601 "Z" timestamp as a timezone-aware UTC datetime.
    assert tombstones[0][1] == datetime(2026, 8, 1, 10, 0, 0, tzinfo=UTC)

    # The live incremental cursor is the max live updatedAt, unchanged by
    # the archived sweep (whose rows carry updatedAt = archivedAt).
    expected_cursor = max(
        item["updatedAt"]
        for page in ("run1_page1", "run1_page2")
        for item in sample_data(f"hubspot__contacts-{page}.json")["results"]
    )
    assert (
        pipeline_state(duckdb_pipeline)["sources"]["hubspot_source"]["resources"][
            "hubspot__contacts"
        ]["incremental"]["updatedAt"]["last_value"]
        == expected_cursor
    )
