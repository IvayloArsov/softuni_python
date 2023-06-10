def solve(a, b, operator):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = int(a / b)
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b

    return result


operand = input()
num1 = int(input())
num2 = int(input())

print(solve(num1, num2, operand))