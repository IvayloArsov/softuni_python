type_fuel = input()
remaining = int(input())
l = ['Diesel', 'Gasoline', 'Gas']

if remaining >= 25 and type_fuel in l:
    print(f'You have enough {type_fuel.lower()}.')
elif remaining < 25 and type_fuel in l:
    print(f'Fill your tank with {type_fuel.lower()}!')
else:
    print('Invalid fuel!')
