import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

X, y = make_regression(n_samples=200, n_features=1, noise=20, random_state=42)
X = X.flatten()


def predict(X, w, b):
    return w * X + b


def compute_mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def compute_gradients(X, y, y_pred):
    dw = -2 * np.mean(X * (y - y_pred))
    db = -2 * np.mean(y - y_pred)
    return dw, db


w, b = 0.5, 0.1
learning_rate = 0.4
n_iterations = 100
loss_history = []

for i in range(n_iterations):
    y_pred = predict(X, w, b)
    loss = compute_mse(y, y_pred)
    loss_history.append(loss)

    dw, db = compute_gradients(X, y, y_pred)
    w -= learning_rate * dw
    b -= learning_rate * db

model_sk = LinearRegression()
model_sk.fit(X.reshape(-1, 1), y)

print(f"Manualne - w: {w:.4f}, b: {b:.4f}")
print(f"Sklearn  - w: {model_sk.coef_[0]:.4f}, b: {model_sk.intercept_:.4f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

ax1.scatter(X, y, color='silver', label='Dane')
ax1.plot(X, predict(X, w, b), color='red', linewidth=2)
ax1.set_title("Dopasowanie linii regresji")
ax1.legend()

ax2.plot(loss_history, color='blue')
ax2.set_title("Krzywa uczenia")
ax2.set_xlabel("Iteracja")
ax2.set_ylabel("MSE")

plt.show()