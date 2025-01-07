import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_matrix(df):
    """Plot the correlation matrix for numerical features."""
    plt.figure(figsize=(10, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()

def plot_feature_distribution(df):
    """Plot distributions for each feature."""
    for column in df.select_dtypes(include=["float64", "int64"]).columns:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[column], kde=True)
        plt.title(f"Distribution of {column}")
        plt.show()

if __name__ == "__main__":
    data_path = "data/raw/credit_risk_data.csv"
    df = load_data(data_path)
    display_data_overview(df)
    plot_correlation_matrix(df)
    plot_feature_distribution(df)
