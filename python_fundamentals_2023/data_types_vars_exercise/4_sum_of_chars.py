score = 0

for _ in range(1, int(input())+1):
    char = input()
    score += ord(char)
print(f"The sum equals: {score}")