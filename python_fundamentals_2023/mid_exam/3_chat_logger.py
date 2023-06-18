chat_log = []
while True:
    command = input()
    if command == "end":
        for text in chat_log:
            print(text)
        break

    if command.startswith("Chat"):
        command, text = command.split()
        chat_log.append(text)
    elif command.startswith("Delete"):
        command, text = command.split()
        if text in chat_log:
            chat_log.remove(text)
        else:
            continue
    elif command.startswith("Edit"):
        command, old_text, new_text = command.split()
        if old_text in chat_log:
            index = chat_log.index(old_text)
            chat_log[index] = new_text
        else:
            continue
    elif command.startswith("Pin"):
        command, text = command.split()
        if text in chat_log:
            index = chat_log.index(text)
            chat_log.append(chat_log.pop(index))
    elif command.startswith("Spam"):
        command, *text = command.split()
        chat_log.extend(text)
