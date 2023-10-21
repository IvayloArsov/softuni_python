n = int(input())

matrix = []
bunny = []
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "B":
            bunny = [row, col]

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

max_eggs = float("-inf")
max_direction = ''
max_eggs_matrix = []

for direction, move in possible_moves.items():
    eggs = 0
    curr_eggs_matrix = []
    row = bunny[0]+move[0]
    col = bunny[1]+move[1]

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "X":
            break
        eggs += int(matrix[row][col])
        curr_eggs_matrix.append([row, col])
        row += move[0]
        col += move[1]
    if eggs > max_eggs and curr_eggs_matrix:
        max_eggs = eggs
        max_direction = direction
        max_eggs_matrix = curr_eggs_matrix

print(max_direction)
[print(row) for row in max_eggs_matrix]
print(max_eggs)