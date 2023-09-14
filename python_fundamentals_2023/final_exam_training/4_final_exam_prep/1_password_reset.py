raw_string = input()

cmd_line = input()

while cmd_line != "Done":

    command, *info = cmd_line.split()
    if command == "TakeOdd":
        raw_string = raw_string[1::2]
        print(raw_string)
    elif command == "Cut":
        idx, len_substr = info
        idx = int(idx)
        len_substr = int(len_substr)
        raw_string = raw_string[:idx]+raw_string[idx+len_substr:]
        print(raw_string)
    elif command == "Substitute":
        old_str, new_str = info
        if old_str == new_str or old_str not in raw_string:
            print("Nothing to replace!")
        else:
            raw_string = raw_string.replace(old_str, new_str)
            print(raw_string)
    cmd_line = input()

print(f"Your password is: {raw_string}")