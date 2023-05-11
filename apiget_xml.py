import requests
import xml.etree.ElementTree as ET

response = requests.get('http://api.nbp.pl/api/exchangerates/tables/A?format=xml')
print(response)

xml_data = response.content

root = ET.fromstring(xml_data)
print(xml_data)
table_name = root.find('.//ExchangeRatesTable')
date = root.find('.//EffectiveDate')
currrency = table_name.findall(".//Currency")

print(table_name)
print(currrency)
print(currrency[0])
print(date)