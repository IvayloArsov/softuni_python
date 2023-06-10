import sys

n = int(input())
max_num = -sys.maxsize
sum_nums = 0

for i in range(0, n):
    num = int(input())
    sum_nums += num
    if num > max_num:
        max_num = num
if (sum_nums - max_num) == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    sum_nums = sum_nums - max_num
    print(f'Diff = {abs(sum_nums - max_num)}')
