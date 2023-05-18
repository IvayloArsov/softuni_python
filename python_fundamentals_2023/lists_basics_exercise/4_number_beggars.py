nums = input().split(', ')
beggars = int(input())

handpicked = [
    [
        int(num)
        for num in
        nums[num::beggars]
    ]
    for num in range(beggars)
]

sums = [
    sum(sublist)
    for sublist in handpicked
]

print(sums)
