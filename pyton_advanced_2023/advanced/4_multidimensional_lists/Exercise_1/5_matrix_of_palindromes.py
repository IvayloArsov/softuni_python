def generate_palindrome_matrix(r, c):
    matrix = [['' for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            first_letter = chr(ord('a') + i)
            middle_letter = chr(ord('a') + i + j)
            last_letter = chr(ord('a') + i)
            palindrome = first_letter + middle_letter + last_letter
            matrix[i][j] = palindrome
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))


rows, columns = map(int, input().split())

palindrome_matrix = generate_palindrome_matrix(rows, columns)
print_matrix(palindrome_matrix)
