def absolutes(numbers):
    return list(map(abs, numbers))


user_input = [float(num) for num in input().split(" ")]
print(absolutes(user_input))