import json

with open('dane_json.json', 'r') as f:
    data = json.load(f)

print(data)
# members
print(data['members'])
print(data['members'][0])
# powers
print(data['members'][0]['powers'])
print(data['members'][0]['powers'][1])