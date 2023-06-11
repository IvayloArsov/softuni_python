efficiency = [int(input()) for _ in range(3)]
students = int(input())

time_needed = 0
while students > 0:
    time_needed += 1
    if time_needed % 4 != 0:
        students -= sum(efficiency)

print(f"Time needed: {time_needed}h.")