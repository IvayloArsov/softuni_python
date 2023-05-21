def add_and_subtract(a, b, c):
    def sum_numbers(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    result_sum = sum_numbers(a, b)
    result_subtraction = subtract(result_sum, c)
    return result_subtraction


n1 = int(input())
n2 = int(input())
n3 = int(input())

result = add_and_subtract(n1,n2,n3)

print(result)