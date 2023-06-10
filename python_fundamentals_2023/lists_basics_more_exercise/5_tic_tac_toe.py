line_1 = [int(num) for num in input().split(" ")]
line_2 = [int(num) for num in input().split(" ")]
line_3 = [int(num) for num in input().split(" ")]
matrix = [line_1, line_2, line_3]


def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            return row[0]

    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] != 0 for row in range(len(board))):
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    return None


winner = check_winner(matrix)
if winner == 1:
    print(f"First player won")
elif winner == 2:
    print('Second player won')
else:
    print("Draw!")
