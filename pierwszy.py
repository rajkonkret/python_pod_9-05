print()  # wypisz/wydrukuj

print("Mam na imię Radek")
# ctrl + d - powielenie lini
# PEP8
print('Mam na imię Radek')  # str - dane typu tekstowego
print("Mam na imię Radek\'")
# ctrl alt l - wyrownanie kodu

print(39)  # int - liczby całkowite
print(str(39))  # rzutowanie na string(tzw zamiana)

# zmienna
imie = "Radek"
print(imie)
print(type(imie))  # sprawdzenie typu

# hint, podpowiedz o typie zmiennej
wiek: int = 39
print(wiek)
print(type(wiek))  # <class 'int'>
wiek = "Radek"
print(wiek)
print(type(wiek))  # <class 'str'>
