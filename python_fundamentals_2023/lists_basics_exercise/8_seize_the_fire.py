fires = input().split("#")
water = int(input())

cells = []
total_fire = 0
effort = 0

for fire in fires:
    fire = fire.split(' = ')
    is_valid = False
    if fire[0] == 'High':
        if 81 <= int(fire[1]) <= 125:
            cells.append(int(fire[1]))
            is_valid = True
    elif fire[0] == 'Medium':
        if 51 <= int(fire[1]) <= 80:
            cells.append(int(fire[1]))
            is_valid = True
    elif fire[0] == 'Low':
        if 1 <= int(fire[1]) <= 50:
            cells.append(int(fire[1]))
            is_valid = True
    if is_valid:
        if int(fire[1]) > water:
            cells.pop()
            continue
        else:
            water -= int(fire[1])
            total_fire += int(fire[1])
            effort += int(fire[1])*0.25
print("Cells:")
for cell in cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")


