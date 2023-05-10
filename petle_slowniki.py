dictionary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}

print(dictionary)

# zwraca klucze
for k in dictionary:
    print(k)

# zwraca klucze
for k in dictionary.keys():
    print(k)

# zwraca wartości
for v in dictionary.values():
    print(v)

# zwraca klucz k i wartosc v
for k, v in dictionary.items():
    print(k, '=>', v)

dict_1 = {'name': 'radek'}
for k in dict_1:
    print(k)
# { key: value } -> {value:key}
# zamiana klucza z wartoscią w słowniku
print({value: key for key, value in dict_1.items()})
# a,b = b,a
# key, value = value, key
dict_2 = {}
for key, value in dict_1.items():
    dict_2[value] = key

print(dict_2)
