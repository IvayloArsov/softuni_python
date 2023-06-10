input_sequence = input().split(" ")
input_sequence = [int(num) for num in input_sequence]
midpoint = len(input_sequence) // 2

left_car = input_sequence[:midpoint]
right_car = input_sequence[midpoint + 1:][::-1]


def lap_calc(car):
    best_time = 0
    for lap in car:
        if lap == 0:
            best_time *= 0.8
        else:
            best_time += lap
    return best_time


left = lap_calc(left_car)
right = lap_calc(right_car)

if left < right:
    print(f"The winner is left with total time: {left:.1f}")
else:
    print(f"The winner is right with total time: {right:.1f}")
