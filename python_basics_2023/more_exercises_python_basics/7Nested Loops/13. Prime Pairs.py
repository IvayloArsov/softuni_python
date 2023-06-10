lst = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
first_row = int(input())
second_row = int(input())
third_row = int(input())
fourth_row = int(input())

for x in range(first_row, first_row + third_row + 1):
    for y in range(second_row, second_row + fourth_row + 1):
        if 99 > x > 9 and 99 > y > 9:
            if x in lst and y in lst:
                print(f'{x}{y}')
                