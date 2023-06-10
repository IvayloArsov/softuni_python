deck = input().split(' ')
smallest = int(input())

lst_ = [
    int(num)
    for num in deck
]

for _ in range(smallest):
    lst_.remove(min(lst_))


print(*lst_, sep=', ')