matrix = []
position = []
targets = 0
for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == "A":
            position = [row, col]
        elif matrix[row][col] == "x":
            targets += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}
n = int(input())
targets_down = []
for _ in range(n):
    command = input().split()

    if command[0] == "shoot":
        r = position[0]+directions[command[1]][0]
        c = position[1]+directions[command[1]][1]

        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == 'x':
                matrix[r][c] = "."
                targets -= 1
                targets_down.append([r, c])
                break
            r += directions[command[1]][0]
            c += directions[command[1]][1]
        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break
    if command[0] == "move":
        steps = int(command[2])
        direction = command[1]
        if direction == "up":
            r = position[0]-steps
            c = position[1]
        elif direction == "down":
            r = position[0] + steps
            c = position[1]
        elif direction == "right":
            r = position[0]
            c = position[1] + steps
        elif direction == "left":
            r = position[0]
            c = position[1] - steps

        if 0 <= r < 5 and 0 <= c < 5 and matrix[r][c] == ".":
            matrix[r][c] = "A"
            matrix[position[0]][position[1]] = "."
            position = [r, c]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

[print(row) for row in targets_down]
