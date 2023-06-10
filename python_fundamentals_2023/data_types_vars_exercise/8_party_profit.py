import math

companions_count = int(input())
days = int(input())
coins = 0

for day in range(1, days+1):
    party = False
    if day % 10 == 0:
        companions_count -= 2
    if day % 15 == 0:
        companions_count += 5
    coins += 50-(companions_count*2)

    if day % 3 == 0:
        coins -= 3*companions_count
        party = True
    if day % 5 == 0:
        coins += 20*companions_count
        if party:
            coins -= companions_count*2

print(f"{companions_count} companions received {math.floor(coins/companions_count)} coins each.")
