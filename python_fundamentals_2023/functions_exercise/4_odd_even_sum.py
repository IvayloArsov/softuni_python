user_input = input()

nums = [int(num) for num in list(user_input)]


def sum_evens(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    return sum(evens)
def sum_odds(numbers):
    odds = [num for num in numbers if num % 2 != 0]
    return sum(odds)

print(f"Odd sum = {sum_odds(nums)}, Even sum = {sum_evens(nums)}")