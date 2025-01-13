from cryptography.fernet import Fernet
import pandas as pd

# Generate key
key = Fernet.generate_key()
cipher = Fernet(key)

# Load dataset
data = pd.read_csv("data/credit_risk_data.csv")

# Encrypt sensitive column
data['sensitive_column'] = data['sensitive_column'].apply(lambda x: cipher.encrypt(x.encode()))

# Save encrypted data
data.to_csv("data/encrypted_data.csv", index=False)
