num = int(input())
size = input()
delivery = input()
delivery_price = 0

price = 0

if num <= 10:
    print("Invalid order")

if num > 10:
    if delivery == "With delivery":
        delivery_price = 60
    elif delivery == "Without delivery":
        delivery_price = 0

    if size == '90X130':
        price = 110
        if num > 60:
            price *= 0.92
        if 30 < num <= 60:
            price *= 0.95

    if size == '100X150':
        price = 140
        if num > 80:
            price *= 0.90
        if 40 < num <= 80:
            price *= 0.94

    if size == '130X180':
        price = 190
        if num > 50:
            price *= 0.88
        if 20 < num <=50:
            price *= 0.93

    if size == '200X300':
        price = 250
        if num > 50:
            price *= 0.86
        if 25 < num <= 50:
            price *= 0.91

    total = price * num + delivery_price

    if num > 99:
        total *= 0.96

    print(f"{total:.2f} BGN")
