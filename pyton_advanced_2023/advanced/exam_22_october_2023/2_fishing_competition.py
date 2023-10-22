def next_move(command, current_row, current_col):
    global rows, cols

    if command == 'up':
        new_row = (current_row - 1) % rows
        return new_row, current_col
    elif command == 'down':
        new_row = (current_row + 1) % rows
        return new_row, current_col
    elif command == 'left':
        new_col = (current_col - 1) % cols
        return current_row, new_col
    elif command == 'right':
        new_col = (current_col + 1) % cols
        return current_row, new_col

    return None, None


rows = int(input())
cols = rows
matrix = []
start_row, start_col = None, None
pointer_row, pointer_col = None, None
fish_caught = 0
fish_target = 20

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
    if line == 'collect the nets':
        break
    if matrix[next_row][next_col] == 'W':
        print(
            f'You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{",".join(map(str, (next_row, next_col)))}]')
        exit()
    elif matrix[next_row][next_col].isdigit():
        fish = int(matrix[next_row][next_col])
        fish_caught += fish
        matrix[next_row][next_col] = '-'

    pointer_row, pointer_col = next_row, next_col
    matrix[pointer_row][pointer_col] = '-'
    matrix[start_row][start_col] = '-'

matrix[pointer_row][pointer_col] = 'S'
if fish_caught >= fish_target:
    print('Success! You managed to reach the quota!')
else:
    print(
        f"You didn't catch enough fish and didn't reach the quota! You need {fish_target - fish_caught} tons of fish more.")
if fish_caught:
    print(f'Amount of fish caught: {fish_caught} tons.')
for row in matrix:
    print(''.join(row))
