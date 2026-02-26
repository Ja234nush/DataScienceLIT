import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score

# 1. Wygenerowanie danych
# Niezbalansowany dataset: 95% klasa 0, 5% klasa 1
X, y = make_classification(
    n_samples=10000,
    n_features=20,
    n_classes=2,
    weights=[0.95, 0.05],
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)


y_probs = model.predict_proba(X_test)[:, 1]

thresholds = np.arange(0.1, 1.0, 0.1)
precisions = []
recalls = []
f1_scores = []

for threshold in thresholds:
    y_pred_adj = (y_probs >= threshold).astype(int)

    precisions.append(precision_score(y_test, y_pred_adj, zero_division=0))
    recalls.append(recall_score(y_test, y_pred_adj, zero_division=0))
    f1_scores.append(f1_score(y_test, y_pred_adj, zero_division=0))

best_f1_idx = np.argmax(f1_scores)
best_f1_threshold = thresholds[best_f1_idx]
print(f"Próg z najlepszym F1-score: {best_f1_threshold:.1f} (F1 = {f1_scores[best_f1_idx]:.3f})")

valid_indices = [i for i, p in enumerate(precisions) if p > 0.5]
if valid_indices:

    best_recall_idx = max(valid_indices, key=lambda i: recalls[i])
    best_recall_threshold = thresholds[best_recall_idx]
    print(f"Próg Recall przy Precision > 0.5: {best_recall_threshold:.1f}")
    print(f"  -> Recall = {recalls[best_recall_idx]:.3f}, Precision = {precisions[best_recall_idx]:.3f}")
else:
    print("Nie znaleziono progu, dla którego Precision > 0.5")
    best_recall_threshold = None

plt.figure(figsize=(10, 6))
plt.plot(thresholds, precisions, label='Precision', marker='o')
plt.plot(thresholds, recalls, label='Recall', marker='s')
plt.plot(thresholds, f1_scores, label='F1 Score', marker='^', linestyle='--')



plt.title('Precision-Recall Trade-off (Dataset 95:5)')
plt.xlabel('Próg decyzyjny (Threshold)')
plt.ylabel('Wartość metryki')
plt.xticks(thresholds)
plt.legend()
plt.grid(True)
plt.show()