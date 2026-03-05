import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LassoCV


data = fetch_california_housing()
X = data.data
y = data.target
feature_names = np.array(data.feature_names)

lasso_cv_model = LassoCV(cv=5, random_state=42)
lasso_cv_model.fit(X, y)

optimal_alpha = lasso_cv_model.alpha_
coefs = lasso_cv_model.coef_


zeroed_mask = np.abs(coefs) < 1e-6
zeroed_count = np.sum(zeroed_mask)

active_mask = np.abs(coefs) >= 1e-6
active_count = np.sum(active_mask)
active_features = feature_names[active_mask]


print( optimal_alpha)
print(f"Liczba wyzerowanych cech: {zeroed_count}")
print(f"Liczba niezerowych cech: {active_count}")
print(f"Lista aktywnych cech: {list(active_features)}")