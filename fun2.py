# return  - funkcja zwraca wynik
def dodaj(a, b):
    c = a + b
    return c  # odeslij


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5, 6))
print(dodaj(5, 6) + dodaj(7, 8))
print(oblicz_vat(1000, 23))
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))

zm = oblicz_vat(1000)
if zm == 1230.0:
    print("Prawidlowo")
# 13:40