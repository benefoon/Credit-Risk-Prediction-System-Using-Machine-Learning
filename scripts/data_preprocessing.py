import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(input_path, output_path):
    """Preprocess the dataset and save the cleaned data."""
    df = pd.read_csv(input_path)
    
    # Handle missing values
    df = df.dropna()
    
    # Encode categorical variables
    label_encoders = {}
    for column in df.select_dtypes(include=["object"]).columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le
    
    # Normalize numerical features
    scaler = StandardScaler()
    numerical_cols = df.select_dtypes(include=["float64", "int64"]).columns
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    
    # Save processed data
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

if __name__ == "__main__":
    input_file = "data/raw/credit_risk_data.csv"
    output_file = "data/processed/credit_risk_data.csv"
    preprocess_data(input_file, output_file)
