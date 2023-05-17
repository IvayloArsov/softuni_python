import math

people, entry_fee, pr_sunbed, pr_parasol = int(input()), float(input()), float(input()), float(input())

fee = people * entry_fee
sunbeds = math.ceil(people*0.75)*pr_sunbed
parasols = math.ceil(people/2)*pr_parasol

total = fee + sunbeds + parasols

print(f'{total:.2f} lv.')