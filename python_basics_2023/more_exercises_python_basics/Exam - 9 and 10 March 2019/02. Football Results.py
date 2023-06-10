first_match = input()
second_match = input()
third_match = input()

wins = 0
losses = 0
draws = 0


if first_match[0] > first_match[2]:
    wins += 1
if first_match[0] < first_match[2]:
    losses += 1
if first_match[0] == first_match[2]:
    draws += 1
if second_match[0] > second_match[2]:
    wins += 1
if second_match[0] < second_match[2]:
    losses += 1
if second_match[0] == second_match[2]:
    draws += 1
if third_match[0] > third_match[2]:
    wins += 1
if third_match[0] < third_match[2]:
    losses += 1
if third_match[0] == third_match[2]:
    draws += 1

print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws} ")
