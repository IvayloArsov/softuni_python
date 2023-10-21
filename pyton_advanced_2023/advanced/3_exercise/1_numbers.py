first_set = set(map(int, input().split()))
second_set = set(map(int, input().split()))
input_lines = int(input())

for _ in range(input_lines):
    command = input()
    if command == "Check Subset":
        print(first_set.issuperset(second_set))
    else:
        info_nums = [int(number) for number in command.split() if number.isdigit()]

        if command.startswith("Add"):
            if command.split()[1] == "First":
                for item in info_nums:
                    first_set.add(item)
            elif command.split()[1] == "Second":
                for item in info_nums:
                    second_set.add(item)
        elif command.startswith("Remove"):
            if command.split()[1] == "First":
                for item in info_nums:
                    first_set.discard(item)
            elif command.split()[1] == "Second":
                for item in info_nums:
                    second_set.discard(item)


print(", ".join(map(str, sorted(first_set))))
print(", ".join(map(str, sorted(second_set))))


##TODO This solution gets 81/100 ... I don't know what's breaking it
# first_set = set(map(int, input().split()))
# second_set = set(map(int, input().split()))
# input_lines = int(input())
#
# for _ in range(input_lines):
#     command, *info_nums = input().split()
#     nums = [int(x) for x in info_nums if x.isdigit()]
#
#     if "Check" in command and "Subset" in info_nums:
#         print(first_set.issuperset(second_set))
#     else:
#         target_set = first_set if command == "Add" and "First" in info_nums else second_set
#         if command.startswith("Add") or command.startswith("Remove"):
#             target_set.update(nums) if command.startswith("Add") else target_set.difference_update(nums)
#
# print(", ".join(map(str, sorted(first_set))))
# print(", ".join(map(str, sorted(second_set))))
