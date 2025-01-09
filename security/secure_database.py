from sqlalchemy import create_engine, text
import pandas as pd

DATABASE_URL = "mysql+pymysql://user:password@host/database"

def get_data_securely(query, params={}):
    """Fetch data securely using parameterized queries to prevent SQL Injection"""
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute(text(query), params)
        return pd.DataFrame(result.fetchall(), columns=result.keys())

# Example Usage
query = "SELECT * FROM credit_data WHERE customer_id = :customer_id"
params = {"customer_id": 12345}
df = get_data_securely(query, params)
