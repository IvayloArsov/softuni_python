import math
from math import trunc
holidays = int(input())
playtime = 30_000
work_days = 365 - holidays
total = (holidays * 127) + (work_days * 63)
time_spent = abs(playtime - total)

if total > playtime:
    print("Tom will run away")
    print(f"{math.trunc(time_spent//60)} hours and {abs(time_spent)%60} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{math.trunc(time_spent//60)} hours and {abs(time_spent)%60} minutes less for play")
