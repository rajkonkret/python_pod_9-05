# set() - przechowuje tylko niepowtarzające sie elemnty
lista = [44, 55, 66, 77, 33, 22, 11, 55, 33, 11]

zbior = set(lista)  # zamina listy na set

print(lista)
print(zbior)

zbior1 = set()  # pusty set
print(zbior1)
zbior1.add("1")
print(zbior1)

zbior.add(18)
zbior.add(18)
zbior.add(62)
print(zbior)
print(zbior.pop())
print(zbior)
print(zbior.pop())

lista2 = list(zbior)  # zamiana na listę
print(lista2)
print(type(zbior))  # <class 'set'>
print(type(lista))  # <class 'list'>

# 13:35

zbior2 = {66, 11, 44, 18, 55, 62, 999}
print(zbior2)
print(zbior | zbior2)  # suma zbiorów
print(zbior & zbior2)  # część wspólna
print(zbior - zbior2)
print(zbior2.difference(zbior))
print(zbior.difference(zbior2))
