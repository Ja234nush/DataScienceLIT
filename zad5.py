class Student:
    def __init__(self, imie, indeks):
        self.imie = imie
        self.indeks = indeks
        self.oceny = []

    def dodajOcene(self, ocena):
        self.oceny.append(ocena)
    def srednia(self):
        if len(self.oceny) ==0:
            return 0
        return sum(self.oceny)/len(self.oceny)
    def __str__(self):
        return f'student:{self.imie}, indeks: {self.indeks}, oceny: {self.oceny}'

student1 = Student("Adam Nowak", "12345")
student2 = Student("Ewa Kowalska", "54321")
student3 = Student("Piotr Wiśniewski", "99887")

student1.dodajOcene(5.0)
student1.dodajOcene(4.5)
student1.dodajOcene(5.0)


student2.dodajOcene(3.0)
student2.dodajOcene(4.0)
student2.dodajOcene(3.5)
student2.dodajOcene(2.0)


student3.dodajOcene(4.0)


print("--- Wyniki studentów ---")
print(student1)
print(student2)
print(student3)

print(f"\nSama średnia Adama: {student1.srednia()}")