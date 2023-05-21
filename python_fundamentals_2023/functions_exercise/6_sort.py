def sort_list(numbers):
    result = sorted(numbers)
    return list(result)


user_input = input().split()
user_input = [int(nums) for nums in user_input]

print(sort_list(user_input))