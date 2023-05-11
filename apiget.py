import requests as re

# pip install requests
url = 'http://api.nbp.pl/api/exchangerates/rates/A/eur/'

response = re.get(url)
print(response)\
# <Response [200]> - ok
# 400 - bad request, 404 - błędny adres
# 300 - różne
# 5xx  - błedy wewnętrzne serwera

table = response.json()
print(table)
print(table['table'])
# wyciagnąc 'mid'
print(table['rates'][0]['mid'])