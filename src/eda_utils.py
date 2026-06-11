import pandas as pd
import numpy as np

def check_data_quality(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a comprehensive data quality scorecard covering null values,
    data types, and cardinality.
    """
    quality_df = pd.DataFrame({
        'Data Type': df.dtypes,
        'Missing Values': df.isnull().sum(),
        'Missing %': (df.isnull().sum() / len(df)) * 100,
        'Unique Values': df.nunique()
    })
    return quality_df.sort_values(by='Missing Values', ascending=False)

def get_outlier_bounds(df: pd.DataFrame, column: str) -> tuple:
    """
    Calculates operational IQR boundaries for tracking extreme values 
    in financial attributes.
    """
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = max(0, q1 - 1.5 * iqr) # Insurance values shouldn't fall below zero
    upper_bound = q3 + 1.5 * iqr
    return lower_bound, upper_bound

def aggregate_geographic_risk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates risk and financial profiles across South African provinces.
    """
    geo_summary = df.groupby('Province').agg(
        TotalPremiums=('TotalPremium', 'sum'),
        TotalClaims=('TotalClaims', 'sum'),
        PolicyCount=('PolicyID', 'count'),
        ClaimCount=('TotalClaims', lambda x: (x > 0).sum())
    ).reset_index()
    
    geo_summary['ProvinceLossRatio'] = geo_summary['TotalClaims'] / geo_summary['TotalPremiums']
    geo_summary['ClaimFrequency'] = geo_summary['ClaimCount'] / geo_summary['PolicyCount']
    
    return geo_summary.sort_values(by='ProvinceLossRatio', ascending=False)