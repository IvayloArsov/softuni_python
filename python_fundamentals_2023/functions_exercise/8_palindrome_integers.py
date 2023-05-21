def is_palindrome_int(number):
    if str(number) == str(number)[::-1]:
        return True
    return False


user_input = input().split(", ")
user_input = [int(nums) for nums in user_input]

for num in user_input:
    print(is_palindrome_int(num))