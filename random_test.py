import random

# random - generowanie liczb pseudolosowych

print(random.randint(1, 6))  # int 1..6
print(random.random() * 6)  # float od 0..1(bez 1) * 6 daje od 0..5.99999999
print(random.randrange(6))  # int 0..5
print(random.randrange(1, 6))  # int 1..5

lista = [5, 7, 6, 45, 34, 56]
print(random.choice(lista))

# generowanie listy od 1..49
lista2 = list(range(1, 50))
print(lista2)
lista3 = []

wyn = random.choice(lista2)
lista2.remove(wyn)
lista3.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista3.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista3.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista3.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista3.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista3.append(wyn)

print(lista3)

# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
