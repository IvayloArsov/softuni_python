words = input().split()

for word in words:
    starting_char = []
    for char in word:
        if char.isdigit():
            starting_char.append(char)
    word = word[len(starting_char):]
    starting_char = chr(int("".join(starting_char)))
    word = starting_char+word
    word_list = list(word)
    word_list[1], word_list[-1] = word_list[-1], word_list[1]
    new_word = "".join(word_list)

    print(new_word, end=" ")
