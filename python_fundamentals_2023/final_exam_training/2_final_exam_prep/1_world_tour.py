def add_stop(sequence, num, new_string):
    sequence = sequence[:num] + new_string + sequence[num:]
    return sequence

def remove_stop(sequence, start_idx, end_idx):
    sequence = sequence[:start_idx] + sequence[end_idx+1:]
    return sequence

def switch_stops(sequence, old_stop, new_stop):
    return sequence.replace(old_stop, new_stop)


stops = input()
while True:
    command = input()
    if command == "Travel":
        break
    else:
        split_command = command.split(":")

        if split_command[0] == "Add Stop" and 0 <= int(split_command[1]) < len(stops):
            stops = add_stop(stops, int(split_command[1]), split_command[2])
        elif split_command[0] == "Remove Stop" \
                and 0 <= int(split_command[1]) < len(stops)\
                and 0 <= int(split_command[2]) < len(stops):
            stops = remove_stop(stops, int(split_command[1]), int(split_command[2]))
        elif split_command[0] == "Switch":
            stops = switch_stops(stops, split_command[1], split_command[2])
    print(stops)

print("Ready for world tour! Planned stops:", stops)
