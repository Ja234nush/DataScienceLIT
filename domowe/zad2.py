import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

iris = load_iris()
X = iris.data
y = iris.target

k_values = range(1, 21)
mean_accuracies = []


for k in k_values:
    knn_model = KNeighborsClassifier(n_neighbors=k)

    scores = cross_val_score(knn_model, X, y, cv=5, scoring='accuracy')

    mean_accuracies.append(scores.mean())


optimal_index = np.argmax(mean_accuracies)
optimal_k = k_values[optimal_index]
max_accuracy = mean_accuracies[optimal_index]


print(f"Optymalnak: {optimal_k}")
print(f"Accuracy: {max_accuracy:.4f}")


plt.figure(figsize=(10, 6))
plt.plot(k_values, mean_accuracies, marker='o', linestyle='-', color='b', label='Średnia dokładność')

plt.plot(optimal_k, max_accuracy, marker='*', color='r', markersize=15,
         label=f'Optymalne k={optimal_k} (Acc: {max_accuracy:.4f})')

plt.xlabel('Wartość k')
plt.ylabel('Średnia dokładność ')
plt.xticks(k_values)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Wyświetlenie wykresu
plt.show()