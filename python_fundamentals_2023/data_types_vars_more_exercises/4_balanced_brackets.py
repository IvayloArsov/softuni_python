def check_balanced_parentheses(lines):
    balance = 0
    for line in lines:
        if "(" in line:
            balance += 1
        elif ")" in line:
            balance -= 1
        if 0 != balance != 1:
            return "UNBALANCED"
    else:
        return "BALANCED"


n = int(input())
lines = [input() for _ in range(n)]
result = check_balanced_parentheses(lines)
print(result)