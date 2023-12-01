expression = input()
# start = []
# end = []
# for idx, element in enumerate(expression):
#     if element == "(":
#         start.append(idx)
#     elif element == ")":
#         end.append(idx+1)
#     if start and end:
#         print(expression[start.pop():end.pop()])
#

new_stack = []
for idx, el in enumerate(expression):
    if el == "(":
        new_stack.append(idx)
    elif el == ")":
        start_idx, last_idx = new_stack.pop(), idx+1
        print(expression[start_idx: last_idx])