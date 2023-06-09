number_pieces = int(input())

pieces_info = {}

for piece in range(number_pieces):
    piece_name, *info = input().split("|")
    pieces_info[piece_name] = info


def add_piece(piece, composer, key):
    if piece in pieces_info:
        return f"{piece} is already in the collection!"

    pieces_info[piece] = [composer, key]
    return f"{piece} by {composer} in {key} added to the collection!"


def remove_piece(piece):
    if piece in pieces_info:
        del pieces_info[piece]
        return f"Successfully removed {piece}!"
    return f"Invalid operation! {piece} does not exist in the collection."


def change_key(piece, new_key):
    if piece in pieces_info:
        pieces_info[piece][1] = new_key
        return f"Changed the key of {piece} to {new_key}!"
    return f"Invalid operation! {piece} does not exist in the collection."


def show_result():
    [print(f"{piece} -> Composer: {pieces_info[piece][0]}, Key: {pieces_info[piece][1]}") for piece in pieces_info]


command_func = {
    "Add": add_piece,
    "Remove": remove_piece,
    "ChangeKey": change_key
}

command = input()
while command != "Stop":
    command_type, *info = command.split("|")
    print(command_func[command_type](*info))
    command = input()

show_result()