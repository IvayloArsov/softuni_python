budget = float(input())
nights = int(input())
pr_night = float(input())
percentage = int(input())/100

expenses = budget * percentage

if nights > 7:
    pr_night *= 0.95

hotel = nights*pr_night
total = hotel + expenses

if budget >= total:
    print(f"Ivanovi will be left with {budget-total:.2f} leva after vacation.")
else:
    print(f"{total-budget:.2f} leva needed.")