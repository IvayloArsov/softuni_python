def blacklist_name(sequence, name):
    if name in sequence:
        print(f"{name} was blacklisted.")
        for i in range(len(sequence)):
            if sequence[i] == name:
                sequence[i] = "Blacklisted"
        return sequence
    else:
        print(f"{name} was not found.")
        return sequence


def error_idx(sequence, idx):
    idx = int(idx)
    if 0 <= idx < len(sequence):
        if sequence[idx] != "Blacklisted" and sequence[idx] != "Lost":
            print(f"{sequence[idx]} was lost due to an error.")
            sequence[idx] = "Lost"
    else:
        pass


def change_name(sequence, idx, new_name):
    idx = int(idx)
    if 0 <= idx < len(sequence):
        print(f"{sequence[idx]} changed his username to {new_name}.")
        sequence[idx] = new_name
    else:
        pass


def report(sequence):
    blacklisted = sequence.count("Blacklisted")
    lost = sequence.count("Lost")
    print(f"Blacklisted names: {blacklisted}")
    print(f"Lost names: {lost}")
    print(" ".join(sequence))


commands = {
    "Blacklist": blacklist_name,
    "Error": error_idx,
    "Change": change_name
}

name_sequence = list(map(str, input().split(", ")))

command = input()
while True:
    if command == "Report":
        break
    else:
        command_type, *info = command.split(" ")
        commands[command_type](name_sequence, *info)
        command = input()

report(name_sequence)
