from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkościa", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Orzel(Ptak):
    """
    klasa orzeł
    """

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")

    def wydaj_odglos(self):
        print("piiiiiiiiiii")


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")

    def wydaj_odglos(self):
        print("kokokokokoko")

# @abstractmethod - powoduje, ze kalsa jest abstrakcyjna i nie mozna utworzyć obiektu klasy Ptak
# orzel = Ptak("Orzeł", 20)
# orzel.latam()
# kura = Ptak("Kura", 0)
# kura.latam()
orz2 = Orzel("Orzeł", 20)
orz2.latam()
orz2.poluj()
kur2 = Kura("Kura")
kur2.latam()
kur2.dziobanie()
orz2.wydaj_odglos()
kur2.wydaj_odglos()