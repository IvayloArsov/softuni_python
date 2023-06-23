ledger = {}
for _ in range(int(input())):
    name = input()
    grade = float(input())

    if name not in ledger:
        ledger[name] = []
    ledger[name].append(grade)

for name, grades in ledger.items():
    avg_score = sum(grades) / len(grades)
    if avg_score >= 4.50:
        print(f"{name} -> {avg_score:.2f}")