from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Define model path and load model with error handling
MODEL_PATH = "models/credit_risk_model.pkl"
model = None

try:
    model = joblib.load(MODEL_PATH)
    print(f"Model loaded successfully from {MODEL_PATH}")
except FileNotFoundError:
    print(f"Error: Model file not found at {MODEL_PATH}")
except Exception as e:
    print(f"Error loading model: {e}")

@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict credit risk based on input JSON.
    
    Input: JSON with the structure:
    [{"feature1": value1, "feature2": value2, ...}]
    
    Output: JSON with predictions or error messages.
    """
    if not model:
        return jsonify({"error": "Model is not loaded. Cannot make predictions."}), 500

    try:
        # Parse input JSON
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Convert input data to DataFrame
        df = pd.DataFrame(data)

        # Ensure input features match the model's expected features
        required_features = getattr(model, "feature_names_in_", None)
        if required_features is not None:
            if not all(feature in df.columns for feature in required_features):
                missing_features = list(set(required_features) - set(df.columns))
                return jsonify({"error": f"Missing features: {missing_features}"}), 400

        # Make predictions
        predictions = model.predict(df)

        # Return predictions
        return jsonify({"predictions": predictions.tolist()}), 200

    except ValueError as ve:
        return jsonify({"error": f"Value error: {ve}"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

if __name__ == "__main__":
    if model:
        # Run the Flask app if the model is successfully loaded
        app.run(debug=True, host="0.0.0.0", port=5000)
    else:
        print("The Flask app cannot start because the model could not be loaded.")
