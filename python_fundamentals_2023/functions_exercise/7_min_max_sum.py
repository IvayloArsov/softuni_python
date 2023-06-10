user_input = input().split()
user_input = [int(nums) for nums in user_input]


def multi_analysis(numbers):
    return min(numbers), max(numbers), sum(numbers)


min_,max_,sum_ = multi_analysis(user_input)
print(f"The minimum number is {min_}\n"
      f"The maximum number is {max_}\n"
      f"The sum number is: {sum_}")