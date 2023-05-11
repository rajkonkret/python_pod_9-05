class Dom:
    """
    To jest klasa Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def podaj_metraz(self):
        print("Metraż wynosi", self.__metraz)

    def podaj_okna(self):
        print("Liczba okien wynosi", self.__liczba_okien)

    def podaj_kolor(self):
        print("Mamy kolor", self.__kolor)

    def zmien_metraz(self):
        wybor = int(input("Podaj metraż"))
        self.__metraz = wybor
        print("Metraż wynosi", self.__metraz)

    def zmien_kolor(self):
        wybor = input("Podaj kolor")
        self.__kolor = wybor
        print("Mamy kolor", self.__kolor)
        self.__farba()

    def zmien_okna(self):
        wybor = int(input("Podaj liczbę okien"))
        self.__liczba_okien = wybor
        print("Liczba okien wynosi", self.__liczba_okien)

    def __farba(self):
        print("Skończyła się farba")


dom1 = Dom(134, "zielony", 8)
dom1.podaj_metraz()
dom1.zmien_metraz()
dom1.zmien_kolor()
dom1.zmien_okna()
