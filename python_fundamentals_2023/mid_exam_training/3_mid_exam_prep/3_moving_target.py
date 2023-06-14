def shoot_target(sequence, idx, val):
    if 0 <= idx < len(sequence):
        sequence[idx] -= val
        if sequence[idx] <= 0:
            del sequence[idx]
    return sequence


def add_target(sequence, idx, val):
    if 0 <= idx < len(sequence):
        sequence.insert(idx, val)
    else:
        print("Invalid placement!")
    return sequence


def strike_target(sequence, idx, rad):
    if all([idx - rad >= 0, idx + rad < len(sequence)]):
        start_idx = max(0, idx - rad)
        end_idx = min(len(sequence), idx + rad + 1)
        del sequence[start_idx:end_idx]
    else:
        print("Strike missed!")
    return sequence


commands = {
    "Shoot": shoot_target,
    "Add": add_target,
    "Strike": strike_target
}

targets = [int(num) for num in input().split()]
command = input()
while command != "End":
    command_type, *info = command.split()
    info = list(map(int, info))
    sample_array = commands[command_type](targets, *info)
    command = input()

formatted_list = "|".join(map(str, targets))
print(formatted_list)