lista_bledow = []
alert_system = 'email'
error = 'medium'
error_message = "Stało sie coś strasznego"

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error == 'critical':
        lista_bledow.append('critical')
    elif error == 'medium':
        lista_bledow.append('medium')
    else:
        lista_bledow.append('nieznany')

print(lista_bledow)

lang = input("Wpisz znany Ci język programowania")
lista = []

match lang:
    case "python":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case _:  # domyslna (else)
        print("Nie znam takiego języka")

print(lista)