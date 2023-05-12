import sqlite3

# baza danych coprzechowuje dane w pliku

conn = sqlite3.connect('dane.sqlite')
c = conn.cursor()

# c.execute('''
#
# CREATE TABLE transakcje
# (data TEXT, id INTEGER, cena REAL)
# ''')

c.execute('''
INSERT INTO transakcje VALUES('2023-05-12', 11, 17.50)
''')

lista = []

for row in c.execute("SELECT * FROM transakcje"):
    print(row)

conn.commit()
conn.close()
