from itertools import permutations


def possible_permutations(input_list):
    for perm in permutations(input_list):
        yield list(perm)


# def possible_permutations(lst):
#     if len(lst) == 0:
#         yield []
#     else:
#         for i in range(len(lst)):
#             rest = lst[:i] + lst[i+1:]
#             for p in possible_permutations(rest):
#                 yield [lst[i]] + p

my_list = [1, 2, 3]
for perm in possible_permutations(my_list):
    print(perm)
