budget = float(input())
season = input()

price = 0
housing = ''
location = ''

if budget > 3000:
    housing = 'Hotel'
    price = budget*0.90
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'
elif budget > 1000:
    housing = 'Hut'
    if season == 'Summer':
        price = budget*0.80
        location = 'Alaska'
    elif season == 'Winter':
        price = budget*0.60
        location = 'Morocco'
elif budget <= 1000:
    housing = 'Camp'
    if season == 'Summer':
        price = budget*0.65
        location = 'Alaska'
    elif season == 'Winter':
        price = budget*0.45
        location = 'Morocco'
print(f'{location} - {housing} - {price:.2f}')
