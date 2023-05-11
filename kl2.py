class Human:
    """
    Dokumentacje
    """

    # konstruktor
    def __init__(self, imie, wiek, wzrost, plec):
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print("Nazywam się", self.imie)

    def moj_wzrost(self):
        print("Nazywam się", self.imie, "Mam", self.wzrost, "cm wzrostu")

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


cz1 = Human("Radek", "48", "193", "m")
print(cz1.plec)
cz1.powitanie()
cz1.moj_wzrost()
cz1.ruszaj()

# drugi obiekt płci przeciwnej niz ten pierwszy i uzyc tych metod
cz2 = Human("Gosia", "24", "169", "k")
cz2.powitanie()
cz2.moj_wzrost()
cz2.ruszaj()
