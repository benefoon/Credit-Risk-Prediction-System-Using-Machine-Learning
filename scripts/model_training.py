import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score
import joblib

def optimize_hyperparameters(X_train, y_train, cv=3, scoring="roc_auc", verbose=2):
    """
    Optimize hyperparameters for RandomForestClassifier using Grid Search.
    
    Parameters:
    - X_train: Features for training
    - y_train: Target labels for training
    - cv: Number of cross-validation folds (default: 3)
    - scoring: Scoring metric for evaluation (default: "roc_auc")
    - verbose: Level of verbosity for GridSearchCV (default: 2)
    
    Returns:
    - best_model: The best estimator found by GridSearchCV
    """
    # Define the parameter grid for hyperparameter tuning
    param_grid = {
        "n_estimators": [50, 100, 200],
        "max_depth": [None, 10, 20],
        "min_samples_split": [2, 5, 10],
    }
    
    # Initialize the GridSearchCV object
    grid_search = GridSearchCV(
        estimator=RandomForestClassifier(random_state=42),
        param_grid=param_grid,
        cv=cv,
        scoring=scoring,
        verbose=verbose
    )
    
    try:
        # Perform the grid search
        grid_search.fit(X_train, y_train)
        print(f"Best Parameters: {grid_search.best_params_}")
        return grid_search.best_estimator_
    except Exception as e:
        print(f"An error occurred during hyperparameter optimization: {e}")
        return None

def save_model(model, filepath="models/optimized_model.pkl"):
    """
    Save the trained model to the specified filepath.
    
    Parameters:
    - model: Trained model to save
    - filepath: Filepath to save the model (default: "models/optimized_model.pkl")
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    try:
        joblib.dump(model, filepath)
        print(f"Model saved to {filepath}")
    except Exception as e:
        print(f"An error occurred while saving the model: {e}")

if __name__ == "__main__":
    # Replace X_train and y_train with your actual training data
    X_train = None  # Placeholder for training features
    y_train = None  # Placeholder for training labels
    
    # Ensure that training data is provided
    if X_train is not None and y_train is not None:
        # Optimize the model
        best_model = optimize_hyperparameters(X_train, y_train)
        
        if best_model:
            # Save the best model
            save_model(best_model, "models/optimized_credit_risk_model.pkl")
    else:
        print("Training data (X_train, y_train) is not provided.")
