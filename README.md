# Credit Risk Prediction System Using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8-blue.svg)
![Build Status](https://img.shields.io/github/actions/workflow/status/benefoon/Credit-Risk-Prediction-System-Using-Machine-Learning/main.yml?label=CI/CD&style=plastic)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![MLflow](https://img.shields.io/badge/MLflow-Monitoring-orange)

---

## 🌟 Overview

The **Credit Risk Prediction System** is a comprehensive project leveraging machine learning and advanced feature engineering techniques to predict the credit risk of individuals or organizations. It includes robust data analysis, preprocessing, model training, and deployment capabilities. The system also integrates security features and APIs for real-time usage.

### Key Features:
- 📊 **Exploratory Data Analysis (EDA)**: Gain insights into data with visualizations and statistics.
- 🤖 **Machine Learning Models**: Use advanced algorithms like Random Forest, XGBoost, and Neural Networks.
- 🔍 **Feature Engineering**: Create polynomial and interaction features for improved model accuracy.
- 🌐 **API Support**: Real-time predictions via FastAPI.
- 🔒 **Security**: Implements encryption and input validation for sensitive data.
- 📈 **Model Monitoring**: Tracks and logs model performance with MLflow.

---

## 🏗 Repository Structure

```plaintext
Credit-Risk-Prediction-System-Using-Machine-Learning/
├── data/
│   ├── credit_risk_data.csv        # Raw data
│   ├── preprocessed_data.csv       # Preprocessed data
│   ├── interaction_data.csv        # Feature-engineered data
│   ├── eda_analysis.py             # Exploratory data analysis script
│   ├── data_analysis.py            # Data insights and summaries
│   ├── data_preprocessing.py       # Data preprocessing script
│   ├── model_training.py           # Basic ML model training
│   ├── model_training2.py          # Alternative ML model training
├── scripts/
│   ├── advanced_model_training.py  # Advanced ML training with hyperparameter tuning
│   ├── api.py                      # Basic API structure
│   ├── api_service.py              # FastAPI service for real-time predictions
│   ├── feature_interactions.py     # Create polynomial and interaction features
│   ├── hyperparameter_tuning.py    # Hyperparameter tuning for ML models
│   ├── mlflow_reporting.py         # MLflow integration for model monitoring
│   ├── neural_network_model.py     # Neural network training script
│   ├── outlier_detection.py        # Outlier detection logic
│   ├── utils.py                    # Utility functions
├── security/
│   ├── auth_jwt.py                 # JSON Web Token (JWT) authentication
│   ├── data_encryption.py          # Sensitive data encryption
│   ├── encryption_utils.py         # Utility functions for encryption
│   ├── input_validation.py         # Input validation for API requests
│   ├── logging_monitoring.py       # Logging and monitoring
│   ├── rate_limiting.py            # API rate limiting
│   ├── rbac.py                     # Role-based access control
│   ├── secure_database.py          # Secure database connection logic
├── tests/
│   ├── test_project.py             # Unit tests for scripts
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker container configuration
├── README.md                       # Project documentation
```

---

## 🚀 Features

### 📊 Exploratory Data Analysis (EDA)
- Visualizes missing values, correlations, and target variable distributions.
- Summarizes data statistics and detects patterns for better understanding.

### 🛠 Data Preprocessing
- Cleans and standardizes data using advanced preprocessing techniques.
- Handles missing values, encodes categorical features, and scales numerical columns.

### 🔍 Feature Engineering
- Creates polynomial and interaction features to improve model accuracy.
- Saves transformed datasets for downstream processes.

### 🤖 Machine Learning Models
- **Traditional ML Models**: Random Forest, XGBoost with hyperparameter tuning.
- **Deep Learning**: Neural networks implemented using TensorFlow/Keras.

### 🌐 API Integration
- Implements a REST API using FastAPI for real-time predictions.
- API is secured with JWT authentication and input validation.

### 🔒 Security
- Encrypts sensitive columns in datasets.
- Implements role-based access control (RBAC) and rate limiting.

### 📈 Model Monitoring
- Tracks performance metrics using MLflow.
- Logs parameters, metrics, and trained models for easy reproducibility.

---

## 📦 Installation

### Prerequisites
- Python 3.8+
- Docker (optional for containerization)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/benefoon/Credit-Risk-Prediction-System-Using-Machine-Learning.git
   cd Credit-Risk-Prediction-System-Using-Machine-Learning
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run unit tests:
   ```bash
   pytest tests/
   ```

4. Launch the FastAPI service:
   ```bash
   uvicorn scripts.api_service:app --reload
   ```

---

## ⚙️ Usage

### Preprocessing Data
Prepare the dataset by running:
```bash
python data/data_preprocessing.py
```

### Feature Engineering
Create polynomial and interaction features:
```bash
python scripts/feature_interactions.py
```

### Train Machine Learning Models
Train advanced models:
```bash
python scripts/advanced_model_training.py
```

Train a neural network model:
```bash
python scripts/neural_network_model.py
```

### API Predictions
Run the API service:
```bash
python scripts/api_service.py
```

Make a prediction by sending a POST request:
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"feature1": 1, "feature2": 2, "feature3": 3}'
```

---

## 🔗 References

1. **Machine Learning for Credit Risk**: Provost, F., & Fawcett, T. (2013). *Data Science for Business*. O'Reilly Media.
2. **Neural Networks**: Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
3. **FastAPI Documentation**: https://fastapi.tiangolo.com
4. **MLflow Documentation**: https://mlflow.org

---

## 🤝 Contributing

We welcome contributions to improve this project! To contribute:
1. Fork the repository.
2. Create a new branch.
3. Submit a pull request.

---

![Python](https://img.shields.io/badge/Python-3.8-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-RandomForest-brightgreen.svg)
![Deep Learning](https://img.shields.io/badge/Deep_Learning-TensorFlow-orange.svg)
![FastAPI](https://img.shields.io/badge/API-FastAPI-green.svg)
```
