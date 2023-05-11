# klasy
class Human:
    """
    Klasa Human opisująca czlowieka w Pythonie
    """
    imie = ""
    wiek = None
    wzrost = None
    plec = ""

    def powitanie(self):
        """
        metoda w klasie Human
        :return: print z imieniem
        """
        print("Nazywam się", self.imie)

    def moj_wiek(self):
        print("Nazywam się", self.imie, "Mam", self.wiek, "lat(a)")


# wyswietlenie opsiu z dokumentacji
# print(Human.__doc__)
#
# print(print.__doc__)
# tworzymy obiekt klasy Human
cz1 = Human()
print(cz1.__doc__)
print(cz1.plec)
cz1.plec = "k"
cz1.wiek = 44
cz1.imie = "Magda"
cz1.wzrost = 170
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)
print(cz1.wzrost)
cz1.powitanie()
cz1.moj_wiek()