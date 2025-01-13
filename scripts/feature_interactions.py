import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

# Load dataset
data = pd.read_csv("data/filtered_data.csv")

# Generate feature interactions
poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
interactions = poly.fit_transform(data.drop('target_column', axis=1))

# Save transformed data
transformed_data = pd.DataFrame(interactions)
transformed_data['target_column'] = data['target_column']
transformed_data.to_csv("data/transformed_data.csv", index=False)
