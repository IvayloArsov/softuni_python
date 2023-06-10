room_for_one_person = 18
apartment = 25
president_apartment = 35
days = int(input())
room = input()
review = input()
spent = 0
nights = days - 1
if room == 'room for one person':
    spent = nights * room_for_one_person
elif nights < 10:
    if room == 'apartment':
        spent = nights * apartment * 0.70
    elif room == 'president apartment':
        spent = nights * president_apartment * 0.90
elif 10 <= nights <= 15:
    if room == 'apartment':
        spent = nights * apartment * 0.65
    elif room == 'president apartment':
        spent = nights * president_apartment * 0.85
elif nights > 15:
    if room == 'apartment':
        spent = nights * apartment * 0.50
    elif room == 'president apartment':
        spent = nights * president_apartment * 0.80
if review == 'positive':
    spent *= 1.25
else:
    spent *= 0.90

print(f'{spent:.2f}')
