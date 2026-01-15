class BankAccount:
    def __init__(self, wlasciciel, saldo_poczatkowe=0):

        self.wlasciciel = wlasciciel
        self.saldo = saldo_poczatkowe

    def wplac(self, kwota):

        if kwota > 0:
            self.saldo += kwota
            print(f"[Wpłata] Wpłacono {kwota} zł na konto {self.wlasciciel}.")
        else:
            print("Kwota wpłaty musi być dodatnia.")

    def wyplac(self, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
            print(f"[Wypłata] Wypłacono {kwota} zł z konta {self.wlasciciel}.")
        else:
            print(f"[Błąd] Brak wystarczających środków u {self.wlasciciel}. Chcesz wypłacić {kwota}, a masz {self.saldo}.")

    def pokaz_saldo(self):
        print(f"Saldo konta ({self.wlasciciel}): {self.saldo} zł")


konto1 = BankAccount("Jan Kowalski", 1000)

konto1.pokaz_saldo()
konto1.wplac(500)
konto1.wyplac(200)
konto1.pokaz_saldo()
konto1.wyplac(2000)

print("-" * 30)

konto2 = BankAccount("Anna Nowak", 0)

konto2.pokaz_saldo()
konto2.wplac(100)
konto2.wyplac(50)
konto2.pokaz_saldo()