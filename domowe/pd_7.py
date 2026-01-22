import pandas as pd
import numpy as np
url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df=pd.read_csv(url)
df = df[['Name', 'Age', 'Survived']]
oldest=df.sort_values(by=['Age'],ascending=False).head(10)
youngest=df.sort_values(by=['Age'],ascending=True).head(10)
print(oldest)
print(youngest)