
main_msg = input()
command = input()


while command != "Reveal":
    command_type, *info = command.split(":|:")
    found_error = False
    if command_type == "ChangeAll":
        main_msg = main_msg.replace(info[0], info[1])

    elif command_type == "Reverse":
        substring = info[0]
        if substring not in main_msg:
            print("error")
            found_error = True
        else:
            main_msg = main_msg.replace(substring, "", 1) + substring[::-1]

    elif command_type == "InsertSpace":
        index_for_insert = int(info[0])
        main_msg = main_msg[:index_for_insert] + " " + main_msg[index_for_insert:]

    if not found_error:
        print(main_msg)

    command = input()

print(f"You have a new text message: {main_msg}")