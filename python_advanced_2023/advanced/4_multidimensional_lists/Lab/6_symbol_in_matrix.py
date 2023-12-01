rows = int(input())
matrix = [input() for _ in range(rows)]


def find_element(matrix, target):
    for row in range(rows):
        if target in matrix[row]:
            return row, matrix[row].find(target)
    return f"{target} does not occur in the matrix"


target = input()
indices = find_element(matrix, target)
print(indices)