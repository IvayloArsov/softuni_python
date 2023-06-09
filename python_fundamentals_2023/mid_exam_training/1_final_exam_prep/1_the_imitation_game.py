def move_letters(sequence, num):
    sequence = sequence[num:]+sequence[:num]
    return sequence
def insert_letters(sequence, num, letter):
    sequence = sequence[:num]+letter+sequence[num:]
    return sequence
def change_letters(sequence, old_letter, new_letter):
    return sequence.replace(old_letter, new_letter)


encrypted_string = input()
while True:
    command = input()
    if command == "Decode":
        break
    else:
        split_command = command.split("|")
        if split_command[0] == "ChangeAll":
            old_char = split_command[1]
            new_char = split_command[2]
            encrypted_string = change_letters(encrypted_string, old_char, new_char)
        elif split_command[0] == "Insert":
            idx = int(split_command[1])
            char = split_command[2]
            encrypted_string = insert_letters(encrypted_string, idx, char)
        elif split_command[0] == "Move":
            idx = int(split_command[1])
            encrypted_string = move_letters(encrypted_string, idx)

print("The decrypted message is:", encrypted_string)
