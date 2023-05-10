import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    csvreader = csv.reader(csv_f)
    # ustawia wskaznik na kolejny element
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Suma wierszy", csvreader.line_num)

print(fields)
print(rows)
print(rows[0])
print(rows[0][0])
