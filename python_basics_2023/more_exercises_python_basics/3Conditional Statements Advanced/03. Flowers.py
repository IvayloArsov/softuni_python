chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday_check = input()

s1 = {
    'chrysanthemums': 2,
    'roses': 4.1,
    'tulips': 2.5
}
s2 = {
    'chrysanthemums': 3.75,
    'roses': 4.50,
    'tulips': 4.15
}
num_flowers = chrysanthemums + roses + tulips
multiplier = 1
total = 0
sum = 0
if holiday_check == 'Y':
    multiplier = 1.15
elif holiday_check == 'N':
    multiplier = 1

if season == 'Spring' or season == 'Summer':
    total = (roses * s1['roses'] + tulips * s1['tulips'] + chrysanthemums * s1['chrysanthemums'])
elif season == 'Autumn' or season == 'Winter':
    total = (roses * s2['roses'] + tulips * s2['tulips'] + chrysanthemums * s2['chrysanthemums'])

sum = total * multiplier

if roses >= 10 and season == 'Winter':
    sum = total * multiplier * 0.90
elif tulips > 7 and season == 'Spring':
    sum = total * multiplier * 0.95
if num_flowers > 20:
    sum *= 0.80
print(f'{sum+2:.2f}')