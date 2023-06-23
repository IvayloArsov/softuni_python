# preset inventory with the important reagents
inventory = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

junk = {}
flag = True
while flag:
    input_data = input().split(" ")
    # split the input data into a list with the corresponding reagents and quantities
    for i in range(0, len(input_data), 2):
        quantity = int(input_data[i])
        reagent = input_data[i + 1].casefold()

        if reagent in inventory:
            inventory[reagent] += quantity
            # checks if the critical quantity is reached for any of the reagents
            if inventory[reagent] >= 250:
                inventory[reagent] -= 250
                if reagent == "shards":
                    print("Shadowmourne obtained!")
                elif reagent == "fragments":
                    print("Valanyr obtained!")
                elif reagent == "motes":
                    print("Dragonwrath obtained!")
                flag = False
                break

        else:
            junk[reagent] = junk.get(reagent, 0) + quantity

# print statements for the two dictionaries according to the requirements
for item, quantity in inventory.items():
    print(f"{item}: {quantity}")
for item, quantity in junk.items():
    print(f"{item}: {quantity}")
