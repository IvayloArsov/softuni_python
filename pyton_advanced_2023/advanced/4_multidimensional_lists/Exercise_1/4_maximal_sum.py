rows, cols = map(int, input().split())

matrix_ = [
    [int(el) for el in input().split()]
    for _ in range(rows)
]


def find_max_sum_square(matrix):
    max_sum = float("-inf")
    max_submatrix = []
    for i in range(len(matrix)-2):
        for j in range(len(matrix[0])-2):
            submatrix_sum = sum(matrix[i][j:j+3] + matrix[i+1][j:j+3] + matrix[i+2][j:j+3])
            if submatrix_sum > max_sum:
                max_sum = submatrix_sum
                max_submatrix = [
                    matrix[i][j:j+3],
                    matrix[i+1][j:j+3],
                    matrix[i+2][j:j+3]
                ]
    return max_submatrix, max_sum


submatrix, max_sum = find_max_sum_square(matrix_)

print("Sum =", max_sum)
for row in submatrix:
    print(*row)