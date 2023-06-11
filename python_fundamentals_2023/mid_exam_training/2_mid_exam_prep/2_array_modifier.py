def swap_nums(array, idx1, idx2):
    array[idx1], array[idx2] = array[idx2], array[idx1]
    return array


def multiply_nums(array, idx1, idx2):
    array[idx1] *= array[idx2]
    return array


def decrease(array):
    array = [num - 1 for num in array]
    return array


sample_array = list(map(int, input().split()))
commands = {
    "swap": swap_nums,
    "multiply": multiply_nums,
    "decrease": decrease
}

command = input()
while command != "end":
    command_type, *info = command.split()
    info = list(map(int, info))
    sample_array = commands[command_type](sample_array, *info)
    command = input()
formatted_list = ", ".join(str(num) for num in sample_array)
print(formatted_list)
