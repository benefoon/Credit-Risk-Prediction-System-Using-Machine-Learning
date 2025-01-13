import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data/credit_risk_data.csv")

# Summary statistics
print("Summary Statistics:")
print(data.describe())

# Check missing values
missing_values = data.isnull().sum()
print("\nMissing Values:")
print(missing_values)

# Visualize missing values
plt.figure(figsize=(10, 6))
sns.heatmap(data.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.savefig("outputs/missing_values_heatmap.png")

# Correlation heatmap
plt.figure(figsize=(12, 8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.savefig("outputs/correlation_matrix.png")

# Distribution of target variable
plt.figure(figsize=(8, 6))
sns.countplot(x="target_column", data=data, palette="pastel")
plt.title("Target Variable Distribution")
plt.savefig("outputs/target_distribution.png")

# Save analysis results
data.describe().to_csv("outputs/data_summary.csv")
missing_values.to_csv("outputs/missing_values.csv")
