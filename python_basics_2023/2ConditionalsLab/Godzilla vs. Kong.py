budget = float(input())
ppl = int(input())
costume_price = float(input())
decors = budget*0.10
costumes = ppl*costume_price

if ppl > 150:
    costumes = costumes*0.9

expenses = costumes+decors

if expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {expenses-budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget-expenses:.2f} leva left.")