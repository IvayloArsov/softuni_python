def func_executor(*args):
    results = []
    for func, params in args:
        results.append(f"{func.__name__} - {func(*params)}")
    return "\n".join(results)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
