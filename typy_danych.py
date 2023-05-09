wiek = 47  # int - liczby całkowite
rok = 2023
temp = 36.6  # float - zmiennoprzecinkowy
wiek2 = 37.5

# print(wiek)
# print(type(wiek))
# print(wiek2)
# print(type(wiek2))

print(5 * "Radek")
print(5 * "2")
print(5 * int("2"))  # rzutowanie na int

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek // rok)  # czesc całkowita dzielenia
print(wiek / rok)  # dzielenie ( zawsze zwraca float)
print(type(wiek / rok))  # dzielenie ( zawsze zwraca float)
print(wiek ** rok)  # potęgowanie
print(54 - (5 * 42) + (4 / 2 + 4) / 2)
print("\tSprawdzam zmienną temp: {} {}\n".format(wiek, temp))
# 11:30
print(f"\tSprawdzam zmienną wiek: {wiek} {temp}\n")
print(f"""
    zmienna {wiek}
    zmienna {temp}
    wynik działania:
    {54 - (5 * 43) + (4 / 2 + 4) / 2}
""")
imie = "Radek Radek"
imie.lower()  # zamiana na małe litery
print(imie)
imie2 = imie.lower()
print(imie2)
# upper, cpitalize
print(imie2.upper())
print(imie2.capitalize())
print(imie2)

# czesc całkowita z dzielenia
print(4 // 2)  # int
print(type(4 // 2))  # int
# dzielenie z ulamkiem
print(4 / 2)  # float
print(type(4 / 2))  # float
print(type(5 / 2))  # float

# zmienna logiczna
# typ logiczny
# True , False
czy_znasz_Pythona = True  # prawda
print(czy_znasz_Pythona)
czy_znasz_Pythona = False
print(czy_znasz_Pythona)
print(type(czy_znasz_Pythona))  # <class 'bool'>
print(int(czy_znasz_Pythona))  # 0 - False
print(int(True))  # 1 - True
print(bool(0))  # False
print(bool(1))  # True
print(bool(100))  # True
print(bool(-100))  # True
