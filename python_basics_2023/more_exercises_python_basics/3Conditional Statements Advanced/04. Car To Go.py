budget = float(input())
season = input()

price = 0

if budget > 500:
    price = budget*0.90
    print(f'Luxury class')
    print(f'Jeep - {price:.2f}')
elif budget > 100:
    if season == 'Summer':
        price = budget*0.45
        print('Compact class')
        print(f'Cabrio - {price:.2f}')
    elif season == 'Winter':
        price = budget * 0.80
        print('Compact class')
        print(f'Jeep - {price:.2f}')
elif budget <= 100:
    if season == 'Summer':
        price = budget*0.35
        print('Economy class')
        print(f'Cabrio - {price:.2f}')
    elif season == 'Winter':
        price = budget * 0.65
        print('Economy class')
        print(f'Jeep - {price:.2f}')