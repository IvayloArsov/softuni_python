drink = input()
sugar = input()
units = int(input())
price = 0

if drink == 'Espresso':
    if sugar == 'Without':
        price = 0.90
        price *= 0.65
    if sugar == 'Normal':
        price = 1
    if sugar == 'Extra':
        price = 1.20

if drink == 'Cappuccino':
    if sugar == 'Without':
        price = 1
        price *= 0.65
    if sugar == 'Normal':
        price = 1.20
    if sugar == 'Extra':
        price = 1.60

if drink == 'Tea':
    if sugar == 'Without':
        price = 0.50
        price *= 0.65
    if sugar == 'Normal':
        price = 0.60
    if sugar == 'Extra':
        price = 0.70

total = units*price

if drink == 'Espresso' and units >= 5:
    total *= 0.75

if total > 15:
    total *= 0.80

print(f"You bought {units} cups of {drink} for {total:.2f} lv.")