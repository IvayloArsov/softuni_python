user_input = [int(input()) for _ in range(3)]


def find_solution(number_list):
    if any(num == 0 for num in number_list):
        return 'zero'
    negatives = sum(1 for num in number_list if num < 0)

    return "negative" if negatives % 2 != 0 else "positive"


result = find_solution(user_input)
print(result)
