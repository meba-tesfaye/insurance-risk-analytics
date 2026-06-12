import pandas as pd
from src.modeling_pipeline import preprocess_insurance_data

def test_preprocess_insurance_data_removes_leakage():
    """Test that target leakage and ID columns are successfully dropped."""
    dummy_df = pd.DataFrame({
        'CustomerID': [1, 2, 3],
        'ClaimAmount': [100, 200, 300],
        'TotalClaims': [10, 20, 30],
        'RiskScore': [0.4, 0.5, 0.6]
    })
    X, y = preprocess_insurance_data(dummy_df)
    assert 'ClaimAmount' not in X.columns
    assert 'CustomerID' not in X.columns