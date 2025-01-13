import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

# Load dataset
data = pd.read_csv("data/preprocessed_data.csv")

# Create polynomial and interaction features
poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
interaction_features = poly.fit_transform(data.drop("target_column", axis=1))

# Create a new DataFrame
feature_names = poly.get_feature_names_out(data.drop("target_column", axis=1).columns)
interaction_data = pd.DataFrame(interaction_features, columns=feature_names)

# Combine with target column
interaction_data["target_column"] = data["target_column"]

# Save transformed data
interaction_data.to_csv("data/interaction_data.csv", index=False)
