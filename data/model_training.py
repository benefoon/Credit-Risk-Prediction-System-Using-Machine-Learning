import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, confusion_matrix, ConfusionMatrixDisplay
import os

def plot_roc_curve(y_test, y_scores, figsize=(8, 6), curve_color="blue", line_color="gray"):
    """
    Plot the ROC curve.
    
    Parameters:
    - y_test: Array-like, true labels.
    - y_scores: Array-like, predicted probabilities.
    - figsize: Tuple, figure size.
    - curve_color: String, color of the ROC curve.
    - line_color: String, color of the diagonal line.
    """
    if len(y_test) != len(y_scores):
        raise ValueError("Length of y_test and y_scores must be equal.")
    
    fpr, tpr, thresholds = roc_curve(y_test, y_scores)
    plt.figure(figsize=figsize)
    plt.plot(fpr, tpr, label="ROC Curve", color=curve_color)
    plt.plot([0, 1], [0, 1], linestyle="--", color=line_color, label="Random Classifier")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

def plot_confusion_matrix(y_test, y_pred, cmap="Blues", title="Confusion Matrix"):
    """
    Plot the confusion matrix.
    
    Parameters:
    - y_test: Array-like, true labels.
    - y_pred: Array-like, predicted labels.
    - cmap: String, colormap for the confusion matrix.
    - title: String, title of the plot.
    """
    if len(y_test) != len(y_pred):
        raise ValueError("Length of y_test and y_pred must be equal.")
    
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=cmap)
    plt.title(title)
    plt.grid(alpha=0.3)
    plt.show()

if __name__ == "__main__":
    # Example paths (modify as needed)
    data_file = os.path.join("data", "processed", "credit_risk_data.csv")
    model_file = os.path.join("models", "credit_risk_model.pkl")
    
    try:
        # Train the model (assuming train_model is defined elsewhere)
        train_model(data_file, model_file)

        # Evaluation (ensure variables like X_test, y_test, y_pred are available)
        y_scores = model.predict_proba(X_test)[:, 1]
        plot_roc_curve(y_test, y_scores, curve_color="green")
        plot_confusion_matrix(y_test, y_pred, cmap="Oranges")
    except Exception as e:
        print(f"An error occurred: {e}")