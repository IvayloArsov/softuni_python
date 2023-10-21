rows = int(input())

matrix = [
    [int(el) for el in input().split(" ")]
    for _ in range(rows)
]

diagonal_sum1 = sum(matrix[i][i] for i in range(len(matrix)))
diagonal_sum2 = sum(matrix[i][-i-1] for i in range(len(matrix)))
print(abs(diagonal_sum1-diagonal_sum2))