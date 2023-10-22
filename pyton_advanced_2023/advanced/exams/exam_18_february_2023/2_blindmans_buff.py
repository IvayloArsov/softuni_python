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


rows, cols = [int(f) for f in input().split()]
matrix = []
start_row, start_col = None, None
pointer_row, pointer_col = None, None
targets = 0
moves = 0

for r in range(rows):
    row = input().split()
    matrix.append(row)
    if 'B' in row:
        pointer_row = r
        pointer_col = row.index('B')
        start_row = pointer_row
        start_col = pointer_col

while True:
    line = input()
    next_row, next_col = next_move(line, pointer_row, pointer_col)

    if line == 'Finish':
        break
    if next_row is None or next_col is None:
        continue
    elif matrix[next_row][next_col] == 'O':
        continue
    elif matrix[next_row][next_col] == 'P':
        moves += 1
        targets += 1
        matrix[next_row][next_col] = '-'
        if targets == 3:
            break
    elif matrix[next_row][next_col] == '-':
        moves += 1

    pointer_row, pointer_col = next_row, next_col
    matrix[pointer_row][pointer_col] = '-'
    matrix[start_row][start_col] = '-'

print('Game over!')
print(f'Touched opponents: {targets} Moves made: {moves}')

# for row in matrix:
#     print(' '.join(row))
