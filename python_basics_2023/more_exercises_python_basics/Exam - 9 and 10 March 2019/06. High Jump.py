record = int(input())

fail_counter = 0
current_bar = record-30
attempts = 0

while fail_counter < 3:
    jump = int(input())
    attempts += 1

    if jump > current_bar:
        fail_counter = 0
        current_bar += 5

        if current_bar > record:
            print(f'Tihomir succeeded, he jumped over {record}cm after {attempts} jumps.')
            break
    else:
        fail_counter += 1
else:
    print(f"Tihomir failed at {current_bar}cm after {attempts} jumps.")