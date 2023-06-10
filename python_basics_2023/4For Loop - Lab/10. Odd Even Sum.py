# Да се напише програма, която чете n-на брой цели числа,
# подадени от потребителя и проверява дали сумата от
# числата на четни позиции е равна на сумата на числата на нечетни позиции.


num = int(input())
evens = 0
odds = 0
for i in range(1, num + 1):
    num = int(input())
    if i % 2 == 0:
        evens += num
    else:
        odds += num
if odds == evens:
    print(f'Yes')
    print(f'Sum = {evens}')
else:
    print(f'No')
    print(f'Diff = {abs(evens - odds):.0f}')
