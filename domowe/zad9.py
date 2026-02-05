import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# 1. Parametry
n, p = 20, 0.5
n_experiments = 1000

data = np.random.binomial(n, p, n_experiments)

mean_empiric = np.mean(data)
mean_theoretic = n * p

print(f"Średnia praktyczna: {mean_empiric}")
print(f"Średnia teoretyczna: {mean_theoretic}")

plt.figure(figsize=(10, 6))

plt.hist(data, bins=np.arange(data.min(), data.max() ) - 0.5,
         density=True, color='skyblue')

x = np.arange(0, n + 1)
plt.stem(x, binom.pmf(x, n, p), linefmt='r-', markerfmt='ro', basefmt=" ", label='Teoretyczny PMF')

plt.xlabel("Liczba sukcesów")
plt.ylabel("Prawdopodobieństwo")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()