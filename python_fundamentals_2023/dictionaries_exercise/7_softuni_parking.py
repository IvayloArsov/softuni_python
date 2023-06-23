# init empty dictionary to hold the values of the registered vehicles
cars = dict()
for _ in range(int(input())):
    command = input()
    # check the input command
    if command.startswith("register"):
        token, name, car_plate = command.split()
        # check membership of the owner's name in the database, if false throws an exception
        if name not in cars:
            cars[name] = car_plate
            print(f"{name} registered {car_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {cars.get(name)}")
    # check membership of the owner's name in the database, if false throws an exception
    elif command.startswith("unregister"):
        token, name = command.split()
        if name in cars:
            del cars[name]
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")
# checks if the database isn't empty, else prints the full dictionary
if cars:
    for name, plate in cars.items():
        print(f"{name} => {plate}")