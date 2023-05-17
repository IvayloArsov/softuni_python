juniors = int(input())
seniors = int(input())
race = input()

price_j= 0
price_s = 0
participants = juniors+seniors
if participants < 50:
    discount = 1
if race == 'trail':
    price_j = 5.50
    price_s = 7
elif race == 'cross-country' and participants >= 50:
    price_j = 8*0.75
    price_s = 9.50*0.75
elif race == 'cross-country':
    price_j = 8
    price_s = 9.50
elif race == 'downhill':
    price_j = 12.25
    price_s = 13.75
elif race == 'road':
    price_j = 20
    price_s = 21.50


collected = (juniors*price_j + price_s*seniors)
charity = collected*0.95
print(f'{charity:.2f}')