import mlflow
import mlflow.sklearn
from sklearn.metrics import accuracy_score

# Log metrics and model
mlflow.start_run()

mlflow.log_param("model", "XGBoost")
mlflow.log_metric("accuracy", accuracy)

mlflow.sklearn.log_model(model, "model")
mlflow.end_run()
