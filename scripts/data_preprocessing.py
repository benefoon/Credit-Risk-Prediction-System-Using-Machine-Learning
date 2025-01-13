import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load dataset
data = pd.read_csv("data/credit_risk_data.csv")

# Handle missing values
imputer = SimpleImputer(strategy="median")
data_filled = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

# Standardize numerical columns
scaler = StandardScaler()
numerical_cols = data_filled.select_dtypes(include=["float64", "int64"]).columns
data_filled[numerical_cols] = scaler.fit_transform(data_filled[numerical_cols])

# Encode categorical columns
categorical_cols = data_filled.select_dtypes(include=["object"]).columns
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    data_filled[col] = le.fit_transform(data_filled[col])
    label_encoders[col] = le

# Save preprocessed data
data_filled.to_csv("data/preprocessed_data.csv", index=False)

# Save encoders
import joblib
joblib.dump(label_encoders, "models/label_encoders.pkl")
