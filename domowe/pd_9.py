import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

total_age_sum = 0
total_count = 0
batch_num = 1

for chunk in pd.read_csv(url, chunksize=100):
    batch_mean = chunk['Age'].mean()

    print(f"Batch {batch_num}: wiek = {batch_mean:.2f}")

    total_age_sum += chunk['Age'].sum()
    total_count += chunk['Age'].count()

    batch_num += 1

global_mean = total_age_sum / total_count

print (global_mean)
