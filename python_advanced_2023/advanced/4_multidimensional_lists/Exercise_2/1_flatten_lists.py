segments = input().split('|')[::-1]
matrix = [list(map(int, segment.strip().split())) for segment in segments]
for row in range(len(matrix)):
    for num in matrix[row]:
        print(num, end=" ")