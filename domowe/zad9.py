import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

# 1. Generowanie danych (tym razem z wieloma cechami)
X_raw, y = make_regression(n_samples=200, n_features=2, noise=15, random_state=42)
y = y.reshape(-1, 1)

# Dodajemy kolumnę jedynek do X, aby obsłużyć bias (b) jako jedną z wag
X = np.c_[np.ones((X_raw.shape[0], 1)), X_raw]

# 2. Inicjalizacja wag jako wektora (liczba cech + 1 dla biasu)
w = np.zeros((X.shape[1], 1))


# 3. Funkcje wektorowe
def predict(X, w):
    return np.dot(X, w)  # Iloczyn macierzowy: y = X * w


def compute_mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def compute_gradients(X, y, y_pred):
    m = len(y)
    # Wzór wektorowy na gradient: (2/m) * X^T * (y_pred - y)
    dw = (2 / m) * np.dot(X.T, (y_pred - y))
    return dw


# 4. Pętla treningowa
learning_rate = 0.1
n_iterations = 100
loss_history = []

for i in range(n_iterations):
    y_pred = predict(X, w)
    loss = compute_mse(y, y_pred)
    loss_history.append(loss)

    dw = compute_gradients(X, y, y_pred)
    w -= learning_rate * dw

print("Finalny wektor wag (w tym w0 jako bias):")
print(w)