import pandas as pd

excel_data = pd.read_excel('sales.xlsx')

# data = pd.DataFrame(excel_data)
# wyswietla tylko wskazaną kolumne
data = pd.DataFrame(excel_data, columns=['Sales Date'])

print("The content is:\n", data)