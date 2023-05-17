days = int(input())
food_available = float(input())
biscuits = 0
dog_eaten = 0
cat_eaten = 0

for day in range(1, days+1):

    dog_food_input = int(input())
    cat_food_input = int(input())

    if day % 3 == 0:
        biscuits += (dog_food_input+cat_food_input) * 0.10
    dog_eaten += dog_food_input
    cat_eaten += cat_food_input

total_eaten = dog_eaten + cat_eaten

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f'{(total_eaten / food_available) * 100:.2f}% of the food has been eaten.')
print(f'{(dog_eaten / total_eaten) * 100:.2f}% eaten from the dog.')
print(f'{(cat_eaten / total_eaten) * 100:.2f}% eaten from the cat.')
