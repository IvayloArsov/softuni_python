numbers = [int(num) for num in input().split(", ")]

positives = list(filter(lambda x: x >= 0, numbers))
negative = list(filter(lambda x: x < 0, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))
odd = list(filter(lambda x: x % 2 != 0, numbers))

print(f'Positive: {", ".join(map(str, positives))}')
print(f'Negative: {", ".join(map(str, negative))}')
print(f'Even: {", ".join(map(str, even))}')
print(f'Odd: {", ".join(map(str, odd))}')