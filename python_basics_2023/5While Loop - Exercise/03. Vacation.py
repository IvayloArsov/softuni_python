goal = float(input())
savings = float(input())
cons_spending = 0
day_passed = 0

while savings < goal:
    action = input()
    amount = float(input())
    day_passed += 1
    if action == 'save':
        savings += amount
        cons_spending = 0
    elif action == 'spend':
        if savings < 0:
            savings = 0
        else:
            savings -= amount
        cons_spending += 1
        if cons_spending == 5:
            break

if goal <= savings:
    print(f"You saved the money for {day_passed} days.")
else:
    print(f"You can't save the money. \n {day_passed}")
