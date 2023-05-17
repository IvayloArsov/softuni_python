import math
vineyards = int(input())
grape_yield = float(input())
quota = int(input())
workers = int(input())

harvest_per_vine = (vineyards * grape_yield * 0.40)
wine = harvest_per_vine / 2.5
left = abs(quota-wine)
if wine < quota:
    print(f"It will be a tough winter! More {math.floor(left)} liters wine needed.")

else:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(left)} liters left -> {math.ceil(left / workers)} liters per person.")