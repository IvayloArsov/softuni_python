rows, columns = map(int, input().split(", "))
matrix = []

for _ in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)

matrix_sum = sum(sum(row) for row in matrix)
print(matrix_sum)
print(matrix)