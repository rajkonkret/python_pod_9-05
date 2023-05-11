# json - {'name' : 'Radek'}
import json

person_dict = {'name': 'Radek', 'age': 39, 'czy_pali': None}
print(person_dict)

with open('dane_nasze.json' , 'w') as f:
    json.dump(person_dict, f)

with open('dane_nasze.json', 'r') as f:
    data = json.load(f)

print(data)
print(data['name'])
print(data.keys())
print(data.values())
print(data.items())
