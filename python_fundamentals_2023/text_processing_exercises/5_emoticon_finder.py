text = input()

for idx, letter in enumerate(text):
    if ":" == letter:
        print(f"{letter}{text[idx + 1]}")