wartosci = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


min_val = wartosci[0]
max_val = wartosci[0]

for x in wartosci:
    if x < min_val:
        min_val = x
    if x > max_val:
        max_val = x

print(f"Minimum: {min_val}")
print(f"Maksimum: {max_val}")

normalized_list = []
zakres = max_val - min_val  # Mianownik wzoru

for x in wartosci:
    x_norm = (x - min_val) / zakres
    normalized_list.append(x_norm)

print(f"Lista wartości: {wartosci}")
print(f"Znormalizowane: {normalized_list}")
