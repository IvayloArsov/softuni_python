from collections import deque


rows, cols = map(int, input().split())
snake = deque(input())

matrix = []

for row in range(rows):
    matrix.append([''] * cols)
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = snake[0]
        else:
            matrix[row][-1 - col] = snake[0]
        snake.rotate(-1)


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


print_matrix(matrix)