import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

data = load_breast_cancer()
X = data.data
y = data.target
feature_names = data.feature_names

tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X, y)

forest_model = RandomForestClassifier(random_state=42)
forest_model.fit(X, y)


tree_importances = tree_model.feature_importances_
forest_importances = forest_model.feature_importances_

top10_tree_idx = np.argsort(tree_importances)[-10:]
top10_forest_idx = np.argsort(forest_importances)[-10:]

fig, axes = plt.subplots(1, 2, figsize=(15, 6))


axes[0].barh(range(10), tree_importances[top10_tree_idx], align='center', color='skyblue')
axes[0].set_yticks(range(10))
axes[0].set_yticklabels(feature_names[top10_tree_idx])
axes[0].set_xlabel('Ważność cechy')



axes[1].barh(range(10), forest_importances[top10_forest_idx], align='center', color='lightgreen')
axes[1].set_yticks(range(10))
axes[1].set_yticklabels(feature_names[top10_forest_idx])
axes[1].set_xlabel('Ważność cechy')



plt.tight_layout()
plt.show()