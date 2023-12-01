def reverse_text(input_string: str):
    for ch in input_string[::-1]:
        yield ch


for char in reverse_text("step"):
    print(char, end='')