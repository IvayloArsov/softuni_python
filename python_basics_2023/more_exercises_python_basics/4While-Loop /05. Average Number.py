n = int(input())
sum_nums = 0
for i in range(0, n):
    current_num = int(input())
    sum_nums += current_num
    avg = sum_nums/n

print(f'{avg:.2f}')