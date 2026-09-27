from pathlib import Path

import pandas as pd
import pytest

from src.data_loader import load_tsv


def test_load_tsv_reads_expected_columns_and_dtype(tmp_path):
    path = tmp_path / "sample.tsv"
    path.write_text(
        "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
        "S1-001\tAcme Corp\t123 Main St\tUS\n"
        "S2-002\tBeta LLC\t\tIndia\n",
        encoding="utf-8",
    )

    df = load_tsv(path)

    assert list(df.columns) == ["entity_id", "business_name", "business_address", "country"]
    assert df["entity_id"].dtype == "string"
    assert df["business_name"].dtype == "string"
    assert df["business_address"].dtype == "string"
    assert df["country"].dtype == "string"
    assert df.iloc[0]["entity_id"] == "S1-001"
    assert df.iloc[1]["entity_id"] == "S2-002"
    assert df.iloc[1]["country"] == "India"


def test_load_tsv_preserves_missing_values_without_corrupting_columns(tmp_path):
    path = tmp_path / "missing.tsv"
    path.write_text(
        "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
        "S1-010\tAlpha\t123 Oak Avenue\tUS\n"
        "S2-011\t\t\tIndia\n"
        "S3-012\tGamma\t\t\n",
        encoding="utf-8",
    )

    df = load_tsv(path)

    assert df["business_name"].isna().sum() == 1
    assert df["business_address"].isna().sum() == 2
    assert df["country"].isna().sum() == 1
    assert df.iloc[1]["business_name"] is pd.NA or pd.isna(df.iloc[1]["business_name"])
    assert df.iloc[2]["country"] is pd.NA or pd.isna(df.iloc[2]["country"])


def test_load_tsv_preserves_source_prefixes_and_country_strings(tmp_path):
    path = tmp_path / "prefixes.tsv"
    path.write_text(
        "entity_id\tbusiness_name\tbusiness_address\tcountry\n"
        "S1-100\tNorthwind Foods\t18 Rue de l'Opera\tFrance\n"
        "S2-200\tNorthwind Foods Pvt Ltd\t18 Rue de l'Opera\tFrance\n",
        encoding="utf-8",
    )

    df = load_tsv(path)

    assert df["entity_id"].tolist() == ["S1-100", "S2-200"]
    assert df["country"].tolist() == ["France", "France"]
    assert all(isinstance(v, str) for v in df["country"].tolist())
