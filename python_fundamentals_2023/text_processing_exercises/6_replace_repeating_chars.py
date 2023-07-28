def replace_sequence_with_single_letter(input_str):
    result = ''
    prev_char = None

    for char in input_str:
        if char != prev_char:
            result += char
            prev_char = char

    return result


input_str = input()
modified_str = replace_sequence_with_single_letter(input_str)
print(modified_str)

