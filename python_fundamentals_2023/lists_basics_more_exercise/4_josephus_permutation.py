soldiers = [int(soldier) for soldier in input().split(" ")]
step = int(input())


def josephus_with_step(circle, k):
    dead_list = []
    index = 0
    while len(circle) > 0:
        index = (index + k - 1) % len(circle)
        killed_soldier = circle.pop(index)
        dead_list.append(killed_soldier)

    return dead_list


result = josephus_with_step(soldiers, step)
result_str = ','.join(map(str, result))
output = f'[{result_str}]'
print(output)