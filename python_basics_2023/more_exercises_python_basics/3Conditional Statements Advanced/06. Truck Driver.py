select_season = input()
mileage = float(input())
fare = 0
if 20_000>= mileage > 10_000:
    fare = 1.45
elif mileage > 5000:
    if select_season == 'Spring' or select_season == 'Autumn':
        fare = 0.95
    elif select_season == 'Summer':
        fare = 1.10
    elif select_season == 'Winter':
        fare = 1.25
elif mileage <= 5000:
    if select_season == 'Spring' or select_season == 'Autumn':
        fare = 0.75
    elif select_season == 'Summer':
        fare = 0.90
    elif select_season == 'Winter':
        fare = 1.05

cash = (mileage * fare * 4)*0.90

print(f'{cash:.2f}')