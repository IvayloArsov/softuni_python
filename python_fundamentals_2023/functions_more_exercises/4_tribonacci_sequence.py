def tribonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n == 3:
        return [1, 1, 2]
    else:
        sequence = [1, 1, 2]
        for i in range(3, n):
            next_num = sequence[i-1] + sequence[i-2] + sequence[i-3]
            sequence.append(next_num)
        return sequence


user_input = int(input())

result = tribonacci(user_input)
print(*result)