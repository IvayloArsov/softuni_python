rows = int(input())
matrix = []

for _ in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)

flattened_matrix = [
    element
    for row in matrix
    for element in row
]
print(flattened_matrix)