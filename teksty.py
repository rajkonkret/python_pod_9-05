from datetime import date, timedelta, datetime

tekst = "Witaj świecie"
tekst2 = tekst.upper()
imie = "Radek"
print(tekst)
print(tekst.lower())
print(tekst2)

print(tekst.removeprefix("Witaj "))
print(tekst.removesuffix("świecie"))
encoded_s = tekst.encode('utf-8')
print(encoded_s)
print(type(encoded_s))
print(encoded_s.decode('utf-8'))
tekst_bajtowy = b"Tutaj jest tekst bajtowy"
print(tekst_bajtowy)
print(type(tekst_bajtowy))  # <class 'bytes'>

print(tekst.count("i"))
print(tekst.count("i", 0, 4))

# b - backspace
tekst_format = f"Mam\t na imię {imie} \ni lubię \bPythona"
print(tekst_format)

star = "Witaj %s"
print(star % imie)
print("Witaj śiecie. Mam na imie {}".format(imie))

a = 14
b = 3

print(f"Wynik porównania {a} > {b}", a > b)
print(f"Wynik porównania {a} < {b}", a < b)
print(f"Wynik porównania {a} == {b}", a == b)
print(f"Wynik porównania {a} != {b}", a != b)

print("Data: ", date.today())

print("""
Tekst 
wielolinijkowy""")
