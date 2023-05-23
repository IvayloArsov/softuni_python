numbers_list = [int(num) for num in input().split(", ")]
indices = [index for index, number in enumerate(numbers_list) if number % 2 == 0]

print(indices)

## TODO Softuni solution below:
#
# numbers_list = [int(num) for num in input().split(", ")]
# indices = map(
#     lambda x: x if numbers_list[x] % 2 == 0 else "no",
#     range(len(numbers_list))
# )
#
# even_indices = list(filter(lambda a: a!= "no", indices))
# print(even_indices)