num_cars = int(input())
cars_data = dict()

for cars in range(num_cars):
    car, mileage, fuel = input().split("|")
    cars_data[car] = (int(mileage), int(fuel))

while True:
    cmd_line = input()
    if cmd_line == "Stop":
        break
    command_type, *info = cmd_line.split(" : ")


    if command_type == "Drive":
        car, distance, fuel_needed = info
        distance, fuel_needed = int(distance), int(fuel_needed)
        if cars_data[car][1] >= fuel_needed:
            cars_data[car] = (cars_data[car][0] + distance, cars_data[car][1] - fuel_needed)
            print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
            if cars_data[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del cars_data[car]
        else:
            print("Not enough fuel to make that ride")

    elif command_type == "Refuel":
        car, fuel_to_add = info
        fuel_to_add = int(fuel_to_add)
        if cars_data[car][1] + fuel_to_add > 75:
            fuel_to_add = 75 - cars_data[car][1]
        cars_data[car] = (cars_data[car][0], cars_data[car][1] + fuel_to_add)
        print(f"{car} refueled with {fuel_to_add} liters")

    elif command_type == "Revert":
        car, kilometers = info
        kilometers = int(kilometers)
        if cars_data[car][0] - kilometers < 10000:
            cars_data[car] = (10000, cars_data[car][1])
        else:
            cars_data[car] = (cars_data[car][0] - kilometers, cars_data[car][1])
        print(f"{car} mileage decreased by {kilometers} kilometers")

for car, (mileage, fuel) in cars_data.items():
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")