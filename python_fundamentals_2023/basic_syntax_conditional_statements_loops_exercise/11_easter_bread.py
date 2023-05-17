budget = float(input())
flour_price = float(input())

egg_pack = flour_price * 0.75
milk_lt_price = flour_price * 1.25
number_of_loaves = 0
counter = 0
colored_eggs = 0
ingredients = flour_price+milk_lt_price/4+egg_pack
while budget > ingredients:
    budget -= ingredients
    number_of_loaves += 1
    counter += 1
    colored_eggs += 3
    if counter % 3 == 0:
        colored_eggs -= counter-2
money_left = budget
print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")