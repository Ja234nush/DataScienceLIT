import pandas as pd
import numpy as np
url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df=pd.read_csv(url)
df.info()
srednia_age = df['Age'].mean()
#df.describe()
#2
# print(df['Age'].mean())
#4
#print(len(df[(df['Age']<18) & (df['Survived']==1)]))
#print(df[(df['Age']<18) & (df['Survived']==1)][['Age','Name']])
#data=df.isna().sum()
#print(data[data>89])
df['Age'] = df['Age'].fillna(srednia_age)
liczba_brakow = df['Age'].isna().sum()
print(liczba_brakow)