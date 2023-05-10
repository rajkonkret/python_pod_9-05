from datetime import date, timedelta, datetime

today = date.today()
time = datetime.now()

print(today)
print(time)
print(today.year)
print(time.hour)

tommorow = today + timedelta(days=1)

print(tommorow)

products = [
    {'sku': '1', 'exp_date': today, 'price': 100.0},
    {'sku': '2', 'exp_date': tommorow, 'price': 50.0},
    {'sku': '3', 'exp_date': today, 'price': 20},
    {'sku': '4', 'exp_date': today, 'price': 30.0},
    {'sku': '5', 'exp_date': tommorow, 'price': 40},
]

for product in products:
    if product['exp_date'] != today:
        continue  # wraca na początek petli bez wykonywania kolejnych instrukcji
    print(product)
    product['price'] *= 0.8  # p = p * 0.8

    print(f"""
    Price for sku={product['sku']}
    is now {product['price']}""")

