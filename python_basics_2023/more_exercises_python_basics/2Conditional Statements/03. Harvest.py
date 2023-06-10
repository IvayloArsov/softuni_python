import math

vineyard = int(input())
wine_yield = float(input())
quota = int(input())
workers = int(input())

liters_wine = ((vineyard*wine_yield)*0.40)/2.5

if liters_wine >= quota:
    print(f'Good harvest this year! Total wine: {math.floor(liters_wine)} liters.')
    print(f'{math.ceil(liters_wine-quota)} liters left -> {math.ceil((liters_wine-quota)/workers)} liters per person.')
else:
    print(f'It will be a tough winter! More {math.floor(quota-liters_wine)} liters wine needed.')