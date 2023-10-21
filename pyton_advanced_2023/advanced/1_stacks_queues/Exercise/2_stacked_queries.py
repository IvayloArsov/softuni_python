n = int(input())
stack = []


for _ in range(n):
    command, *info = input().split()
    if command == "1":
        stack.append(*info)
    elif stack:
        if command == "2":
            stack.pop()
        if command == "3":
            max_num = max(stack)
            print(max_num)
        if command == "4":
            min_num = min(stack)
            print(min_num)
formatted_nums = ", ".join(str(num) for num in reversed(stack))
print(formatted_nums)