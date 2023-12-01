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


rows, cols = [int(f) for f in input().split(",")]
matrix = []
start_row, start_col = None, None
mouse_row, mouse_col = None, None
cheeses = 0

for r in range(rows):
    row = list(input())
    matrix.append(row)
    if 'M' in row:
        mouse_row = r
        mouse_col = row.index('M')
        start_row = mouse_row
        start_col = mouse_col
    for c in range(cols):
        if matrix[r][c] == "C":
            cheeses += 1

while True:
    line = input()
    next_row, next_col = next_move(line, mouse_row, mouse_col)
    if line == 'danger':
        print("Mouse will come back later!")
        break
    if next_row is None or next_col is None:
        print("No more cheese for tonight!")
        matrix[mouse_row][mouse_col] = 'M'
        break
    if matrix[next_row][next_col] == '@':
        continue
    if matrix[next_row][next_col] == "T":
        print("Mouse is trapped!")
        matrix[next_row][next_col] = 'M'
        break
    if matrix[next_row][next_col] == 'C':
        cheeses -= 1
        if not cheeses:
            print("Happy mouse! All the cheese is eaten, good night!")
            matrix[next_row][next_col] = 'M'

            break
    mouse_row, mouse_col = next_row, next_col
    matrix[mouse_row][mouse_col] = '*'
    matrix[start_row][start_col] = '*'

for row in matrix:
    print(''.join(row))