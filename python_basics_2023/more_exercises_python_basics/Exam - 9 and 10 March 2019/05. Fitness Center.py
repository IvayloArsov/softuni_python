clients = int(input())
back = 0
chest = 0
legs = 0
t_abs = 0
protein_shake = 0
protein_bar = 0
workouts = 0
proteins = 0

for sale in range(clients):
    command = input()
    if command == 'Back':
        back += 1
        workouts += 1
    elif command == 'Chest':
        chest += 1
        workouts += 1
    elif command == 'Legs':
        legs += 1
        workouts += 1
    elif command == 'Abs':
        t_abs += 1
        workouts += 1
    elif command == 'Protein shake':
        protein_shake += 1
        proteins += 1
    elif command == 'Protein bar':
        protein_bar += 1
        proteins += 1
print(f'{back} - back\n'
      f'{chest} - chest\n'
      f'{legs} - legs\n'
      f'{t_abs} - abs\n'
      f'{protein_shake} - protein shake\n'
      f'{protein_bar} - protein bar\n'
      f'{workouts/clients*100:.2f}% - work out\n'
      f'{proteins/clients*100:.2f}% - protein')