lines = int(input())
names = [
    input()
    for _ in range(lines)
]
uniques = set(names)
for name in uniques:
    print(name)