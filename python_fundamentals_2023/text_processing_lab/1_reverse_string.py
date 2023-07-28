while True:
    word = input()
    if word == "end":
        break
    word_reversed = word[::-1]

    # word_reversed = ""
    # for el in reversed(word):
    #     word_reversed += el

    print(word + " = " + word_reversed)
