# # 14:43
#
# czy_znasz_Python = False
# if czy_znasz_Python:
#     print("Brawo")  # wciecie w tym miejscu obowiązkowe
#
# if czy_znasz_Python:
#     pass
#
# if czy_znasz_Python:
#     print("Brawo")
# else:  # w przeciwnym przypadku
#     print("Musisz się jeszce pouczyć")
#
# print("Jestem poza warunkiem")
#
# name = "Tomek"
# name = "Radek"
#
# if name == "Radek":  # == - porównanie
#     print(f"Twoje imie {name}")
#
# name = "Tomek"
# if name := "Radek":  # := rozbiło na name = 'Radek' i name == 'Radek'
#     print(f"Masz na imie {name}")
#
# podatek = 0.0
# # input() zwraca str
# zarobki = int(input("Podaj swój dochód"))
#
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.3
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.5
#
# print(f"Zapłacisz {zarobki * podatek} zł")
#
# suma_zam = 50
# if suma_zam > 100:
#     rabat = 25
# else:
#     rabat = 0
#
# print("suma zam:", suma_zam, "rabat:", rabat)
#
# rabat2 = 25 if suma_zam > 100 else 0
# print("suma zam:", suma_zam, "rabat:", rabat2)
# ctrl / - komentarz zaznaczonych linii
temp = -115
alert = False

if temp < 0:
    print("mróz")
    if temp < -100:
        print("Duzy mróz")
    elif temp < -10:
        if alert:
            print("Alert pogodowy")
elif temp == 0:
    print("przymrozek")
elif 10 < temp < 20:  # temp > 10 ale mniejsze od 20
    print("Dodatnia")
elif temp >= 20:
    print("upał")
