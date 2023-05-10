# while - petla sterowana warunkiem
import time
licznik = 0
while True:
    licznik += 1
    print("Komunikat...")
    if licznik > 10:
        break  # przerwaanie aktualnej pętli

print(licznik)
licznik = 0
while licznik < 10:
    print("Komunikat...")
    # time.sleep(1)
    licznik += 1

lista = []
while True:
    wej = input("Podaj liczbe")
    if not wej.isnumeric():
        break
    lista.append(wej)

print(lista)
# 11:00
