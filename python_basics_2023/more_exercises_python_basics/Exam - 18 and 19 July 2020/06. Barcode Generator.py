# start = int(input())
# end = int(input())
#
# evens = range(1, 10, 2)
#
# for i in range(start // 1000, (end // 1000) + 1):
#     for x in range((start // 100) % 10, (end // 100) % 10 + 1):
#         for y in range((start // 10) % 10, (end // 10) % 10 + 1):
#             for z in range(start % 10, end % 10 + 1):
#                 if i in evens:
#                     if x in evens:
#                         if y in evens:
#                             if z in evens:
#                                 print(f'{i}{x}{y}{z}', end=" ")


# using comprehensions below

# start, end = int(input()), int(input())
# odds = range(1, 10, 2)
# combinations = [
#     [
#         [
#             [print(f'{i}{x}{y}{z}', end=" ")
#              for z in range(start % 10, end % 10 + 1) if z in odds
#              ]
#             for y in range((start // 10) % 10, (end // 10) % 10 + 1) if y in odds
#         ]
#         for x in range((start // 100) % 10, (end // 100) % 10 + 1) if x in odds
#     ]
#     for i in range(start // 1000, (end // 1000) + 1) if i in odds
# ]


start, end = input(), input()

combinations = [
    [
        [
            [
                print(f'{i}{x}{y}{z}', end=" ")
                for z in range(int(start[3]), int(end[3]) + 1)
                if z % 2 != 0
            ]
            for y in range(int(start[2]), int(end[2]) + 1)
            if y % 2 != 0
        ]
        for x in range(int(start[1]), int(end[1]) + 1)
        if x % 2 != 0
    ]
    for i in range(int(start[0]), int(end[0]) + 1)
    if i % 2 != 0
]
