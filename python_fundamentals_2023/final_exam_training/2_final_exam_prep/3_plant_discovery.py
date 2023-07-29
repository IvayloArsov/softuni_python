def add_or_update_plant(plants, plant, rarity):
    plants[plant] = int(rarity)

def rate_plant(plant_ratings, plant, rating):
    plant_ratings[plant].append(int(rating))

def update_plant(plants, plant, new_rarity):
    plants[plant] = int(new_rarity)

def reset_entry(plant_ratings, plant):
    plant_ratings[plant] = []

n = int(input())
plants = {}
plant_ratings = {}

# Store plant information
for _ in range(n):
    plant_info = input().split("<->")
    plant_name, rarity = plant_info
    add_or_update_plant(plants, plant_name, rarity)
    plant_ratings[plant_name] = []

# Process commands
command = input()
while command != "Exhibition":
    command_type, *info = command.split(": ")
    if command_type == "Rate":
        plant, rating = info[0].split(" - ")
        if plant in plants:
            rate_plant(plant_ratings, plant, rating)
        else:
            print("error")
    elif command_type == "Update":
        plant, new_rarity = info[0].split(" - ")
        if plant in plants:
            update_plant(plants, plant, new_rarity)
        else:
            print("error")
    elif command_type == "Reset":
        plant, = info
        if plant in plants:
            reset_entry(plant_ratings, plant)
        else:
            print("error")
    else:
        print("error")

    command = input()

# Calculate average ratings and handle zero division
average_ratings = {plant: sum(plant_ratings[plant]) / len(plant_ratings[plant]) if plant_ratings[plant] else 0 for plant in plant_ratings}

print("Plants for the exhibition:")
for plant, rarity in plants.items():
    avg_rating = average_ratings[plant]
    print(f"- {plant}; Rarity: {rarity}; Rating: {avg_rating:.2f}")
