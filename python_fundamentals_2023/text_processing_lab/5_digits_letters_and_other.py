import re


def separate_string(string):
    digits = re.findall(r'\d', string)
    letters = re.findall(r'[a-zA-Z]', string)
    other_chars = re.findall(r'[^a-zA-Z0-9]', string)

    return digits, letters, other_chars


string = input()
digits, letters, other_chars = separate_string(string)

print("".join(digits))
print("".join(letters))
print("".join(other_chars))
