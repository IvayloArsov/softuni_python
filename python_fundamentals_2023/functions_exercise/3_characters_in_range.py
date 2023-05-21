def chars_in_between(first, last):
    for char in range(ord(first)+1, ord(last)):
        print(chr(char), end=' ')


start = input()
end = input()
chars_in_between(start, end)
