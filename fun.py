# funkcje

a = 10
b = 5


# definicja funkcja
def dodaj():
    print(a + b)


def dodaj2(a, b):
    print(a + b)


def odejmij(a, b, c=0):
    print(a - b - c)


# wywołanie funkcji
dodaj()
dodaj2(5, 6)
odejmij(8, 6)
odejmij(8, 6, 5)
odejmij(b=5, a=7, c=1)

print(dodaj())  # zwraca None
