from imblearn.over_sampling import SMOTE

def balance_data(X, y):
    """Balance imbalanced datasets using SMOTE."""
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)
    return X_resampled, y_resampled

if __name__ == "__main__":
    # Load data
    input_file = "data/raw/credit_risk_data.csv"
    output_file = "data/processed/credit_risk_data.csv"
    df = preprocess_data(input_file, output_file)
    
    # Separate features and target
    X = df.drop("target", axis=1)
    y = df["target"]
    
    # Balance data
    X_balanced, y_balanced = balance_data(X, y)
    print("Data balanced successfully.")
