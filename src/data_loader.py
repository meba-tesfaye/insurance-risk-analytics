import os
import pandas as pd
from typing import Tuple, List


def load_insurance_data(file_path: str) -> pd.DataFrame:
    """Loads the ACIS historical insurance dataset from a CSV/text file.

    Handles file verification and returns a baseline DataFrame.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Target dataset not found at: {file_path}. "
            "Verify DVC checkout or file path."
        )

    # Ingest file (accounting for standard pipe or comma delimiters)
    try:
        df = pd.read_csv(file_path, sep=None, engine="python")
    except Exception as e:
        raise IOError(f"Failed parsing dataset: {str(e)}")

    return df


def inspect_data_quality(df: pd.DataFrame) -> pd.DataFrame:
    """Performs a comprehensive data quality check.

    Returns a DataFrame breaking down types, missing cells, and sparsity.
    """
    quality_df = pd.DataFrame(
        {
            "Data Type": df.dtypes,
            "Missing Values": df.isnull().sum(),
            "Missing %": (df.isnull().sum() / len(df)) * 100,
            "Unique Values": df.nunique(),
        }
    )
    return quality_df.sort_values(by="Missing %", ascending=False)


def get_feature_groups(df: pd.DataFrame) -> Tuple[List[str], List[str]]:
    """Partitions column names into numerical and categorical subgroups for EDA."""
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    categorical_cols = df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    return numeric_cols, categorical_cols