capacity = float(input())
suitcases_counter = 0
inefficiency_counter = 0

while True:
    suitcase = input()
    inefficiency_counter += 1

    if suitcase == 'End':
        print('Congratulations! All suitcases are loaded!')
        break

    if inefficiency_counter % 3 == 0:
        suitcase = float(suitcase) * 1.10

    if float(suitcase) > capacity or capacity <= 0:
        print('No more space!')
        break

    capacity -= float(suitcase)
    suitcases_counter += 1

print(f'Statistic: {suitcases_counter} suitcases loaded.')