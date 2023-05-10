# petla for
import random

lista2 = list(range(1, 50))
print(lista2)
lista3 = []

for i in range(6):  # 0..5  0 1 2 3 4 5
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    lista3.append(wyn)

print(lista3)

lista_p = []
for i in range(10):  # 0..9
    if i % 2 == 0:  # reszta z dzielenia
        print("Jest parzysta")
        print(i)
        lista_p.append(i)

print(lista_p)

lista_p2 = [j for j in range(10) if j % 2 == 0]
print(lista_p2)

print(lista_p)

for c in lista_p:
    if c == 2:
        c += 1  # c = c + 1
    print(c)

print(c)

imiona = ["Radek", "Zenek", "Monika"]

for p in imiona:
    print(p)

for p in range(len(imiona)):  # 0..2 range(3)
    print(p, imiona[p])

# enumerate - zwraca index i element kolekcji
for pozycja, osoba in enumerate(imiona):  # pozycja, osoba -> p, imiona[p]
    print(pozycja, osoba)

ludzie = ['Radek', 'Janek', 'Asia', 'Michał']
wiek = [47, 67, 32, 34]

for p, o in enumerate(ludzie):
    # p - kolejne indexy z listy ludzie
    # o - kolejne elemnty z listy ludzie
    print(p, o, wiek[p])

for i, (o, w) in enumerate(zip(ludzie, wiek)):
    print(i, o, w)

for i in range(0, 10, 2):  # 0..9 co 2, start, stop, krok
    print(i)
