min_walk = int(input())
num_walks = int(input())
kcal_intake = int(input())

burned_kcal = 5*min_walk*num_walks

if burned_kcal >= kcal_intake/2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_kcal}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_kcal}.")