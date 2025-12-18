def funckja(lista):
    suma=sum(lista)
    srednia=suma/len(lista)
    minimum=min(lista)
    maximum=max(lista)

    return (suma,srednia,minimum,maximum)

lista_danych = [10, 20, 30, 40, 50]
sum, sr, min, max = funckja(lista_danych)

print(f"Suma: {sum}")
print(f"Średnia: {sr}")
print(f"Minimum: {min}")
print(f"Maksimum: {max}")