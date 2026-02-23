import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(42)
X = 2 * np.random.rand(50, 1)
y = 3 * X + 2 + np.random.randn(50, 1)

X_mean, Y_Mean=np.mean(X, 0), np.mean(y, 0)
w=np.sum((X-X_mean)*(y-Y_Mean))/np.sum((X-X_mean)**2)
b=Y_Mean-w*X_mean

model=LinearRegression().fit(X, y)

print(w)
print(b)
print(model.coef_)
print(model.intercept_)
