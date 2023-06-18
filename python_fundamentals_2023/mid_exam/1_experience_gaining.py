experience_needed = float(input())
battles_count = int(input())

counter_battles = 0
flag = False
for _ in range(battles_count):
    experience_gained = float(input())
    counter_battles += 1
    if counter_battles % 3 == 0:
        experience_gained *= 1.15
    if counter_battles % 5 == 0:
        experience_gained *= 0.90
    if counter_battles % 15 == 0:
        experience_gained *= 1.05
    experience_needed -= experience_gained
    if experience_needed <= 0:
        flag = True
        break

if flag:
    print(f"Player successfully collected his needed experience for {counter_battles} battles.")
else:
    print(f"Player was not able to collect the needed experience, {experience_needed:.2f} more needed.")
