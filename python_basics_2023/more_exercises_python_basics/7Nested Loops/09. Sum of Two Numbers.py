start_range = int(input())
end_range = int(input())
magic_num = int(input())
combo_counter = 0 # keeps count of the number of combinations passed
found = False #combination not yet found, so it is false

for x in range(start_range, end_range+1):
    for y in range(start_range, end_range+1):
        combo_counter += 1 # counter whenever combination is made
        if (x+y) == magic_num:
            print(f'Combination N:{combo_counter} ({x} + {y} = {magic_num})')
            #be careful with whitespaces cuz judge system HATES white spaces in a print statement <3
            found = True #first occurrence of a combination, so it breaks the boolean
            break
    if found: #breaks out of the loop
        break

if not found:
    print(f'{combo_counter} combinations - neither equals {magic_num}')
