import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

def preprocess_insurance_data(df, target_col='TotalClaims'):
    """
    Cleans data, handles missing values explicitly, drops identifiers, 
    and removes target leakage columns like ClaimAmount.
    """
    processed_df = df.copy()
    
    # --- STRATEGY: Explicit Missing Value Handling ---
    num_cols = processed_df.select_dtypes(include=['number']).columns
    for col in num_cols:
        if processed_df[col].isnull().sum() > 0:
            processed_df[col] = processed_df[col].fillna(processed_df[col].median())
            
    cat_cols = processed_df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        if processed_df[col].isnull().sum() > 0:
            processed_df[col] = processed_df[col].fillna(processed_df[col].mode()[0])
    
    cols_to_drop = ['CustomerID', 'TransactionDate', 'VehicleModel', 'ClaimAmount']
    existing_drops = [col for col in cols_to_drop if col in processed_df.columns]
    processed_df = processed_df.drop(columns=existing_drops)
    
    X = processed_df.drop(columns=[target_col])
    y = processed_df[target_col]
    
    categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
    X_encoded = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
    
    return X_encoded, y

def train_and_evaluate_all_models(X, y):
    """
    Splits data, trains Linear Regression, Random Forest, and Gradient Boosting,
    prints performance, and writes a formal audit report to the reports/ directory.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1),
        "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=42)
    }
    
    results = {}
    
    print("--- Model Performance Comparison ---")
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        r2 = r2_score(y_test, preds)
        
        results[name] = {
            "model_object": model,
            "RMSE": rmse,
            "R2_Score": r2
        }
        print(f"{name} -> RMSE: {rmse:.2f}, R2: {r2:.2f}")
    
    # --- STRATEGY: Formalized Results Table for Production Audit ---
    os.makedirs('reports', exist_ok=True)
    report_path = os.path.join('reports', 'model_comparison.md')
    
    table_lines = [
        "# ACIS Risk Analytics: Model Performance Audit Report",
        f"**Generated Evaluation Date:** 2026-06\n",
        "| Model Architecture | Root Mean Squared Error (RMSE) | R² Score (Variance Explained) |",
        "| :--- | :--- | :--- |"
    ]
    
    for name, metrics in results.items():
        table_lines.append(f"| **{name}** | {metrics['RMSE']:.4f} | {metrics['R2_Score']:.4f} |")
        
    with open(report_path, 'w') as f:
        f.write('\n'.join(table_lines))
        
    print(f"\n[AUDIT INFO] Formalized results table successfully compiled at: {report_path}")
        
    return results, X_test, y_test