import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X = iris.data
y = iris.target

models = {
    'kNN (k=5)': KNeighborsClassifier(n_neighbors=5),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42)
}

mean_accuracies = []
std_accuracies = []
model_names = list(models.keys())

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

    mean_accuracies.append(scores.mean())
    std_accuracies.append(scores.std())

best_idx = np.argmax(mean_accuracies)
best_model_name = model_names[best_idx]
best_model_score = mean_accuracies[best_idx]

for name, mean, std in zip(model_names, mean_accuracies, std_accuracies):
    print(f"{name:<15}: {mean:.4f} (+/- {std:.4f})")

print(f"\nNajlepszy algorytm: {best_model_name} (Średnia dokładność: {best_model_score:.4f})")

plt.figure(figsize=(9, 6))

plt.bar(model_names, mean_accuracies, yerr=std_accuracies, capsize=8,
        color=['#4C72B0', '#55A868', '#C44E52'], alpha=0.8, edgecolor='black')

plt.ylim(0.85, 1.05)

plt.ylabel('Accuracy')
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, v in enumerate(mean_accuracies):
    plt.text(i, v + std_accuracies[i] + 0.005, f"{v:.3f}", ha='center', fontweight='bold')

plt.tight_layout()
plt.show()