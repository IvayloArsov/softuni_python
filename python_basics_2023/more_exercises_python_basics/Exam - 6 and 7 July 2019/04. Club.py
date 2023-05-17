target = float(input())
sales = 0

while True:
    cocktail = input()
    if cocktail == 'Party!':
        break

    number = input()
    price = int(number) * len(cocktail)

    if int(str(price)[-1]) % 2 !=0:
        price *= 0.75
    sales += price

    if sales >= target:
        break

if sales >= target:
    print("Target acquired.")
else:
    print(f'We need {target-sales:.2f} leva more.')

print(f"Club income - {sales:.2f} leva.")