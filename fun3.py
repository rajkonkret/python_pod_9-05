a = 10
b = 10


def dodaj():
    a = 6  # to jest wewnetrne a, nienadpisujemy a z głownego programu
    b = 7
    print(a + b)


def dodaj2():
    a = 6
    b = 7
    return a + b


def dodaj3():
    global a  # uzyj zmiennej globalnej a wewnatrz funkcji
    a = 6
    b = 7
    print(a + b)


def dodaj4(a):
    b = 7
    print(a + b)


print("Zmienna a z góry", a)
dodaj()
print("Zmienna a z góry", a)
print(dodaj2())
print("Zmienna a z góry", a)
dodaj3()
print("Zmienna a z góry", a)  # a globalne wynosi 6
dodaj4(a)  # 6 + 7 a nie 10 + 7
