rows = int(input())

matrix = []
alice = []
for row in range(rows):
    matrix.append(input().split())
    for col in range(rows):
        if matrix[row][col] == "A":
            matrix[row][col] = "*"
            alice = [row, col]

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

collected_tea = 0

while collected_tea < 10:
    command = input()
    move = possible_moves[command]
    row = alice[0] + move[0]
    col = alice[1] + move[1]
    if row < 0 or row >= rows or col < 0 or col >= rows:
        break
    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break
    if matrix[row][col] not in "*.":
        collected_tea += int(matrix[row][col])
    matrix[row][col] = "*"
    alice = [row, col]

if collected_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))


print_matrix(matrix)