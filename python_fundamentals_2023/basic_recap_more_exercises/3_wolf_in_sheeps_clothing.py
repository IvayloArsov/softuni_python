herd = input().split(", ")
counter_sheep = 0

if herd[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for animal in reversed(herd):
        if animal == 'sheep':
            counter_sheep += 1
        if animal == 'wolf':
            print(f"Oi! Sheep number {counter_sheep}! You are about to be eaten by a wolf!")