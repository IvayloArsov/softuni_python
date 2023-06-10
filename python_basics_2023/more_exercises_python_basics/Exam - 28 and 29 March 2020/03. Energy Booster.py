fruit_input = input()
size_input = input()
num_sets = int(input())


price = 0
multi = 0
if size_input == 'small':
    multi = 2
    if fruit_input == 'Watermelon':
        price = 56

    if fruit_input == 'Mango':
        price = 36.66

    if fruit_input == 'Pineapple':
        price = 42.10

    if fruit_input == 'Raspberry':
        price = 20

if size_input == 'big':
    multi = 5
    if fruit_input == 'Watermelon':
        price = 28.70

    if fruit_input == 'Mango':
        price = 19.60

    if fruit_input == 'Pineapple':
        price = 24.80

    if fruit_input == 'Raspberry':
        price = 15.20
total = price*multi*num_sets

if 400 <= total <= 1000:
    total *= .85
if total > 1000:
    total /= 2

print(f'{total:.2f} lv.')