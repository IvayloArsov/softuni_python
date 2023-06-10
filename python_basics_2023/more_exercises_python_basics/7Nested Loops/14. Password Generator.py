import string

n = int(input())
l = int(input())
alphabet_string_lower = string.ascii_lowercase

for i in range(1, n+1):
    for x in range(1, n+1):
        for y in string.ascii_lowercase[:l]:
            for z in string.ascii_lowercase[:l]:
                for t in range(1, n+1):
                    if x < t > i:
                        print(f"{i}{x}{y}{z}{t}", end=" ")