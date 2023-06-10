first_digit_ceil = int(input())
second_digit_ceil = int(input())
third_digit_ceil = int(input())
primes = [2, 3, 5, 7]

for i in range(1, first_digit_ceil + 1):
    for x in range(1, second_digit_ceil + 1):
        for y in range(1, third_digit_ceil + 1):
            if i % 2 == 0:
                if x in primes:
                    if y % 2 == 0:
                        print(f"{i} {x} {y}")
