def mnozenie(a, b):
    try:
        print(int(a) * int(b))
    except Exception as e:
        print("Wystąpił bład", e)
    else:
        wynik = [a, b]
        print(wynik)
    finally:
        print("Zawsze")


mnozenie(1, 2)
mnozenie((1,), 2)

# 9:50