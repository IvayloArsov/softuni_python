n = int(input())

lst_ = []
for _ in range(n):
    lst_.append(int(input()))

cmd = input()
filtered = []
if cmd == 'even':
    filtered = filter(lambda x: x % 2 == 0, lst_)

if cmd == 'odd':
    filtered = filter(lambda x: x % 2 != 0, lst_)

if cmd == 'negative':
    filtered = filter(lambda x: x < 0, lst_)

if cmd == 'positive':
    filtered = filter(lambda x: x >= 0, lst_)

print(list(filtered))
