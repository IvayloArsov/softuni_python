def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command, current_row, current_col):
    if command == 'up' and is_valid(current_row-1, rows):
        return current_row-1, current_col
    if command == 'down' and is_valid(current_row+1, rows):
        return current_row+1, current_col
    if command == 'left' and is_valid(current_col-1, cols):
        return current_row, current_col-1
    if command == 'right' and is_valid(current_col+1, cols):
        return current_row, current_col+1
    return None, None


rows, cols = [int(x) for x in input().split(' ')]
field = []
start_row, start_col = None, None
boy_row, boy_col = None, None
line = ' '

for r in range(rows):
    row = list(input())
    field.append(row)
    if 'B' in row:
        boy_row = r
        boy_col = row.index('B')
        start_row = boy_row
        start_col = boy_col

while line:
    line = input()
    next_row, next_col = next_move(line, boy_row, boy_col)
    if next_row is None or next_col is None:
        print('The delivery is late. Order is canceled.')
        field[start_row][start_col] = ' '
        break
    if field[next_row][next_col] == '*':
        continue
    if field[next_row][next_col] == 'A':
        field[boy_row][boy_col] = '.'
        boy_row, boy_col = next_row, next_col
        field[boy_row][boy_col] = 'P'
        print("Pizza is delivered on time! Next order...")
        field[start_row][start_col] = 'B'
        break
    if field[next_row][next_col] == 'P':
        field[boy_row][boy_col] = '.'
        boy_row, boy_col = next_row, next_col
        field[next_row][next_col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")
        continue
    if not field[boy_row][boy_col] == 'R':
        field[boy_row][boy_col] = '.'
    boy_row, boy_col = next_row, next_col
    field[boy_row][boy_col] = '.'

for row in field:
    print(''.join(row))