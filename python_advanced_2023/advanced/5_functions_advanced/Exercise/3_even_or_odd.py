def even_odd(*args):
    *numbers, command = args
    if "even" in command:
        return [num for num in numbers if num % 2 == 0]
    return [num for num in numbers if num % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
