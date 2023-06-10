luggage_above_20 = float(input())
luggage_weight = float(input())
travel_days = int(input())
n_luggage = int(input())
multiplier = 1
price = luggage_above_20

if luggage_weight < 10:
    price *= 0.20
elif 10 <= luggage_weight <= 20:
    price *= 0.50
else:
    price = luggage_above_20

if travel_days > 30:
    multiplier = 1.10
elif 7 <= travel_days <= 30:
    multiplier = 1.15
elif travel_days < 7:
    multiplier = 1.40
else:
    multiplier = 1

total = (price * multiplier) * n_luggage

print(f" The total price of bags is: {total:.2f} lv. ")
