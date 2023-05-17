import math

gold = 0
money = float(input())
change_to_coins = money * 100

while change_to_coins > 0:
    if change_to_coins >= 200:
        change_to_coins -= 200
        gold += 1
    elif 200 > change_to_coins >= 100:
        change_to_coins -= 100
        gold += 1
    elif 100 > change_to_coins >= 50:
        change_to_coins -= 50
        gold += 1
    elif 50 > change_to_coins >= 20:
        change_to_coins -= 20
        gold += 1
    elif 20 > change_to_coins >= 10:
        change_to_coins -= 10
        gold += 1
    elif 10 > change_to_coins >= 5:
        change_to_coins -= 5
        gold += 1
    elif 5 > change_to_coins >= 2:
        change_to_coins -= 2
        gold += 1
    elif 2 > change_to_coins >= 1:
        change_to_coins -= 1
        gold += 1
    change_to_coins = math.floor(change_to_coins)

print(gold)