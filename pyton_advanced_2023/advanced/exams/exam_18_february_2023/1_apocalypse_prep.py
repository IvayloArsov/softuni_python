from collections import deque

textiles = deque(map(int, input().split()))
medicaments = list(map(int, input().split()))

healing_items = {}

while textiles and medicaments:
    cur_textile = textiles.popleft()
    cur_medicament = medicaments.pop()
    product = cur_medicament + cur_textile

    if product == 30:
        healing_items['Patch'] = healing_items.get('Patch', 0) + 1
    elif product == 40:
        healing_items['Bandage'] = healing_items.get('Bandage', 0) + 1
    elif product == 100:
        healing_items['MedKit'] = healing_items.get('MedKit', 0) + 1
    elif product > 100:
        healing_items['MedKit'] = healing_items.get('MedKit', 0) + 1
        product -= 100
        medicaments[-1] += product
    else:
        cur_medicament += 10
        medicaments.append(cur_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

sorted_items = sorted(healing_items.items(), key=lambda x: (-x[1], x[0]))
for item, amount in sorted_items:
    if int(amount) > 0:
        print(f"{item} - {amount}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")

