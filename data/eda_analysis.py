import pandas as pd
from pandas_profiling import ProfileReport

# Load dataset
data = pd.read_csv("data/credit_risk_data.csv")

# Generate EDA report
profile = ProfileReport(data, title="EDA Report", explorative=True)
profile.to_file("data/eda_report.html")
