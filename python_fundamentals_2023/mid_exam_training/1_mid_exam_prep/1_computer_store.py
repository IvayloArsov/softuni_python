price_no_tax = 0
flag = False
while True:
    command = input()
    if command == "regular":
        break
    elif command == "special":
        flag = True
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        price_no_tax += price

price_tax = price_no_tax*1.2
if flag:
    price_tax *= 0.90

if price_no_tax <= 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_no_tax:.2f}$")
    print(f"Taxes: {price_no_tax*0.2:.2f}$")
    print("-"*11)
    print(f"Total price: {price_tax:.2f}$")