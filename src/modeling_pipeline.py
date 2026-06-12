import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def preprocess_insurance_data(df, target_col='TotalClaims'):
    """
    Cleans data, drops identifiers, and encodes categorical variables.
    """
    # Drop unique identifiers and dates that won't generalize well
    cols_to_drop = ['CustomerID', 'TransactionDate', 'VehicleModel']
    existing_drops = [col for col in cols_to_drop if col in df.columns]
    processed_df = df.drop(columns=existing_drops)
    
    # Separate features and target
    X = processed_df.drop(columns=[target_col])
    y = processed_df[target_col]
    
    # Automatically identify categorical columns and apply one-hot encoding
    categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
    X_encoded = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
    
    return X_encoded, y

def train_and_evaluate_model(X, y):
    """
    Splits data, trains a Random Forest model, and returns performance metrics.
    """
    # 80/20 Train-Test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and fit the model
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    
    # Predict and calculate metrics
    predictions = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)
    
    return model, X_test, y_test, {"RMSE": rmse, "R2_Score": r2}