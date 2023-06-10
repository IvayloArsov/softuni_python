days_parked = int(input())
hours_parked = int(input())
parking_fee = 0
price = 0
for day in range(1, days_parked+1):
    daily_fee = 0
    for hour in range(1, hours_parked+1):
        if day % 2 == 0 and hour % 2 == 1:
            price = 2.5
        elif day % 2 == 1 and hour % 2 == 0:
            price = 1.25
        else:
            price = 1
        daily_fee += price
    print(f'Day: {day} - {daily_fee:.2f} leva')

    parking_fee += daily_fee
print(f'Total: {parking_fee:.2f} leva')