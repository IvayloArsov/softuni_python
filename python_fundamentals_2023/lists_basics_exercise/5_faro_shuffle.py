deck = input().split(' ')
shuffles = int(input())

for _ in range(shuffles):
    first_half = deck[:len(deck) // 2]
    second_half = deck[len(deck) // 2:]

    r = []
    for a, b in zip(first_half, second_half):
        r.append(a)
        r.append(b)

    deck = r
print(deck)
