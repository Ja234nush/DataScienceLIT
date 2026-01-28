import pandas as pd
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing(as_frame=True)
df = pd.concat([housing.data, housing.target.rename('MedHouseVal')], axis=1)

def iqr_func(x):
    return x.quantile(0.75) - x.quantile(0.25)

df['Lat_Idx'] = pd.cut(df['Latitude'], bins=5, labels=False)   # Oś Y
df['Lon_Idx'] = pd.cut(df['Longitude'], bins=5, labels=False)  # Oś X

grouped = df.groupby(['Lat_Idx', 'Lon_Idx'])['MedHouseVal'].agg(iqr_func)


iqr_matrix = grouped.unstack()

iqr_matrix = iqr_matrix.sort_index(ascending=False)

print(iqr_matrix)