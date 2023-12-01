rows = int(input())

matrix = [
    [int(el) for el in input().split()]
    for _ in range(rows)
]

diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
print(diagonal_sum)