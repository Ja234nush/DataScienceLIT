import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing, make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeCV, LassoCV, ElasticNetCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

results = []


def evaluate_models(X, y, dataset_name):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        'RidgeCV': Pipeline([
            ('scaler', StandardScaler()),
            ('model', RidgeCV(alphas=np.logspace(-4, 4, 100), cv=5))
        ]),
        'LassoCV': Pipeline([
            ('scaler', StandardScaler()),
            ('model', LassoCV(cv=5, random_state=42))
        ]),
        'ElasticNetCV': Pipeline([
            ('scaler', StandardScaler()),
            ('model', ElasticNetCV(cv=5, random_state=42))
        ])
    }

    for name, pipeline in models.items():
        pipeline.fit(X_train, y_train)

        r2_score = pipeline.score(X_test, y_test)

        trained_model = pipeline.named_steps['model']
        non_zero_features = np.sum(np.abs(trained_model.coef_) >= 1e-6)

        results.append({
            'Dataset': dataset_name,
            'Model': name,
            'Test R²': round(r2_score, 4),
            'Niezerowe cechy': non_zero_features,
            'Wszystkie cechy': X.shape[1]
        })


california = fetch_california_housing()
evaluate_models(california.data, california.target, 'California Housing')

X_reg, y_reg = make_regression(n_samples=500, n_features=20, n_informative=10, noise=15.0, random_state=42)
evaluate_models(X_reg, y_reg, 'make_regression (Sparse)')

df_results = pd.DataFrame(results)
print(df_results.to_string(index=False))