products = {}

while True:
    data = input()
    if data == "buy":
        break

    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if name in products:
        products[name]['quantity'] += quantity
        if price != products[name]['price']:
            products[name]['price'] = price
    else:
        products[name] = {'price': price, 'quantity': quantity}

for name, data in products.items():
    total_price = data['price'] * data['quantity']
    print(f"{name} -> {total_price:.2f}")