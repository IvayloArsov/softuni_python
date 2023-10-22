def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command, current_row, current_col):
    if command == 'up' and is_valid(current_row - 1, rows):
        return current_row - 1, current_col
    if command == 'down' and is_valid(current_row + 1, rows):
        return current_row + 1, current_col
    if command == 'left' and is_valid(current_col - 1, cols):
        return current_row, current_col - 1
    if command == 'right' and is_valid(current_col + 1, cols):
        return current_row, current_col + 1
    return None, None


rows = int(input())
cols = rows
matrix = []
start_row, start_col = None, None
pointer_row, pointer_col = None, None
targets = 3
health_points = 3

for r in range(rows):
    row = list(input())
    matrix.append(row)
    if 'S' in row:
        pointer_row = r
        pointer_col = row.index('S')
        start_row = pointer_row
        start_col = pointer_col

while True:
    line = input()
    next_row, next_col = next_move(line, pointer_row, pointer_col)

    if not targets:
        print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
        break
    elif not health_points:
        print(f'Mission failed, U-9 disappeared! Last known coordinates {[pointer_row, pointer_col]}!')
        break
    # if next_row is None or next_col is None:
    #     continue
    elif matrix[next_row][next_col] == '*':
        health_points -= 1
        matrix[next_row][next_col] = '-'
    elif matrix[next_row][next_col] == 'C':
        targets -= 1
        matrix[next_row][next_col] = '-'

    pointer_row, pointer_col = next_row, next_col
    matrix[pointer_row][pointer_col] = '-'
    matrix[start_row][start_col] = '-'

matrix[pointer_row][pointer_col] = 'S'
for row in matrix:
    print(''.join(row))
