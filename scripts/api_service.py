from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model
model = joblib.load("scripts/credit_risk_model.pkl")

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": prediction.tolist()}
