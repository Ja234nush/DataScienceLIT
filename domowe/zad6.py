import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df['Family_Size'] = df['SibSp'] + df['Parch'] + 1


survival_by_family = df.groupby('Family_Size')['Survived'].mean()

best_size = survival_by_family.idxmax()
best_rate = survival_by_family.max()

print(survival_by_family.round(2))

print(f"Największą szansę przeżycia  {best_size}")
print(f"Wynosil: {best_rate:.2%}")


survival_by_family.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Szansa przeżycia a wielkość rodziny')
plt.ylabel('Survival Rate')
plt.xlabel('Liczba osób w rodzinie')
plt.show()