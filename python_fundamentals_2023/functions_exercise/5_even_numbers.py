def evens_only(numbers):
    result = filter(lambda n: n % 2 == 0, numbers)
    return list(result)


user_input = input().split()
user_input = [int(nums) for nums in user_input]

print(evens_only(user_input))