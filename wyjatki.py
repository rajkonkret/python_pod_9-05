def mnozenie(a, b):
    try:
        return int(a) * int(b)
    except TypeError:
        return "Błąd typu"
    except ValueError:
        return "Bład wartości"


def mnozenie2(a, b):
    try:
        return int(a) * int(b)
    except (ValueError, TypeError) as e:
        return e


# ZeroDivisionError: division by zero
def dzielenie(a, b):
    try:
        return int(a) / int(b)
    except TypeError:
        return "Błąd typu"
    except ValueError:
        return "Bład wartości"
    except ZeroDivisionError:
        return "Dzielenie przez zero"


def dodawanie(a, b):
    try:
        return a + b
    except Exception as e:
        return e


print(mnozenie(5, 6))
print(mnozenie("5", "6"))
print(mnozenie("A", "6"))
print("Nadal program działa")
print(mnozenie((9,), "6"))
print("Nadal program działa")

print(mnozenie2((9,), "6"))
print("Nadal program działa")

print(dzielenie(2, 0))
print("Nadal program działa")

print(dodawanie((1,), 2))
print("Nadal program działa")

