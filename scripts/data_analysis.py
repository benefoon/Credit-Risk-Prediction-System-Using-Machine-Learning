import pandas as pd

def load_data(file_path):
    """Load the dataset from the given file path."""
    return pd.read_csv(file_path)

def display_data_overview(df):
    """Display basic insights and structure of the dataset."""
    print("Dataset Info:")
    print(df.info())
    print("\nFirst 5 Rows:")
    print(df.head())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nStatistical Overview:")
    print(df.describe())

if __name__ == "__main__":
    data_path = "data/raw/credit_risk_data.csv"
    df = load_data(data_path)
    display_data_overview(df)
