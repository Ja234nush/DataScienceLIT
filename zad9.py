import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import ElasticNet
from sklearn.metrics import r2_score

california = fetch_california_housing()
X, y = california.data, california.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(X_train)
x_test_scaled = scaler.transform(X_test)

l1_ratios=[0, 0.25, 0.5, 0.75, 1]
alpha_val = 0.1
results = []

for l1_ratio in l1_ratios:
    model=ElasticNet(alpha=alpha_val, l1_ratio=l1_ratio,  random_state=42)
    model.fit(x_train_scaled, y_train)
    y_pred = model.predict(x_test_scaled)
    r2 = r2_score(y_test, y_pred)
    results.append((r2,l1_ratio))

print(results)

