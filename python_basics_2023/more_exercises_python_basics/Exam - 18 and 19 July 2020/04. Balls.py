import math

rng_inpt = int(input())
score = 0
total_score = 0
red_counter = 0
orange_counter = 0
yellow_counter = 0
white_counter = 0
other_counter = 0
division_counter = 0
for _ in range(rng_inpt):
    command = input()

    if command == 'red':
        score = 5
        total_score += score
        red_counter += 1
    if command == 'orange':
        score = 10
        total_score += score
        orange_counter += 1
    if command == 'yellow':
        score = 15
        total_score += score
        yellow_counter += 1
    if command == 'white':
        score = 20
        total_score += score
        white_counter += 1
    if command == 'black':
        score = 0
        total_score = math.floor(total_score/2)
        division_counter += 1
    if command not in ['red','orange','yellow','white','black']:
        score = 0
        other_counter += 1
        total_score += 0

print(f"Total points: {total_score}")
print(f"Red balls: {red_counter}")
print(f"Orange balls: {orange_counter}")
print(f"Yellow balls: {yellow_counter}")
print(f"White balls: {white_counter}")
print(f"Other colors picked: {other_counter}")
print(f"Divides from black balls: {division_counter}")

