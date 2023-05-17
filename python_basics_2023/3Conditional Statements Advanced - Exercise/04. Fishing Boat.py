budget = int(input())
season = input()
qty = int(input())

boat = 0

if season == 'Spring':
    boat = 3000
    if qty <= 6:
        boat *= 0.90
    elif 7 <= qty <= 11:
        boat *= 0.85
    elif qty >= 12:
        boat *= 0.75
elif season == 'Summer':
    boat = 4200
    if qty <= 6:
        boat *= 0.90
    elif 7 <= qty <= 11:
        boat *= 0.85
    elif qty >= 12:
        boat *= 0.75
elif season == 'Autumn':
    boat = 4200
    if qty <= 6:
        boat *= 0.90
    elif 7 <= qty <= 11:
        boat *= 0.85
    elif qty >= 12:
        boat *= 0.75
elif season == 'Winter':
    boat = 2600
    if qty <= 6:
        boat *= 0.90
    elif 7 <= qty <= 11:
        boat *= 0.85
    elif qty >= 12:
        boat *= 0.75

if qty % 2 == 0 and not season == 'Autumn':
    boat *= 0.95

if budget >= boat:
    print(f"Yes! You have {abs(budget - boat):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget - boat):.2f} leva.")
