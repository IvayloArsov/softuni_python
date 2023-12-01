rows = int(input())

matrix = [
    [int(x) for x in input().split()]
    for _ in range(rows)
]

while True:
    command = input()
    if command == "END":
        break
    data, *info = command.split()
    row1, col1, value = map(int, info)
    if 0 <= row1 < rows and 0 <= col1 < len(matrix[0]) :
        if data == "Add":
            matrix[row1][col1] += value
        elif data == "Subtract":
            matrix[row1][col1] -= value

    else:
        print("Invalid coordinates")
        continue


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


print_matrix(matrix)