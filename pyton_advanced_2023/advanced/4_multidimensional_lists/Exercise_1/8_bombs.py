
rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
bombs_coordinates = [int(x) for x in input().replace(" ", ",").split(",")]
cols = len(matrix[0])
bomb_row = bombs_coordinates[::2]
bomb_col = bombs_coordinates[1::2]
alive_cells = []


def check_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True


def explode(row, col, bomb_damage):
    if matrix[row][col] > 0:
        matrix[row][col] -= bomb_damage


movement_explosion = [0, -1, 0, 1, -1, 0, 1, 0, -1, -1, -1, 1, 1, -1, 1, 1]
row_movement = movement_explosion[::2]
col_movement = movement_explosion[1::2]
for i in range(len(bomb_row)):
    row, col = bomb_row[i], bomb_col[i]
    if matrix[row][col] > 0:
        bomb_damage, matrix[row][col] = matrix[row][col], 0
        for ind in range(len(row_movement)):
            if check_valid_index(row + row_movement[ind], col + col_movement[ind]):
                explode(row + row_movement[ind], col + col_movement[ind], bomb_damage)

for row in range(len(matrix)):
    for num in matrix[row]:
        if num > 0:
            alive_cells.append(num)

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for row in range(len(matrix)):
    print(*matrix[row], sep=" ")