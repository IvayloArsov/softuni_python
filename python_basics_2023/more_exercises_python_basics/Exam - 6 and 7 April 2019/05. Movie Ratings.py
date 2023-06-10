import sys

number_of_movies = int(input())

total_score = 0
max_score = -sys.maxsize
max_name = ''
min_score = sys.maxsize
min_name = ''

for movie in range(number_of_movies):
    name = input()
    score = float(input())
    total_score += score
    if score > max_score:
        max_score = score
        max_name = name
    elif score < min_score:
        min_score = score
        min_name = name

print(f'{max_name} is with highest rating: {max_score}')
print(f'{min_name} is with lowest rating: {min_score}')
print(f'Average rating: {total_score/number_of_movies:.1f}')
