"""Pipeline configuration module.

This module contains global configuration settings for all data pipelines,
including schema definitions, environment variables, and base constants.
"""

import os

# IS_TEST = os.getenv("TEST") or os.getenv("CI")
BASE_DATE = "2020-01-01"

# google or 1password
SECRET_STORE = os.getenv("SECRET_STORE", default="1password")

# Define target and schema names supplied by the environment, defaulting to local dev
DBT_TARGET = os.getenv("DBT_TARGET") or "dev-md"
DBT_SCHEMA = os.getenv("DBT_SCHEMA") or "reporting_dev"
RAW_SCHEMA = os.getenv("RAW_SCHEMA") or "raw_dev"

# Set environment variables for target and schemas
os.environ["DBT_TARGET"] = DBT_TARGET
os.environ["DBT_SCHEMA"] = DBT_SCHEMA
os.environ["RAW_SCHEMA"] = RAW_SCHEMA

# Disable dlt's anonymous usage telemetry. dlt sends command names, hashed
# pipeline names and execution timings to https://telemetry.scalevector.ai
# by default (runtime.dlthub_telemetry). This is a personal pipeline and the
# telemetry is not needed, so turn it off for every run that imports this
# package (CI, local runs, tests). Unit tests also set it in conftest.py.
os.environ["RUNTIME__DLTHUB_TELEMETRY"] = "false"
