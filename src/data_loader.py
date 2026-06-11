import os
import numpy as np
import pandas as pd
from typing import Tuple, List


def load_insurance_data(file_path: str) -> pd.DataFrame:
    """Loads the ACIS historical insurance dataset from a CSV/text file.

    Handles file verification, parses dates, calculates key domain metrics, 
    and returns a baseline DataFrame.
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

    # --- Domain Specific Transformations ---
    if "TransactionMonth" in df.columns:
        df["TransactionMonth"] = pd.to_datetime(df["TransactionMonth"])

    # Ensure localized identifier features are categorical strings, not numbers
    categorical_ids = ["PolicyID", "UnderwrittenCoverID", "PostalCode", "Mmcode"]
    for col in categorical_ids:
        if col in df.columns:
            df[col] = df[col].astype(str)

    # Calculate derived metrics to anchor risk analytics
    if "TotalClaims" in df.columns and "TotalPremium" in df.columns:
        df["LossRatio"] = np.where(df["TotalPremium"] > 0, df["TotalClaims"] / df["TotalPremium"], 0)
        df["Margin"] = df["TotalPremium"] - df["TotalClaims"]

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