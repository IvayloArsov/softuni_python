# constructed an empty dictionary to store the input values
ore_dict = dict()
# while loop to continuously receive input values for both ore and quantity
# input values
while True:
    ore = input()
    # bool - if input received is "stop" - break the loop
    if ore == "stop":
        break
    quantity = int(input())
    # adds the ore to the dictionary if it isn't already there
    ore_dict[ore] = ore_dict.get(ore, 0)
    # adds the quantity to the corresponding ore in the dictionary
    ore_dict[ore] += quantity

# for loop that iterates over the dictionary and prints each key,value pair
# in the expected format
for ore, count in ore_dict.items():
    print(f"{ore} -> {count}")
