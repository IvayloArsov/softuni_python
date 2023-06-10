food_bought = int(input()) * 1000
_food_eaten = 0

while True:
    eaten = input()
    if eaten == 'Adopted':
        break
    _food_eaten += int(eaten)

if _food_eaten > food_bought:
    print(f"Food is not enough. You need {abs(_food_eaten - food_bought)} grams more.")
else:
    print(f'Food is enough! Leftovers: {abs(_food_eaten-food_bought)} grams.')
