budget = float(input())
extras = int(input())
costume_unit = float(input())

decor_ = budget * 0.10

if extras > 150:
    costume_unit *= 0.90

expenses = extras * costume_unit + decor_

if budget >= expenses:
    print("Action!")
    print(f"Wingard starts filming with {budget - expenses:.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {expenses - budget:.2f} leva more.")
