def merge_array(array, start_index, end_index):
    start_index = max(start_index, 0)
    end_index = min(end_index, len(array) - 1)
    merged = ''.join(array[start_index:end_index+1])
    return array[:start_index] + [merged] + array[end_index+1:]

def divide_array(array, index, partitions):
    element = array[index]
    partition_length = len(element) // partitions
    partition_count = partitions
    if len(element) % partitions != 0:
        partition_count -= 1

    divided = [element[i * partition_length: (i + 1) * partition_length] for i in range(partition_count)]
    divided.append(element[(partition_count) * partition_length:])
    return array[:index] + divided + array[index+1:]

def merge_and_divide_array(data, commands):
    array = data.split()

    for command in commands:
        if command == "3:1":
            break

        command_parts = command.split()
        action = command_parts[0]

        if action == "merge":
            start_index = int(command_parts[1])
            end_index = int(command_parts[2])
            array = merge_array(array, start_index, end_index)

        elif action == "divide":
            index = int(command_parts[1])
            partitions = int(command_parts[2])
            array = divide_array(array, index, partitions)

    return ' '.join(array)


input_array = input()
input_commands = []
while True:
    command = input()
    input_commands.append(command)
    if command == "3:1":
        break

result = merge_and_divide_array(input_array, input_commands)
print(result)
