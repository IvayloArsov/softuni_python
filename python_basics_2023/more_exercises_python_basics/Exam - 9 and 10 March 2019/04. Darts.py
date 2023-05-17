player_name = input()

starting_pts = 301
successful_shots = 0
unsuccessful_shots = 0

field = input()
while field != 'Retire':

    pts = int(input())

    if field == 'Double':
        pts *= 2
    elif field == 'Triple':
        pts *= 3
    if pts <= starting_pts:
        successful_shots += 1
        starting_pts -= pts

        if not starting_pts:
            print(f"{player_name} won the leg with {successful_shots} shots.")
            break
    else:
        unsuccessful_shots += 1

    field = input()

else:
    print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')