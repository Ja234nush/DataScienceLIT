import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeCV

data = fetch_california_housing()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

alphas = np.logspace(-4, 4, 100)

ridge_cv_model = RidgeCV(alphas=alphas, cv=5)
ridge_cv_model.fit(X_train, y_train)

test_r2 = ridge_cv_model.score(X_test, y_test)

print(f"Optymalne alpha: {ridge_cv_model.alpha_:.4f}")
print(f"Test R²: {test_r2:.4f}")