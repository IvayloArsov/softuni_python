destination = input()
package = input()
vip = input()
nights = int(input())

price = 0
if destination not in ['Varna', 'Burgas', 'Bansko', 'Borovets'] or package not in ['withEquipment', 'noEquipment',
                                                                                   'noBreakfast', 'withBreakfast']:
    print('Invalid input!')
else:
    if destination in ['Bansko', 'Borovets']:
        if package == 'withEquipment':
            price = 100
            if vip == 'yes':
                price *= 0.90
        if package == 'noEquipment':
            price = 80
            if vip == 'yes':
                price *= 0.95
    if destination in ['Varna', 'Burgas']:
        if package == 'withBreakfast':
            price = 130
            if vip == 'yes':
                price *= 0.88
        if package == 'noBreakfast':
            price = 100
            if vip == 'yes':
                price *= 0.93

    if 0 >= nights:
        print(f"Days must be positive number!")
    else:
        if nights > 7:
            holiday_price = price * nights - price
        else:
            holiday_price = price * nights

        print(f"The price is {holiday_price:.2f}lv! Have a nice time!")
