import math

n = int(input())
left_sum = 0
right_sum = 0

for i in range(0, n):
    nums_left = float(input())
    left_sum += nums_left
for i in range(0, n):
    nums_right = float(input())
    right_sum += nums_right
if left_sum == right_sum:
    print(f'Yes, sum = {left_sum:.0f}')
else:
    print(f'No, diff = {math.fabs(right_sum - left_sum):.0f}')
