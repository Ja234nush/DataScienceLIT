import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.inspection import permutation_importance

california = fetch_california_housing(as_frame=True)
X = california.data
y = california.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler_base = StandardScaler()
X_train_scaled = scaler_base.fit_transform(X_train)
X_test_scaled = scaler_base.transform(X_test)

model_base = Ridge(alpha=1.0)
model_base.fit(X_train_scaled, y_train)
y_pred_base = model_base.predict(X_test_scaled)
r2_base = r2_score(y_test, y_pred_base)


def engineer_features(df):
    df_new = df.copy()

    df_new['MedInc_x_AveRooms'] = df_new['MedInc'] * df_new['AveRooms']
    df_new['log_Population'] = np.log1p(df_new['Population'])
    df_new['log_AveOccup'] = np.log1p(df_new['AveOccup'])
    df_new['log_MedInc'] = np.log1p(df_new['MedInc'])

    df_new['sqrt_AveRooms'] = np.sqrt(df_new['AveRooms'])
    df_new['sqrt_AveBedrms'] = np.sqrt(df_new['AveBedrms'])

    return df_new


X_train_fe = engineer_features(X_train)
X_test_fe = engineer_features(X_test)

new_features_list = [col for col in X_train_fe.columns if col not in X.columns]

scaler_fe = StandardScaler()
X_train_fe_scaled = scaler_fe.fit_transform(X_train_fe)
X_test_fe_scaled = scaler_fe.transform(X_test_fe)

model_fe = Ridge(alpha=1.0)
model_fe.fit(X_train_fe_scaled, y_train)
y_pred_fe = model_fe.predict(X_test_fe_scaled)
r2_fe = r2_score(y_test, y_pred_fe)

improvement = ((r2_fe - r2_base) / r2_base) * 100
result = permutation_importance(model_fe, X_test_fe_scaled, y_test, n_repeats=10, random_state=42)
importance_df = pd.DataFrame({'Feature': X_train_fe.columns, 'Importance': result.importances_mean})
importance_df = importance_df.sort_values(by='Importance', ascending=False)
top_new_features = importance_df[importance_df['Feature'].isin(new_features_list)].head(3)
print(f" - R² przed: {r2_base:.4f}")
print(f" - R² po: {r2_fe:.4f}")
print(f" - Poprawa:  {improvement:.2f}%")

print("\n3. Które nowe cechy najbardziej poprawiły model?")
for index, row in top_new_features.iterrows():
    print(f" - {row['Feature']} (wpływ: {row['Importance']:.4f})")