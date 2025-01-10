from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Load the trained model
MODEL_PATH = "models/credit_risk_model.pkl"
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise FileNotFoundError(f"Could not load the model. Check if the file exists at {MODEL_PATH}. Error: {e}")

@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict credit risk based on input JSON.
    Expects input JSON with the structure:
    [{"feature1": value1, "feature2": value2, ...}]
    """
    try:
        # Parse input JSON
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Convert input data to DataFrame
        df = pd.DataFrame(data)

        # Ensure input features match the model's expected features
        required_features = model.feature_names_in_
        if not all(feature in df.columns for feature in required_features):
            missing_features = list(set(required_features) - set(df.columns))
            return jsonify({"error": f"Missing features: {missing_features}"}), 400

        # Make predictions
        predictions = model.predict(df)

        # Return predictions
        return jsonify({"predictions": predictions.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
