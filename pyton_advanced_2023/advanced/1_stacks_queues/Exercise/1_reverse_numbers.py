nums = input().split()
stack = []
for n in range(len(nums)):
    stack.append(nums.pop())

print(" ".join(stack))