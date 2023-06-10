number_list = [int(i) for i in input().split()]
user_input = input().split()

while user_input[0] != "end":
    even = [i for i in number_list if i % 2 == 0]
    odd = [i for i in number_list if i % 2 != 0]

    if user_input[0] == "exchange":
        if 0 <= int(user_input[1]) < len(number_list):
            number_list = number_list[int(user_input[1]) + 1:] + number_list[:int(user_input[1]) + 1]
        else:
            print(f'Invalid index')

    elif user_input[0] == "max":
        if user_input[1] == "even" and even:
            print((len(number_list) - number_list[::-1].index(max(even)) - 1))
        elif user_input[1] == "odd" and odd:
            print((len(number_list) - number_list[::-1].index(max(odd)) - 1))
        else:
            print('No matches')

    elif user_input[0] == "min":
        if user_input[1] == "even" and even:
            print((len(number_list) - number_list[::-1].index(min(even)) - 1))
        elif user_input[1] == "odd" and odd:
            print((len(number_list) - number_list[::-1].index(min(odd)) - 1))
        else:
            print('No matches')

    elif user_input[0] == "first":
        if 0 < int(user_input[1]) <= len(number_list):
            if user_input[2] == "even":
                print(even[0:int(user_input[1])])
            else:
                print(odd[0:int(user_input[1])])
        else:
            print(f"Invalid count")

    elif user_input[0] == "last":
        if 0 < int(user_input[1]) <= len(number_list):
            if user_input[2] == "even":
                print(even[-int(user_input[1]):])
            else:
                print(odd[-int(user_input[1]):])
        else:
            print(f"Invalid count")
    user_input = input().split()

print(number_list)