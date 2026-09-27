from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


def load_tsv(path: str | Path, *, preserve_missing: bool = True) -> pd.DataFrame:
    """Load a challenge TSV while preserving string semantics and missing values.

    This is intentionally minimal: it reads tab-separated data exactly as provided,
    preserves entity IDs and string text columns as pandas string dtype, and keeps
    missing values distinct from empty strings instead of silently coercing them.
    """
    file_path = Path(path)
    df = pd.read_csv(
        file_path,
        sep="\t",
        dtype={
            "entity_id": "string",
            "business_name": "string",
            "business_address": "string",
            "country": "string",
        },
        keep_default_na=True,
        na_values=["", "NA", "N/A", "null", "NULL"],
    )

    # Preserve missing values while keeping the original column names/structure.
    if preserve_missing:
        for column in ["entity_id", "business_name", "business_address", "country"]:
            if column in df.columns:
                df[column] = df[column].astype("string")

    return df
