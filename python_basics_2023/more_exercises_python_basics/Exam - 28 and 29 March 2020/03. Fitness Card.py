budget = float(input())
sex = input()
age = int(input())
sport_input = input()

price = 0
if sex == 'm':
    if sport_input == 'Gym':
        price = 42

    if sport_input == 'Boxing':
        price = 41

    if sport_input == 'Yoga':
        price = 45

    if sport_input == 'Zumba':
        price = 34

    if sport_input == 'Dances':
        price = 51

    if sport_input == 'Pilates':
        price = 39
if sex == 'f':
    if sport_input == 'Gym':
        price = 35

    if sport_input == 'Boxing':
        price = 37

    if sport_input == 'Yoga':
        price = 42

    if sport_input == 'Zumba':
        price = 31

    if sport_input == 'Dances':
        price = 53

    if sport_input == 'Pilates':
        price = 37

if age <= 19:
    price *= 0.80

if budget >= price:
    print(f"You purchased a 1 month pass for {sport_input}.")
else:
    print(f"You don't have enough money! You need ${price-budget:.2f} more.")