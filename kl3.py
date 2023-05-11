class Car:
    """
    Klasa samochód
    """

    def __init__(self, model, year=2000):
        self.model = model
        self.year = year
        # pole prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def hamuj(self):
        self.__predkosc -= 10

    def licznik(self):
        print("Prędkość wynosi", self.__predkosc)

    def __zmien_bieg(self):
        print("zmiana biegu")


car1 = Car("Opel", '2018')
print(car1.model)
print(car1.year)
# pole predkosc zrobilismy prywatne(__), brak dostępu do pola spoza klasy
# print(car1.predkosc)
car1.licznik()
car1.gaz()
# print(car1.predkosc)
car1.licznik()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# print(car1.predkosc)
car1.licznik()
car1.hamuj()
# print(car1.predkosc)
car1.licznik()
# car1.__predkosc = 0 nie robiu na polu prywatnym nawet jesli srdowisko pozwala
# print(car1.predkosc)
car1.licznik()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()
# 11:25