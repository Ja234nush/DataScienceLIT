data = [78, 82, 85, 88, 90, 92, 95, 97, 99, 45, 101, 103, 105, 180]

sorted_data = sorted(data)
n = len(sorted_data)


def get_median(dataset):
    count = len(dataset)
    mid_idx = count // 2
    if count % 2 == 1:
        return dataset[mid_idx]
    else:
        return (dataset[mid_idx - 1] + dataset[mid_idx]) / 2


split_index = n // 2

lower_half = sorted_data[:split_index]  # Pierwsza połowa
upper_half = sorted_data[split_index:]  # Druga połowa

q1 = get_median(lower_half)
q3 = get_median(upper_half)

iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = [x for x in sorted_data if x < lower_bound or x > upper_bound]

print(f"Posortowane dane: {sorted_data}")
print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Lista outliers: {outliers}")