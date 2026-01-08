import math

zakres = 101
liczby_pierwsze = []
for liczba in range(2, zakres):
    jest_pierwsza = True
    for i in range(2, int(math.sqrt(liczba))+1):
        if liczba % i == 0:
            jest_pierwsza = False
            break

    if jest_pierwsza:
        liczby_pierwsze.append(liczba)

print(f"Wynik: {liczby_pierwsze}")