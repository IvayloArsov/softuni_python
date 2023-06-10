first_letter = input()
last_letter = input()
odd_letter = input()

start_letter = ord(first_letter.lower())
end_letter = ord(last_letter.lower())
unwanted_letter = ord(odd_letter.lower())
counter = 0
for i in range(start_letter, end_letter+1):
    for x in range(start_letter,end_letter+1):
        for y in range(start_letter,end_letter+1):
            if i != unwanted_letter and x != unwanted_letter and y != unwanted_letter:
                print(f'{chr(i)}{chr(x)}{chr(y)}', end=" ")
                counter += 1
print(counter)
