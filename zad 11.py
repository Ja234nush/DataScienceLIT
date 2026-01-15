class Uczen:
    def __init__(self, imie, oceny):
        self.imie = imie
        self.oceny = oceny
    def oblicz_srednia(self):
        if len(self.oceny) ==0:
            return 0
        return sum(self.oceny)/len(self.oceny)
    def __str__(self):
        return f'{self.imie} {self.oceny}'
class Klasa:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.uczniowie = []

    def dodaj_ucznia(self, uczen):
        self.uczniowie.append(uczen)

    def srednia_klasy(self):
        wszystkie_oceny = []
        for uczen in self.uczniowie:
            wszystkie_oceny.extend(uczen.oceny)

        if not wszystkie_oceny:
            return 0
        return sum(wszystkie_oceny) / len(wszystkie_oceny)

    def najlepszy_uczen(self):
        if not self.uczniowie:
            return None

        najlepszy_temp = self.uczniowie[0]
        najwyzsza_srednia = najlepszy_temp.oblicz_srednia()

        for uczen in self.uczniowie:
            aktualna_srednia = uczen.oblicz_srednia()

            if aktualna_srednia > najwyzsza_srednia:
                najwyzsza_srednia = aktualna_srednia
                najlepszy_temp = uczen

        return najlepszy_temp.__str__()

klasa_3a = Klasa("3A")

# Tworzenie 5 uczniów z ocenami
u1 = Uczen("Janek", [4, 5, 3, 4])
u2 = Uczen("Zosia", [5, 5, 6, 5])
u3 = Uczen("Bartek", [2, 3, 2, 4])
u4 = Uczen("Kasia", [4, 4, 4, 5])
u5 = Uczen("Marek", [3, 3, 4, 3])

# Dodawanie uczniów do klasy
klasa_3a.dodaj_ucznia(u1)
klasa_3a.dodaj_ucznia(u2)
klasa_3a.dodaj_ucznia(u3)
klasa_3a.dodaj_ucznia(u4)
klasa_3a.dodaj_ucznia(u5)

# Wyświetlanie statystyk
print("\n--- WYNIKI ZADANIA 2 ---")
print(f"Klasa: {klasa_3a.nazwa}")
print(f"Liczba uczniów: {len(klasa_3a.uczniowie)}")
print(f"Średnia ocen całej klasy: {klasa_3a.srednia_klasy():.2f}")
print(f"Najlepszy uczeń: {klasa_3a.najlepszy_uczen()}")