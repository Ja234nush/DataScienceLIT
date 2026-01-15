class Akcja:
    def __init__(self,nazwa, cena_kupna, cena_aktualna):
        self.nazwa = nazwa
        self.cena_kupna = cena_kupna
        self.cena_aktualna = cena_aktualna

    def __str__(self):
        return f"{self.nazwa} (Kupno: {self.cena_kupna}, Teraz: {self.cena_aktualna})"

class Portfel:
    def __init__(self, kapital_poczatkowy):
        self.kapital_poczatkowy = kapital_poczatkowy
        self.gotowka = kapital_poczatkowy
        self.akcje = []

    def kup_akcje(self,akcja, ilosc):
        koszt = akcja.cena_kupna * ilosc
        if koszt > self.gotowka:
            print(f"[BŁĄD] Za mało gotówki na zakup {ilosc} akcji {akcja.nazwa}!")
            return

        self.gotowka -= koszt
        znaleziono = False
        for pozycja in self.akcje:
            if pozycja['obiekt'].nazwa == akcja.nazwa:
                pozycja['ilosc'] += ilosc
                znaleziono = True
                break

        if not znaleziono:
            self.akcje.append({'obiekt': akcja, 'ilosc': ilosc})

        print(f"[KUPNO] Kupiono {ilosc} szt. {akcja.nazwa}. Zostalo gotówki: {self.gotowka:.2f}")

    def sprzedaj_akcje(self, akcja_obj, ilosc):
        for pozycja in self.akcje:
            if pozycja['obiekt'].nazwa == akcja_obj.nazwa:
                if pozycja['ilosc'] >= ilosc:
                    przychody = akcja_obj.cena_aktualna * ilosc
                    self.gotowka += przychody
                    pozycja['ilosc'] -= ilosc

                    if pozycja['ilosc'] == 0:
                        self.akcje.remove(pozycja)

                    print(f"[SPRZEDAŻ] Sprzedano {ilosc} szt. {akcja_obj.nazwa}. Przychód: {przychody:.2f}")
                    return
                else:
                    print(f"[BŁĄD] Masz tylko {pozycja['ilosc']} sztuk {akcja_obj.nazwa}!")
                    return
        print(f"[BŁĄD] Nie posiadasz akcji {akcja_obj.nazwa}!")

    def aktualizuj_ceny(self, slownik_cen):
        for pozycja in self.akcje:
            nazwa = pozycja['obiekt'].nazwa
            if nazwa in slownik_cen:
                pozycja['obiekt'].cena_aktualna = slownik_cen[nazwa]
        print("[INFO] Ceny akcji zostały zaktualizowane.")

    def wartosc_portfela(self):
        wartosc_akcji = 0
        for pozycja in self.akcje:
            wartosc_akcji += pozycja['obiekt'].cena_aktualna * pozycja['ilosc']
        return self.gotowka + wartosc_akcji

    def zysk_strata(self):
        return self.wartosc_portfela() - self.kapital_poczatkowy

    def pokaz_status(self):
        print(f"\n--- STATUS PORTFELA ---")
        print(f"Gotówka: {self.gotowka:.2f}")
        print("Akcje:")
        for p in self.akcje:
            print(f" - {p['obiekt'].nazwa}: {p['ilosc']} szt. (Cena akt.: {p['obiekt'].cena_aktualna})")

        wynik = self.zysk_strata()
        print(f"Całkowita wartość: {self.wartosc_portfela():.2f}")
        print(f"Wynik (Zysk/Strata): {wynik:+.2f}")
        print("-" * 25)
moj_portfel = Portfel(10000)

apple = Akcja("Apple", 150, 150)
tesla = Akcja("Tesla", 200, 200)
microsoft = Akcja("Microsoft", 300, 300)

moj_portfel.kup_akcje(apple, 10)
moj_portfel.kup_akcje(tesla, 5)
moj_portfel.kup_akcje(microsoft, 20)


moj_portfel.pokaz_status()


nowe_ceny = {
    "Apple": 160,       # +10 zł
    "Tesla": 180,       # -20 zł
    "Microsoft": 310    # +10 zł
}
moj_portfel.aktualizuj_ceny(nowe_ceny)

moj_portfel.sprzedaj_akcje(apple, 5)   # Sprzedajemy połowę Apple z zyskiem
moj_portfel.sprzedaj_akcje(tesla, 5)   # Sprzedajemy całą Teslę ze stratą (stop loss)

moj_portfel.pokaz_status()