rows, columns = [int(el) for el in input().split(", ")]

matrix = [
    [int(el) for el in input().split()]
    for _ in range(rows)
]

for column in range(columns):
    column_sum = sum(row[column] for row in matrix)
    print(column_sum)