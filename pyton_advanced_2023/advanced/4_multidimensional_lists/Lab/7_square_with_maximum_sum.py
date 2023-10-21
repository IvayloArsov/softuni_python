rows, cols = map(int, input().split(", "))

matrix_ = [
    [int(el) for el in input().split(", ")]
    for _ in range(rows)
]


def find_max_sum_square(matrix):
    max_sum = float("-inf")
    max_submatrix = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            submatrix_sum = sum(matrix[i][j:j+2] + matrix[i+1][j:j+2])
            if submatrix_sum > max_sum:
                max_sum = submatrix_sum
                max_submatrix = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
    return max_submatrix, max_sum


submatrix, max_sum = find_max_sum_square(matrix_)
print(submatrix[0], submatrix[1])
print(submatrix[2], submatrix[3])
print(max_sum)
