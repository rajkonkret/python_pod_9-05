# krotka - tupla
# indeks: 0 Tomek, 1 Michał, 2 Asia, 3 Daniel, 4 Gosia
tupla = ("Tomek", "Michał", "Asia", "Daniel", "Gosia",)
tupla2 = ("radek",)  # tupla jednoelementowa
tupla3 = 43, 55, 22.43, 11, 200

print(tupla)
print(type(tupla))
print(type(tupla2))
print(tupla3)
print(type(tupla3))

print(tupla.count("Tomek"))
print(tupla.index("Asia"))
asia = tupla[2]
print(asia)

a, b = 1, 2
print(a)

imie, imie2, imie3, imie4, imie5 = tupla
print(imie)
*a, b = 1, 2, 3  # * - oznacza worek na pozostałe elemnty
print(a)

print(tupla)
# rozpakowanie tupli(krotki)
imie, imie2, *imie3, imie4 = tupla
print(imie)
print(imie2)
print(imie3)
print(imie4)
print(type(imie3))  # <class 'list'>

lista = list(tupla)  # zamiana na listę
print(lista)
