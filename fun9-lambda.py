# lambda - skrocona wersja funkcji

odejmij = lambda a, b: a - b

print(odejmij(5, 4))

# # to jest dokładnie to samo co w naszej lambdzie
# def odejmij(a, b):
#     return a - b

oblicz_vat = lambda cena, vat=7: cena * (100 + vat) / 100
print(oblicz_vat(1000, 23))
print(oblicz_vat(1000))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")

print(wiek(5))
print(wiek(10))
print(wiek(21))

lista = [1, 2, 7, 8, 10, 56]
# mapowanie danych z kolekcji wg zadanej lambdy
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
# filter - filtrowanie danych wg wzorca zadanego fukncją lambda
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: x > 8, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 20, lista))}")
