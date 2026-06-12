import numpy as np
import pandas as pd
from scipy import stats

def test_numerical_vs_categorical(df, numerical_col, categorical_col, alpha=0.05):
    """
    Performs a statistical test comparing a numerical metric across distinct categories.
    Uses Mann-Whitney U for 2 groups and Kruskal-Wallis for >2 groups.
    """
    # Clean out any missing values for these columns
    clean_df = df[[numerical_col, categorical_col]].dropna()
    
    # Extract data groups dynamically based on unique categories
    categories = clean_df[categorical_col].unique()
    groups = [clean_df[clean_df[categorical_col] == cat][numerical_col].values for cat in categories]
    
    # Filter out empty groups or groups with all identical values
    groups = [g for g in groups if len(g) > 0]
    
    if len(groups) < 2:
        return {"error": f"Not enough distinct groups in {categorical_col} to run a test."}
    
    # Select test based on number of groups
    if len(groups) == 2:
        test_name = "Mann-Whitney U Test"
        stat, p_val = stats.mannwhitneyu(groups[0], groups[1], alternative='two-sided')
    else:
        test_name = "Kruskal-Wallis H-Test"
        stat, p_val = stats.kruskal(*groups)
        
    significant = p_val < alpha
    
    return {
        "test_name": test_name,
        "statistic": float(stat),
        "p_value": float(p_val),
        "significant": bool(significant),
        "message": f"Reject H0: Significant difference found." if significant else "Fail to reject H0: No significant difference found."
    }

def analyze_profitability_by_zip(df, premium_col='TotalPremium', claims_col='TotalClaims', zip_col='PostalCode', alpha=0.05):
    """
    Calculates Margin (Premium - Claims) and tests it across different Zip Codes.
    """
    df_copy = df.copy()
    # Calculate profit margin dynamically
    df_copy['Margin'] = df_copy[premium_col] - df_copy[claims_col]
    
    return test_numerical_vs_categorical(df_copy, 'Margin', zip_col, alpha)