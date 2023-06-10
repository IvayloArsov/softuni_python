type_fuel = input()
qnty = int(input())
club_card = input()
l = {
    'Diesel': 2.33,
    'Gasoline': 2.22,
    'Gas': 0.93
}

price = 0

if type_fuel in l.keys() and club_card == 'Yes':
    l = {
        'Diesel': 2.33 - 0.12,
        'Gasoline': 2.22 - 0.18,
        'Gas': 0.93 - 0.08
    }
if qnty > 25:
    price = l[type_fuel] * qnty * 0.90
elif 20 < qnty <= 25:
    price = l[type_fuel] * qnty * 0.92
else:
    price = l[type_fuel] * qnty
print(f'{price:.2f} lv.')
