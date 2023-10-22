from collections import deque

monsters = deque(map(int, input().split(',')))
damage = list(map(int, input().split(',')))

total_killed_monsters = 0

while monsters and damage:
    hit = damage.pop()
    armor = monsters.popleft()

    if hit >= armor:
        total_killed_monsters += 1
        hit -= armor
        if damage:
            damage[-1] += hit
        elif not damage and hit > 0:
            damage.append(hit)
    else:
        armor -= hit
        monsters.append(armor)

if not monsters:
    print("All monsters have been killed!")
if not damage:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {total_killed_monsters}")
