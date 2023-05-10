kurs_dol = 4.16
kurs_eur = 4.58


def kantor(waluta, kwota):
    print("Uruchomienie kantoru")

    def usd():
        print("Przeliczam dolary", kwota * kurs_dol)

    def eur():
        print("Przeliczam euro", kwota * kurs_eur)

    if waluta == 'eur':
        return eur
    else:
        return usd


def kantor2(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota):
        print("Przeliczam dolary", kwota * kurs_dol)

    def eur(kwota):
        print("Przeliczam euro", kwota * kurs_eur)

    if waluta == 'eur':
        return eur
    else:
        return usd


moj_kantor = kantor("eur", 1000)
print(moj_kantor)
moj_kantor()

mk2 = kantor2("usd")
mk2(1000)
