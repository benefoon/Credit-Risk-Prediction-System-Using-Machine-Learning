import pandas as pd

def load_data(file_path):
    """
    Load the dataset from the given file path.
    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data successfully loaded from: {file_path}")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}. Please check the file path.")
        raise
    except pd.errors.EmptyDataError:
        print(f"Error: The file at {file_path} is empty.")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

def display_data_overview(df):
    """
    Display basic insights and structure of the dataset.
    Includes dataset info, first rows, missing values, and a statistical summary.
    """
    if df.empty:
        print("Warning: The dataset is empty. No data to display.")
        return

    print("\n--- Dataset Info ---")
    print(df.info())
    print("\n--- First 5 Rows ---")
    print(df.head())
    print("\n--- Missing Values ---")
    print(df.isnull().sum())
    print("\n--- Statistical Overview ---")
    print(df.describe())

if __name__ == "__main__":
    # Define the path to the dataset
    data_path = "data/raw/credit_risk_data.csv"
    
    try:
        # Load and display data
        df = load_data(data_path)
        display_data_overview(df)
    except Exception as e:
        print(f"Failed to process the dataset: {e}")