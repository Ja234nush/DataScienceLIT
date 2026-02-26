import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve

data = load_breast_cancer()
X, y = data.data, data.target

model = LogisticRegression(max_iter=10000, random_state=42)

train_sizes, train_scores, test_scores = learning_curve(
    model, X, y,
    cv=5,
    n_jobs=-1,
    train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='accuracy'
)

train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

plt.figure(figsize=(10, 6))

plt.plot(train_sizes, train_scores_mean, 'o-', color="red", label="Train score")
plt.plot(train_sizes, test_scores_mean, 'o-', color="green", label="Validation score ")


plt.title("Krzywe uczenia)", fontsize=14)
plt.xlabel("Liczba próbek treningowych", fontsize=12)
plt.ylabel("Accuracy (Dokładność)", fontsize=12)
plt.legend(loc="lower right")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()