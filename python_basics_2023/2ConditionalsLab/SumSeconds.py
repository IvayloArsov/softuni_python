import math

first = int(input())
second = int(input())
third = int(input())
total = first+second+third
minutes = math.floor(total // 60)
seconds = total % 60
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')