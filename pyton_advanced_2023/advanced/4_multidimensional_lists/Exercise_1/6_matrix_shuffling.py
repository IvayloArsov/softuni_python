rows, cols = map(int, input().split())
matrix = [
    [
        el for el in input().split()
    ]
    for _ in range(rows)
]

while True:
    command = input()
    if command == "END":
        break

    data, *info = command.split()
    if data == "swap" and len(info) == 4:
        row1, col1, row2, col2 = map(int, info)
        if 0 <= row1 < rows and 0 <= col1 < cols and 0 <= row2 < rows and 0 <= col2 < cols:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for row in matrix:
                print(" ".join(str(el) for el in row))
        else:
            print("Invalid input!")

    else:
        print("Invalid input!")