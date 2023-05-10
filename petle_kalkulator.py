while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Podaj działania")
    if odp == '5':
        break
    a = int(input("Podaj pierwsza liczbe"))
    b = int(input("Podaj drugą liczbe"))
    if odp == '1':
        print(a + b)
    elif odp == '2':
        print(a - b)
    elif odp == '3':
        print(a * b)
    elif odp == '4':
        if b != 0:
            print(a / b)
        else:
            print("Nie dzielimy przez zero")
    else:
        print("Nie znam takiego działania")
