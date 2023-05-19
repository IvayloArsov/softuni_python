items = input().split("|")
budget = int(input())

inventory = []
profit = 0
sales = 0

for item in items:
    item = item.split("->")
    buy = False
    if item[0] == "Clothes":
        if float(item[1]) <= 50.00:
            buy = True

    elif item[0] == "Shoes":
        if float(item[1]) <= 35.00:
            buy = True

    elif item[0] == "Accessories":
        if float(item[1]) <= 20.50:
            buy = True

    if buy:
        inventory.append(float(item[1]) * 1.40)

        if float(item[1]) > budget:
            inventory.pop()
            continue

        else:
            budget -= float(item[1])
            profit += float(item[1])*0.40
            sales += float(item[1])*1.40

sales += budget

for inv in inventory:
    print(f'{inv:.2f}', end=' ')

print(f"\nProfit: {profit:.2f}")
if sales >= 150:
    print('Hello, France!')
else:
    print("Not enough money.")