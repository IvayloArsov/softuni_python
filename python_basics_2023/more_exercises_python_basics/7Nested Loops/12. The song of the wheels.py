magic_num = int(input())
counter = 0
found = False
password = ""
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:#checks booleans between a,b and c,d to fit the requirements
                    if a*b+c*d == magic_num:#checks if multiplied and summed are equal to the magic number
                        print(f"{a}{b}{c}{d}", end=" ") # prints the fitting combos
                        counter += 1 # adds a counter to keep track of the combos passed
                        if counter == 4: # if combos reach 4, password is found
                            found = True #changes found to True, so that we can use later print statements cleanly
                            password = f'{a}{b}{c}{d}'#saves password at the 4th position
## they might not seem important but \n the print statements make or break judge... don't ask me why...
if found:
    print(f'\nPassword: {password}')
else:
    print("\nNo!")