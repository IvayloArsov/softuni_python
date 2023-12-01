def is_balanced(expression):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_map = {")": "(", "}": "{", "]": "["}

    for bracket in expression:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack or stack[-1] != bracket_map[bracket]:
                return False
            stack.pop()
        else:
            return False
    return len(stack) == 0


input_expression = input()
if is_balanced(input_expression):
    print("YES")
else:
    print("NO")