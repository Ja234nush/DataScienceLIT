produkty = {
    'jabłko': 3.50,
    'banan': 2.20,
    'pomarańcza': 4.00
}

print("Przed zmianami:", produkty)

produkty['gruszka'] = 3.80

del produkty['banan']

produkty['jabłko'] = 3.20

print("Po zmianach:", produkty)
