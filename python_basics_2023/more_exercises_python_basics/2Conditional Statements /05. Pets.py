import math

d = int(input())
kg = int(input())
dog = float(input())
cat = float(input())
tortoise = float(input())/1000
total_food = (dog+cat+tortoise)*d

if kg >= total_food:
    print(f'{math.floor(kg-total_food)} kilos of food left.')
else:
    print(f'{math.ceil(total_food-kg)} more kilos of food are needed.')