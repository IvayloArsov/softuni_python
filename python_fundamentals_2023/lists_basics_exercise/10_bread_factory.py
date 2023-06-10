events = input().split("|")

energy = 100
gained_energy = 0
coins = 100


for event in events:
    event = event.split("-")
    item = event[0]
    quantity = int(event[1])

    if item == "rest":
        if energy+quantity > 100:
            print(f'You gained {abs(100-energy)} energy.')
            energy = 100
        else:
            energy += quantity
            print(f"You gained {quantity} energy.")
        print(f'Current energy: {energy}.')

    elif item == 'order':
        if energy >= 30:
            energy -= 30
            coins += quantity
            print(f"You earned {quantity} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= quantity:
            coins -= quantity
            print(f'You bought {item}.')
        else:
            print(f'Closed! Cannot afford {item}.')
            break
else:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')