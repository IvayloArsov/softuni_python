def smallest(numbers):
    return min(numbers)

numbers = []
for _ in range(3):
    numbers.append(int(input()))

print(smallest(numbers))