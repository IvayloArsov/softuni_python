letter = input()

complete_word, skip_letters_count, guess_word = "",  "",  ""
while letter != "End":
    if letter in "con":
        skip_letters_count += letter
    elif letter.islower() or letter.isupper():
        guess_word += letter
    if "c" in skip_letters_count and "o" in skip_letters_count and "n" in skip_letters_count:
        complete_word += f"{guess_word} "
        guess_word, skip_letters_count = "", ""
    if skip_letters_count.count(letter) > 1:
        guess_word += letter
    letter = input()

print(complete_word)