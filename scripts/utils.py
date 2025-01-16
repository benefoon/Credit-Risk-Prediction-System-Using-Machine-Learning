from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the trained model with error handling
MODEL_PATH = "models/credit_risk_model.pkl"
try:
    model = joblib.load(MODEL_PATH)
    print(f"Model loaded successfully from {MODEL_PATH}")
except FileNotFoundError:
    model = None
    print(f"Error: Model file not found at {MODEL_PATH}")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict credit risk based on input JSON.
    
    Input: JSON containing feature data
    Output: JSON with predictions
    """
    if not model:
        return jsonify({"error": "Model is not loaded. Cannot make predictions."}), 500

    try:
        # Parse input JSON
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid input: No data provided."}), 400

        # Convert input JSON to DataFrame
        df = pd.DataFrame(data)

        # Ensure required columns exist
        expected_columns = model.feature_names_in_  # Assumes the model has this attribute
        if not all(col in df.columns for col in expected_columns):
            missing_cols = list(set(expected_columns) - set(df.columns))
            return jsonify({"error": f"Missing columns in input data: {missing_cols}"}), 400

        # Make predictions
        predictions = model.predict(df)
        return jsonify({"predictions": predictions.tolist()}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred during prediction: {e}"}), 500

if __name__ == "__main__":
    # Ensure the model file exists before running the app
    if model:
        app.run(debug=True, host="0.0.0.0", port=5000)
    else:
        print("Flask app is not starting because the model file is missing.")
