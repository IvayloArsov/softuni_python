import math

magnolia = int(input()) * 3.25
hyacinth = int(input()) * 4
roses = int(input()) * 3.5
cactus = int(input()) * 8
gift = float(input())

sales = (magnolia+hyacinth+roses+cactus)*0.95
change = abs(gift-sales)

if sales >= gift:
    print(f'She is left with {math.floor(change)} leva.')
else:
    print(f'She will have to borrow {math.ceil(change)} leva.')