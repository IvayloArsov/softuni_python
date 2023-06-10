slct_season = input()
sex_group = input()
num_students = int(input())
num_nights = int(input())
price = 0
discount = 1
sport = ''

if slct_season == 'Winter':
    price = 9.60
    if sex_group == 'boys':
        sport = 'Judo'
    elif sex_group == 'girls':
        sport = 'Gymnastics'
    elif sex_group == 'mixed':
        sport = 'Ski'
        price = 10
elif slct_season == 'Spring':
    price = 7.20
    if sex_group == 'boys':
        sport = 'Tennis'
    elif sex_group == 'girls':
        sport = 'Athletics'
    elif sex_group == 'mixed':
        sport = 'Cycling'
        price = 9.50

elif slct_season == 'Summer':
    price = 15
    if sex_group == 'boys':
        sport = 'Football'
    elif sex_group == 'girls':
        sport = 'Volleyball'
    elif sex_group == 'mixed':
        sport = 'Swimming'
        price = 20

if num_students >= 50:
    discount = 0.5
elif 50 > num_students >= 20:
    discount = 0.85
elif 20 > num_students >= 10:
    discount = 0.95
sub_total = num_nights * num_students * price * discount
print(f'{sport} {sub_total:.2f} lv.')