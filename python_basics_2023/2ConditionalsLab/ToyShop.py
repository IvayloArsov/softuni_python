holiday = float(input())
puzzles = int(input())
talking_toys = int(input())
teddy_bears = int(input())
minions = int(input())
toy_trucks = int(input())

puzzle = 2.6*puzzles
talking_toy = 3*talking_toys
teddy_bear = 4.1*teddy_bears
minion = 8.20*minions
toy_truck = 2*toy_trucks
sold = puzzles+talking_toys+teddy_bears+minions+toy_trucks
money = puzzle+talking_toy+teddy_bear+minion+toy_truck

if sold >= 50:
    money = money * 0.75

money = money * 0.90

if money >= holiday:
    leftovers = money - holiday
    print(f"Yes! {leftovers:.2f} lv left.")
else:
    needed = holiday-money
    print(f"Not enough money! {needed:.2f} lv needed.")
