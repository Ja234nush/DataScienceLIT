import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(eta, n_iterations=30, x_start=5):
    history = []
    x = x_start
    for _ in range(n_iterations):
        history.append(x**2)
        gradient = 2 * x
        x = x - eta * gradient
    return history

learning_rates = [0.001, 0.01, 0.1, 0.5, 1.0, 1.5]
iterations = range(30)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

for eta in learning_rates:
    ax1.plot(iterations, gradient_descent(eta), label=f'η = {eta}')
ax1.set_xlabel("Iteracja")
ax1.set_ylabel("Wartość f(x)")
ax1.legend()
ax1.grid(True)

for eta in learning_rates[:-1]:
    ax2.plot(iterations, gradient_descent(eta), label=f'η = {eta}')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()