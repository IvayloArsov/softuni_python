user_input1 = int(input())
user_input2 = int(input())


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


division = factorial(user_input1)/factorial(user_input2)

print(f"{division:.2f}")