import requests
import xml.etree.ElementTree as ET

response = requests.get('http://api.nbp.pl/api/exchangerates/tables/A?format=xml')
print(response)

xml_data = response.content

root = ET.fromstring(xml_data)
print(xml_data)
table_name = root.find('.//Table').text
date = root.find('.//EffectiveDate').text
rates = root.findall('.//Rate')
print(date)
print(table_name)

for rate in rates:
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = rate.find('Mid').text
    print(f"{code}: {currency} - {mid}")
# IDR: rupia indonezyjska - 0.00028126
# INR: rupia indyjska - 0.050451
# KRW: won południowokoreański - 0.003113
# CNY: yuan renminbi (Chiny) - 0.5970
# XDR: SDR (MFW) - 5.5706