import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import StratifiedKFold, cross_val_score, cross_validate
from sklearn.linear_model import LogisticRegression

data = load_breast_cancer()
X, y = data.data, data.target

model = LogisticRegression(max_iter=10000, random_state=42)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

accuracy_cv_score = cross_val_score(model, X, y, cv=cv, scoring='accuracy')

scoring_metrics = ['accuracy', 'precision', 'recall', 'f1']
cv_results = cross_validate(model, X, y, cv=cv, scoring=scoring_metrics)

# Przygotowanie słownika z wynikami dla łatwiejszego przetwarzania
metrics_dict = {
    'Accuracy': cv_results['test_accuracy'],
    'Precision': cv_results['test_precision'],
    'Recall': cv_results['test_recall'],
    'F1': cv_results['test_f1']
}

# --- Oczekiwany rezultat 1: Tabela z metrykami (mean ± std) ---
print("Tabela metryk z Walidacji")
print("-" * 50)
print(f"{'Metryka':<15} | {'Średnia':<15} | {'Odchylenie'}")
print("-" * 50)

for metric_name, scores in metrics_dict.items():
    mean_score = np.mean(scores)
    std_score = np.std(scores)
    print(f"{metric_name:<15} | {mean_score:.4f}          | ± {std_score:.4f}")
print("-" * 50)


plt.figure(figsize=(10, 6))

plt.boxplot(metrics_dict.values(), labels=metrics_dict.keys(), patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red', linewidth=2))

plt.title('Rozkład metryk klasyfikacji w 5-krotnej Walidacji Krzyżowej', fontsize=14)
plt.ylabel('Wartość metryki', fontsize=12)
plt.xlabel('Rodzaj metryki', fontsize=12)
plt.ylim(0.85, 1.0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()