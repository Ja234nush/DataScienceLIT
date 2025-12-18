studenci = [
    ('Anna', 'Kowalska', 5.0, 4.5, 5.0),
    ('Jan', 'Nowak', 3.0, 3.5, 3.0),
    ('Maria', 'Zielińska', 4.0, 4.5, 5.0),
    ('Piotr', 'Wiśniewski', 2.0, 3.0, 2.5),
    ('Ewa', 'Wójcik', 5.0, 5.0, 4.5),
    ('Tomasz', 'Kamiński', 4.0, 3.5, 4.0)
]

wyniki = {
    'wyróżniający': [],
    'dobry': [],
    'średni': []
}

for student in studenci:
    imie = student[0]
    nazwisko = student[1]
    oceny = student[2:]

    srednia = round(sum(oceny) / len(oceny), 2)

    student_output = (imie, nazwisko, srednia)

    if srednia >= 4.5:
        wyniki['wyróżniający'].append(student_output)
    elif srednia >= 3.5:
        wyniki['dobry'].append(student_output)
    else:
        wyniki['średni'].append(student_output)


print("Wyniki grupowania:")
for kategoria, lista_studentow in wyniki.items():
    print(f"\nKategoria: {kategoria.upper()} (liczba osób: {len(lista_studentow)})")
    if not lista_studentow:
        print("  (brak studentów)")
    for s in lista_studentow:
        print(f"  -> {s[0]} {s[1]}, średnia: {s[2]}")