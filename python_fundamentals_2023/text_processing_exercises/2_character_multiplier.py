def calculate_sum_of_multiplied_char_codes(str1, str2):
    total_sum = 0
    min_length = min(len(str1), len(str2))

    for i in range(min_length):
        total_sum += ord(str1[i]) * ord(str2[i])

    # Add the remaining character codes if one string is longer than the other
    if len(str1) > len(str2):
        for i in range(min_length, len(str1)):
            total_sum += ord(str1[i])
    elif len(str2) > len(str1):
        for i in range(min_length, len(str2)):
            total_sum += ord(str2[i])

    return total_sum


# Get input from the user
input_str = input()
str1, str2 = input_str.split()

# Calculate and print the result
result = calculate_sum_of_multiplied_char_codes(str1, str2)
print(result)
