def rounder(numbers):
    return list(map(round, numbers))


user_input = [float(num) for num in input().split(" ")]
print(rounder(user_input))