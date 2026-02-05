import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
df = pd.read_csv(url, sep=';')

col = 'alcohol'

mean_val = df[col].mean()
std_val = df[col].std()
z_scores = (df[col] - mean_val) / std_val

outliers_mask = np.abs(z_scores) > 3
df_outliers = df[outliers_mask]
df_cleaned = df[~outliers_mask].copy()

stats_before = df[col].agg(['mean', 'median', 'std'])
stats_after = df_cleaned[col].agg(['mean', 'median', 'std'])

comparison = pd.DataFrame({
    'Przed usunięciem': stats_before,
    'Po usunięciu': stats_after
})
print(comparison)

plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.boxplot(df[col], patch_artist=True, boxprops=dict(facecolor='lightcoral'))
plt.title('Przed usunięciem outlierów')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.subplot(1, 2, 2)
plt.boxplot(df_cleaned[col], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Po usunięciu (|z| > 3)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()