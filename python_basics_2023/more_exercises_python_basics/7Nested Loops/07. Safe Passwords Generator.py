import string

a = int(input())
b = int(input())
pass_max_gen = int(input())
pass_counter = 0
alphabet_list_upper = string.printable

for first_symbol in range(35, 56):
    for last_symbol in range(64, 97):
        for num_1 in range(1, a+1):
            for num_2 in range(1, b+1):

                if pass_counter == pass_max_gen:
                    break
                if first_symbol > 55:
                    first_symbol = 35
                if last_symbol > 96:
                    last_symbol = 64
                print(f'{chr(first_symbol)}{chr(last_symbol)}{num_1}{num_2}{chr(last_symbol)}{chr(first_symbol)}', end= "|")
                pass_counter += 1
                first_symbol += 1
                last_symbol += 1
                if num_1 == a and num_2 ==b:
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break