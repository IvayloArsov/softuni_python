energy = int(input())
wins = 0
counter = 0
while True:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {wins}. Energy left: {energy}")
        break
    if energy >= int(command):
        energy -= int(command)
        wins += 1
        counter += 1
        if counter % 3 == 0:
            energy += wins

    elif energy <= int(command):
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break