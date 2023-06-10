floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    if floor == floors:
        label = 'L'
    elif floor % 2 == 0:
        label = 'O'
    else:
        label = 'A'
    for room in range(0, rooms):
        print(f"{label}{floor}{room}", end=" ")
    print()
