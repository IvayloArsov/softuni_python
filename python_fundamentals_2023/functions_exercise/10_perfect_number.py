user_input = int(input())


def is_perfect(number):
    divisors = []
    for num in range(number-1, 0, -1):
        if number % num == 0:
            divisors.append(num)
    if sum(divisors) == number:
        return True
    return False


if is_perfect(user_input):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")