# {'name': 'Raadek}

slownik = {}  # pusty słownik
print(type(slownik))  # <class 'dict'>
slownik['imie'] = "Radek"
slownik['imie'] = "Tomek"
slownik['wiek'] = 39

# {'imie': 'Tomek', 'wiek': 39}
print(slownik)

print(slownik.items())
print(slownik.values())
print(slownik.keys())

print(slownik['imie'])

lista = [44, 55, 66, 77, 88, 33, 22, 11, 55, 33, 11]
# dodajemy liste do słownika pod klucz: 'liczby'
slownik['liczby'] = lista
# {'imie': 'Tomek', 'wiek': 39, 'liczby': [44, 55, 66, 77, 88, 33, 22, 11, 55, 33, 11]}
print(slownik)
print(slownik['liczby'])
print(slownik['liczby'][0])

lista2 = [44, 55, 66, 11]
nowa_lista = lista + lista2
print(nowa_lista)

slownik2 = {'imie': 'Radek', 'wiek': 39}
print(slownik2)
print(type(slownik2))  # <class 'dict'>

slownik3 = {'imie': 'name', 'kot': 'cat'}
print(slownik3['imie'])
slownik3.update({'pies': 'dog'})  # dodanie el do słownika za pomocą update()
print(slownik3)
print("Umiem przetłumaczyć:", slownik3.keys())
key = input("Podaj wyraz")  # wczytanie wyrazu od użytkownika
print(slownik3[key.lower().replace(" ", "")])
