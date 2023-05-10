# funkcję, która będzie obliczać średnią
def liczby(c, *cyfry):
    print(c)
    print(cyfry)
    print(type(cyfry))  # <class 'tuple'>
    suma = 0
    for cy in cyfry:
        suma += cy
    count = len(cyfry)
    print(suma)
    if count != 0:
        print(f"Średnia {suma / count}")


liczby(1)
# liczby(1, (2, 3, 4, 5))  # 1 - cyfra, () - krotka
liczby(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 67, 89, 0)
