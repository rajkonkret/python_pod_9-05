lista = []  # tworzenie pustej listy

lista.append("Radek")
lista.append("Tomek")
lista.append("Asia")
lista.append("Renata")
lista.append("Darek")

# ['Radek', 'Tomek', 'Asia', 'Renata', 'Darek']
print(lista)

# zamiana elementu na indeksie 1
# ['Radek', 'Magda', 'Asia', 'Renata', 'Darek']
lista[1] = "Magda"
print(lista)

# usuniecie elemntu "Asia" z listy
# ['Radek', 'Magda', 'Renata', 'Darek']
lista.remove("Asia")
print(lista)
print(lista.append("A"))  # None - nic nie zwraca metoda

print(lista)
# ['Radek', 'Magda', 'Renata', 'Darek', 'A']
# dodanie elemntu na indeksie 1, nie zamienia elemntu w liscie
lista.insert(1, "Piotr")
# ['Radek', 'Piotr', 'Magda', 'Renata', 'Darek', 'A']
print(lista)

liczby2 = lista.copy()  # kopia listy
print(liczby2)
# tu tylko kopia referencji wiec obie działąja na tym samej komórce w pamieci
# liczby2 = lista
# print(liczby2)
# lista.append(4)
# print(liczby2)


liczby = [54, 999, 34, 22, 12.54, 876]
print(liczby)
liczby.sort()
print(liczby)
liczby.reverse()
print(liczby)
liczby3 = liczby.copy()  # kopia listy (nowa lista z elemntami ze starej listy)
liczby.clear()
print(liczby3)
print(liczby)

liczby3[0] = 6666
# [6666, 876, 54, 34, 22, 12.54]
print(liczby3)
[6666, 876, 54]
print(liczby3[0:3])  # wypisanie elemntów od indeksu 0 do 2
# [6666, 876, 54]
print(liczby3[:3])
# [54, 34, 22, 12.54]
print(liczby3[2:])  # od indeksu 2 (włącznie) do końca (włacznie)
# [6666, 876, 54, 34, 22]
print(liczby3[:-1])  # od indeksu 0 do indeksu -1
# [6666, 876, 54, 34]
print(liczby3[:-2])  # od indeksu 0 do indeksu -2

print(len(liczby3))  # długosc kolekcji
liczby3.remove(54)

print(len(liczby3))
print(liczby3)

krotka = tuple(liczby3)
print(krotka)
print(type(krotka))  # <class 'tuple'>
