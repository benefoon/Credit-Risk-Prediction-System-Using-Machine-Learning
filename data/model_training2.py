from sklearn.model_selection import GridSearchCV

def optimize_hyperparameters(X_train, y_train):
    """Optimize hyperparameters using Grid Search."""
    param_grid = {
        "n_estimators": [50, 100, 200],
        "max_depth": [None, 10, 20],
        "min_samples_split": [2, 5, 10],
    }
    grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, scoring="roc_auc", verbose=2)
    grid_search.fit(X_train, y_train)
    print(f"Best Parameters: {grid_search.best_params_}")
    return grid_search.best_estimator_

if __name__ == "__main__":
    # Optimize the model
    best_model = optimize_hyperparameters(X_train, y_train)
    best_model.fit(X_train, y_train)
    joblib.dump(best_model, "models/optimized_credit_risk_model.pkl")
