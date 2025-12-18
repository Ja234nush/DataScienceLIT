filmy_gatunki = {
    'Matrix': ['Akcja', 'Sci-Fi'],
    'Shrek': ['Komedia', 'Familijny', 'Animacja'],
    'Inception': ['Akcja', 'Sci-Fi', 'Thriller'],
    'Toy Story': ['Animacja', 'Familijny'],
    'Die Hard': ['Akcja', 'Thriller'],
    'The Hangover': ['Komedia']
}

gatunki_filmy = {}
for film, lista_gatunkow in filmy_gatunki.items():
    for gatunek in lista_gatunkow:
        if gatunek not in gatunki_filmy:
            gatunki_filmy[gatunek] = set()

        gatunki_filmy[gatunek].add(film)

print("\nWynik (Gatunek -> Filmy):")
for gatunek, zbior_filmow in gatunki_filmy.items():
    filmy_string = ", ".join(sorted(list(zbior_filmow)))
    print(f" - {gatunek}: [{filmy_string}]")