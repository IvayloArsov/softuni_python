encrypted_string = input()

def move_letters(sequence, num):
    return sequence[num:]+sequence[:num]


something = move_letters(encrypted_string,3)
print(something)