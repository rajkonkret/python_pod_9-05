import csv

# pliki csv - dane oddzielone przecinkie, srednikiem itp
# Radek, Zenek, Tomek

fileds = ['name', 'branch', 'year', 'cgpa']
# ['radek', 'COE', '2', '9.1']
my_list_dict = [
    {'branch': 'COE', 'cgpa': '9.1', 'name': 'Radek', 'year': '2'}
]

filename = 'records.csv'

with open(filename, 'w', newline='') as csv_f:
    cswriter = csv.DictWriter(csv_f, fieldnames=fileds)
    cswriter.writeheader()
    cswriter.writerows(my_list_dict)
