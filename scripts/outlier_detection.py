from sklearn.ensemble import IsolationForest
import pandas as pd

# Load dataset
data = pd.read_csv("data/credit_risk_data.csv")

# Detect outliers
iso = IsolationForest(contamination=0.05, random_state=42)
data['outlier'] = iso.fit_predict(data.drop('target_column', axis=1))

# Save filtered data
filtered_data = data[data['outlier'] == 1]
filtered_data.to_csv("data/filtered_data.csv", index=False)
