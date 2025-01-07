import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, confusion_matrix, ConfusionMatrixDisplay

def plot_roc_curve(y_test, y_scores):
    """Plot the ROC curve."""
    fpr, tpr, thresholds = roc_curve(y_test, y_scores)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label="ROC Curve", color="blue")
    plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.show()

def plot_confusion_matrix(y_test, y_pred):
    """Plot the confusion matrix."""
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap="Blues")
    plt.title("Confusion Matrix")
    plt.show()

if __name__ == "__main__":
    # Train the model
    data_file = "data/processed/credit_risk_data.csv"
    model_file = "models/credit_risk_model.pkl"
    train_model(data_file, model_file)

    # Additional evaluation
    y_scores = model.predict_proba(X_test)[:, 1]
    plot_roc_curve(y_test, y_scores)
    plot_confusion_matrix(y_test, y_pred)
