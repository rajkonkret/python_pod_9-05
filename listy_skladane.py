# listy składane - list comphrehesion

# Tworzenie  nowej listy
numbers = [1, 2, 3, 4, 5]
squred = [num ** 2 for num in numbers]
print(squred)

# filtrowanie pierwsze num to tak naprawde operacja append(num)
# wykonywany tylko jesli warunek jest spełniony
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
# to samo klasycznie
# for num in numbers:
#     if num % 2 == 0:
#         jaksalista.append(num)

# modyfikacja listy uzależniona od warunku
modifed_numbers = [num * 2 if num % 2 == 0 else num for num in numbers]
print(modifed_numbers)
temp_list = []

for num in numbers:
    if num % 2 == 0:
        temp_list.append(num * 2)
    else:
        temp_list.append(num)
print(temp_list)

word = "Python"
letters = [letter for letter in word]
print(letters)
lett2 = []
for letter in word:
    lett2.append(letter)
print(lett2)

# generowanie liczb parzystych z zakresu 0..9
even_numbers2 = [num for num in range(10) if num % 2 == 0]
print(even_numbers2)
# 14:20
