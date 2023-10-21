rows, cols = map(int, input().split())

matrix_ = [
    [char for char in input().split()]
    for _ in range(rows)
]


def find_identical_squares(matrix):
    identicals = 0
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
                identicals += 1
    return identicals


something = find_identical_squares(matrix_)
print(something)