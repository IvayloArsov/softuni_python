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
lines = list(map(str, input().split(', ')))
matrix = []
start_row, start_col = None, None
mouse_row, mouse_col = None, None
hazelnuts = 0
flag = True
for r in range(rows):
    row = list(input())
    matrix.append(row)
    if 's' in row:
        mouse_row = r
        mouse_col = row.index('s')
        start_row = mouse_row
        start_col = mouse_col

for line in lines:
    next_row, next_col = next_move(line, mouse_row, mouse_col)

    if next_row is None or next_col is None:
        print("The squirrel is out of the field.")
        matrix[mouse_row][mouse_col] = '*'
        flag = False
        break
    if matrix[next_row][next_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        matrix[next_row][next_col] = '*'
        flag = False
        break
    if matrix[next_row][next_col] == 'h':
        hazelnuts += 1
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            matrix[next_row][next_col] = '*'
            flag = False
            break
    mouse_row, mouse_col = next_row, next_col
    matrix[mouse_row][mouse_col] = '*'
    matrix[start_row][start_col] = '*'

if flag:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")