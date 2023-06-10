movies = [
    'A Star Is Born',
    'Bohemian Rhapsody',
    'Green Book',
    'The Favourite'
]
projs = [
    'normal',
    'luxury',
    'ultra luxury'
]
selected_movie = input()
selected_proj = input()
number_tickets = int(input())

price = 0

if selected_movie == movies[0]:
    if selected_proj == projs[0]:
        price = 7.50
    if selected_proj == projs[1]:
        price = 10.50
    if selected_proj == projs[2]:
        price = 13.50
if selected_movie == movies[1]:
    if selected_proj == projs[0]:
        price = 7.35
    if selected_proj == projs[1]:
        price = 9.45
    if selected_proj == projs[2]:
        price = 12.75
if selected_movie == movies[2]:
    if selected_proj == projs[0]:
        price = 8.15
    if selected_proj == projs[1]:
        price = 10.25
    if selected_proj == projs[2]:
        price = 13.25
if selected_movie == movies[3]:
    if selected_proj == projs[0]:
        price = 8.75
    if selected_proj == projs[1]:
        price = 11.55
    if selected_proj == projs[2]:
        price = 13.95

print(f'{selected_movie} -> {number_tickets*price:.2f} lv.')